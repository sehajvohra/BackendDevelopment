---
layout: null
title: Backend Development
---
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Backend Development</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script>
(function () {
  var theme = 'light';
  try {
    var saved = localStorage.getItem('bd-theme');
    var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    theme = saved || (prefersDark ? 'dark' : 'light');
  } catch (e) {}
  document.documentElement.setAttribute('data-theme', theme);
})();
</script>
<style>
:root {
  color-scheme: light;
  --bg: #f7f9fc;
  --grid: #e4eaf4;
  --grid-major: #d3dcec;
  --ink: #14213d;
  --muted: #5d6b86;
  --accent: #1f4fd1;
  --accent-soft: #c9d6f7;
  --card: #ffffff;
  --line: #cfd8e8;
  --font-hand: "Caveat", "Segoe Print", "Bradley Hand", cursive;
  --font-body: "Inter", "Segoe UI", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", "SFMono-Regular", Consolas, monospace;
}

html[data-theme="dark"] {
  color-scheme: dark;
  --bg: #0c1424;
  --grid: #131e33;
  --grid-major: #1a2842;
  --ink: #e6edf9;
  --muted: #93a1bf;
  --accent: #7aa2ff;
  --accent-soft: #1d2f5c;
  --card: #111b30;
  --line: #263553;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  background-color: var(--bg);
  background-image:
    linear-gradient(var(--grid-major) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid-major) 1px, transparent 1px),
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 120px 120px, 120px 120px, 24px 24px, 24px 24px;
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.5;
  transition: background-color 0.25s ease, color 0.25s ease;
}

.wrap {
  max-width: 940px;
  margin: 0 auto;
  padding: 64px 24px 72px;
}

/* ---------- Header ---------- */

.page-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 24px;
}

.page-title {
  font-family: var(--font-hand);
  font-weight: 700;
  font-size: 3.6rem;
  line-height: 1;
  letter-spacing: 0.01em;
  margin: 0;
  color: var(--ink);
}

.squiggle {
  display: block;
  width: 160px;
  height: 16px;
  margin: 6px 0 14px;
  color: var(--accent);
}

.equation {
  font-family: var(--font-mono);
  font-size: 0.95rem;
  color: var(--accent);
  margin: 0 0 6px;
}

.page-subtitle {
  color: var(--muted);
  font-size: 1rem;
  margin: 0;
}

.theme-toggle {
  flex: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px 12px;
  cursor: pointer;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--ink);
  transition: border-color 0.15s ease, box-shadow 0.15s ease, background-color 0.25s ease;
}

.theme-toggle:hover {
  border-color: var(--accent);
  box-shadow: 3px 3px 0 var(--accent-soft);
}

.theme-toggle svg { width: 16px; height: 16px; color: var(--accent); }

.icon-sun, .lbl-light { display: none; }
html[data-theme="dark"] .icon-sun,
html[data-theme="dark"] .lbl-light { display: inline-block; }
html[data-theme="dark"] .icon-moon,
html[data-theme="dark"] .lbl-dark { display: none; }

a:focus-visible,
.theme-toggle:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: 4px;
}

/* ---------- Headings ---------- */

.section-title {
  font-family: var(--font-hand);
  font-weight: 700;
  font-size: 2.2rem;
  line-height: 1.1;
  margin: 56px 0 20px;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 10px;
}

.section-title svg {
  width: 26px;
  height: 26px;
  color: var(--accent);
  flex: none;
}

.section-title::after {
  content: "";
  flex: 1;
  border-top: 1px dashed var(--line);
  margin-left: 6px;
}

.subsection-title {
  font-family: var(--font-hand);
  font-weight: 700;
  font-size: 1.6rem;
  line-height: 1.1;
  color: var(--ink);
  margin: 32px 0 16px;
  padding-left: 12px;
  border-left: 2px solid var(--accent);
  display: flex;
  align-items: baseline;
  gap: 10px;
}

.greek {
  font-family: var(--font-mono);
  font-size: 1rem;
  font-weight: 500;
  color: var(--accent);
}

/* ---------- Cards ---------- */

.card-grid {
  display: grid;
  gap: 16px;
}

.card-grid--wide { grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); }
.card-grid--narrow { grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); }

.card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 16px 18px 18px;
  transition: border-color 0.15s ease, box-shadow 0.15s ease, background-color 0.25s ease;
}

.card:hover {
  border-color: var(--accent);
  box-shadow: 4px 4px 0 var(--accent-soft);
}

.card-label {
  display: block;
  font-family: var(--font-hand);
  font-weight: 700;
  font-size: 1.6rem;
  line-height: 1.1;
  color: var(--ink);
  margin-bottom: 10px;
}

.card--sm { padding: 14px 16px 16px; }
.card--sm .card-label { font-size: 1.4rem; }

.card-links {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 16px;
}

.card-link {
  font-family: var(--font-mono);
  font-size: 0.82rem;
  color: var(--accent);
  text-decoration: none;
}

.card-link::before {
  content: ">";
  color: var(--muted);
  margin-right: 6px;
}

.card-link:hover {
  text-decoration: underline;
  text-underline-offset: 4px;
}

/* ---------- Footer ---------- */

.page-footer {
  margin-top: 72px;
  padding-top: 20px;
  border-top: 1px dashed var(--line);
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--muted);
}

@media (max-width: 640px) {
  .wrap { padding: 40px 18px 56px; }
  .page-header { flex-direction: column; gap: 18px; }
  .page-title { font-size: 2.9rem; }
  .section-title { font-size: 1.9rem; }
}

@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; }
}
</style>
</head>
<body>
<main class="wrap">
<header class="page-header">
<div>
<h1 class="page-title">Backend Development</h1>
<svg class="squiggle" viewBox="0 0 160 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M2 8 C 12 -2, 22 18, 32 8 S 52 -2, 62 8 S 82 18, 92 8 S 112 -2, 122 8 S 142 18, 152 8"/></svg>
<p class="equation">f(backend) = lab + theory</p>
<p class="page-subtitle">Lab experiments, lecture notes, and resources for the course.</p>
</div>
<button class="theme-toggle" id="theme-toggle" type="button" aria-label="Toggle dark mode" aria-pressed="false">
<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
<span class="lbl-dark">dark</span><span class="lbl-light">light</span>
</button>
</header>

<h2 class="section-title"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 3h6M10 3v6L5 19a2 2 0 0 0 1.8 3h10.4A2 2 0 0 0 19 19l-5-10V3M7.5 15h9"/></svg>Lab Experiments</h2>
<div class="card-grid card-grid--wide">
<div class="card">
<span class="card-label">Experiment 1</span>
<div class="card-links">
<a class="card-link" href="Lab/Exp%201/index.html">open</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%201/Report.html">report</a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 5</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%205">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%205/Report.html">report</a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 7_8</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%207_8">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%207_8/Report.html">report</a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 12</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%2012/Report.html">report</a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 12B</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012B">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%2012B/Report.html">report</a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 13A</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%2013A/Report.html">report</a>
</div>
</div>
</div>

<h2 class="section-title"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 5H6l6 7-6 7h12"/></svg>Assignments</h2>
<div class="card-grid card-grid--wide">
<div class="card">
<span class="card-label">Assignment 1</span>
<div class="card-links">
<a class="card-link" href="Theory/Assignments/Assignment_1/index.html">open</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Assignments/Assignment_1/Report.html">report</a>
</div>
</div>
<div class="card">
<span class="card-label">Assignment 2</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Assignments/Assignment_2">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Assignments/Assignment_2/Assignment%202%20PostgreSQL%20as%20SQL%20+%20NoSQL%20Working%20with%20JSONB.html">report</a>
</div>
</div>
</div>

<h2 class="section-title"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><ellipse cx="12" cy="12" rx="10" ry="4"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(60 12 12)"/><ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(120 12 12)"/><circle cx="12" cy="12" r="1.4" fill="currentColor"/></svg>Theory</h2>

<h3 class="subsection-title"><span class="greek">&alpha;</span>Unit 1</h3>
<div class="card-grid card-grid--narrow">
<div class="card card--sm">
<span class="card-label">Lecture 3</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture3">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture3/Report.html">report</a>
</div>
</div>
<div class="card card--sm">
<span class="card-label">Lecture 4</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture4/Report.html">report</a>
</div>
</div>
<div class="card card--sm">
<span class="card-label">Lecture 5</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture5/Report.html">report</a>
</div>
</div>
<div class="card card--sm">
<span class="card-label">Lecture 6</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture6/Report.html">report</a>
</div>
</div>
<div class="card card--sm">
<span class="card-label">Lecture 7</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture7">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture7/Report.html">report</a>
</div>
</div>
<div class="card card--sm">
<span class="card-label">Lecture 8</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture8/Report.html">report</a>
</div>
</div>
</div>

<h3 class="subsection-title"><span class="greek">&beta;</span>Unit 2</h3>
<div class="card-grid card-grid--narrow">
<div class="card card--sm">
<span class="card-label">Lecture 13</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture13">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit2/Lecture13/Report.html">report</a>
</div>
</div>
<div class="card card--sm">
<span class="card-label">Lecture 14</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture14">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit2/Lecture14/Report.html">report</a>
</div>
</div>
<div class="card card--sm">
<span class="card-label">Lecture 15</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture15">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit2/Lecture15/Report.html">report</a>
</div>
</div>
<div class="card card--sm">
<span class="card-label">Lecture 19</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19">github</a>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit2/Lecture19/Report.html">report</a>
</div>
</div>
</div>

<footer class="page-footer">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment">view repository</a>
</footer>
</main>

<script>
(function () {
  var root = document.documentElement;
  var btn = document.getElementById('theme-toggle');
  if (!btn) { return; }

  function sync() {
    btn.setAttribute('aria-pressed', root.getAttribute('data-theme') === 'dark' ? 'true' : 'false');
  }

  sync();

  btn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    sync();
    try { localStorage.setItem('bd-theme', next); } catch (e) {}
  });
})();
</script>
</body>
</html>
