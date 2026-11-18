// Minimal CDP verifier: loads each page in headless Chrome, reports
// console errors, failed images, horizontal overflow, moment mount state.
// Usage: node verify.mjs [port] [width]
import { spawn } from 'node:child_process';

const PORT = 8901;
const DEBUG = 9333;
const WIDTH = Number(process.argv[2] || 1440);
const HEIGHT = WIDTH < 500 ? 844 : 900;
const PAGES = ['index', 'work', 'about', 'contact', 'privacy', '404'];
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';

let chrome = null;
async function cdpAlive() {
  try { const r = await fetch(`http://127.0.0.1:${DEBUG}/json/version`); return r.ok; } catch { return false; }
}
if (!(await cdpAlive())) {
  chrome = spawn(CHROME, [
    '--headless=new', '--disable-gpu',
    `--remote-debugging-port=${DEBUG}`,
    `--user-data-dir=D:/WebApps/shruti/shots/.chrome-prof-v5`,
    `--window-size=${WIDTH},${HEIGHT}`,
    '--no-first-run', '--hide-scrollbars', 'about:blank'
  ], { stdio: 'ignore' });
}

const sleep = ms => new Promise(r => setTimeout(r, ms));
async function getWsUrl() {
  for (let i = 0; i < 40; i++) {
    try {
      const r = await fetch(`http://127.0.0.1:${DEBUG}/json/version`);
      const j = await r.json();
      return j.webSocketDebuggerUrl;
    } catch { await sleep(250); }
  }
  throw new Error('chrome CDP never came up');
}

// one shared browser-level ws; create a target per page via /json/new
async function newTab(url) {
  const r = await fetch(`http://127.0.0.1:${DEBUG}/json/new?${encodeURIComponent(url)}`, { method: 'PUT' });
  return r.json();
}

function session(wsUrl) {
  const ws = new WebSocket(wsUrl);
  let id = 0; const pend = new Map(); const events = [];
  ws.onmessage = e => {
    const m = JSON.parse(e.data);
    if (m.id && pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); }
    else if (m.method) events.push(m);
  };
  const send = (method, params = {}) => new Promise(res => {
    const i = ++id; pend.set(i, res);
    ws.send(JSON.stringify({ id: i, method, params }));
  });
  return { ws, send, events, ready: new Promise(r => ws.onopen = r) };
}

const AUDIT = `(() => {
  const de = document.documentElement;
  const imgs = [...document.images].map(i => ({src: i.getAttribute('src'), ok: i.complete && i.naturalWidth > 0}));
  const broken = imgs.filter(i => !i.ok);
  const overflowX = de.scrollWidth > de.clientWidth + 1 || document.body.scrollWidth > window.innerWidth + 1;
  const moments = [...document.querySelectorAll('[data-moment]')].map(el => ({id: el.dataset.moment, mounted: el.dataset.momentMounted || null, failed: el.dataset.momentFailed || null}));
  const h1s = document.querySelectorAll('h1').length;
  const emptySections = [...document.querySelectorAll('main section')].filter(s => s.innerText.trim().length < 20).length;
  return JSON.stringify({title: document.title, broken, overflowX, scrollW: de.scrollWidth, winW: innerWidth, moments, h1s, emptySections, jsReady: de.dataset.momentsReady || null});
})()`;

for (const p of PAGES) {
  const tab = await newTab(`http://localhost:${PORT}/${p}.html`);
  const s = session(tab.webSocketDebuggerUrl);
  await s.ready;
  await s.send('Runtime.enable');
  await s.send('Page.enable');
  await s.send('Emulation.setDeviceMetricsOverride', { width: WIDTH, height: HEIGHT, deviceScaleFactor: 1, mobile: WIDTH < 500 });
  // wait for load + moments settle
  await sleep(3500);
  const r = await s.send('Runtime.evaluate', { expression: AUDIT, returnByValue: true });
  const errors = s.events.filter(e => e.method === 'Runtime.exceptionThrown' || (e.method === 'Runtime.consoleAPICalled' && e.params.type === 'error'));
  const out = JSON.parse(r.result?.result?.value || '{}');
  console.log(`\n=== ${p}.html ===`);
  console.log(' title:', out.title);
  console.log(' broken imgs:', out.broken?.length ? JSON.stringify(out.broken) : 'none');
  console.log(' overflowX:', out.overflowX, `(scrollW ${out.scrollW} vs win ${out.winW})`);
  console.log(' moments:', JSON.stringify(out.moments), 'ready:', out.jsReady);
  console.log(' h1 count:', out.h1s, '| near-empty sections:', out.emptySections);
  if (errors.length) console.log(' console errors:', errors.length, errors.slice(0, 3).map(e => JSON.stringify(e.params).slice(0, 200)));
  await fetch(`http://127.0.0.1:${DEBUG}/json/close/${tab.id}`);
  s.ws.close();
}
chrome?.kill();
process.exit(0);
