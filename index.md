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
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@600;700&display=swap" rel="stylesheet">
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
  --bg: #faf8fb;
  --ink: #201a2b;
  --ink-soft: #5b5468;
  --muted: #8b8496;
  --violet: #5b3ec8;
  --violet-deep: #3d2896;
  --violet-pale: #ece6fb;
  --accent: #ff6f61;
  --accent-2: #ffb648;
  --card-bg: #ffffff;
  --card-border: #e7e1f4;
  --card-shadow: 0 2px 6px rgba(61, 40, 150, 0.06);
  --card-shadow-hover: 0 14px 30px rgba(61, 40, 150, 0.16);
  --glow-1: rgba(91, 62, 200, 0.08);
  --glow-2: rgba(255, 111, 97, 0.10);
  --radius-md: 14px;
  --font-display: "Poppins", "Segoe UI", system-ui, sans-serif;
  --font-body: "Inter", "Segoe UI", system-ui, sans-serif;
}

html[data-theme="dark"] {
color-scheme: dark;
--bg: #14111c;
--ink: #f1eef9;
--ink-soft: #c8c1da;
--muted: #9a94ad;
--violet: #9a80f0;
--violet-deep: #c3b1fa;
--violet-pale: #2a2340;
--accent: #ff8a7a;
--accent-2: #ffc266;
--card-bg: #1e1a2c;
--card-border: #322a48;
--card-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);
--card-shadow-hover: 0 14px 30px rgba(0, 0, 0, 0.45);
--glow-1: rgba(154, 128, 240, 0.12);
--glow-2: rgba(255, 138, 122, 0.08);
}

- { box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
margin: 0;
background: var(--bg);
background-image:
radial-gradient(circle at 12% 8%, var(--glow-1), transparent 40%),
radial-gradient(circle at 88% 0%, var(--glow-2), transparent 45%);
background-attachment: fixed;
color: var(--ink);
font-family: var(--font-body);
line-height: 1.5;
transition: background-color 0.25s ease, color 0.25s ease;
}

.wrap {
max-width: 920px;
margin: 0 auto;
padding: 56px 24px 96px;
}

/_ ---------- Header ---------- _/

.page-header {
display: flex;
align-items: flex-start;
justify-content: space-between;
gap: 24px;
margin-bottom: 8px;
}

.page-title {
font-family: var(--font-display);
font-weight: 700;
font-size: 2.6rem;
letter-spacing: -0.03em;
line-height: 1.15;
margin: 0 0 8px;
color: var(--ink);
}

.page-subtitle {
color: var(--muted);
font-size: 1.05rem;
margin: 0 0 24px;
}

.theme-toggle {
flex: none;
display: inline-flex;
align-items: center;
gap: 8px;
background: var(--card-bg);
border: 1px solid var(--card-border);
border-radius: 999px;
padding: 6px 14px 6px 6px;
cursor: pointer;
font-family: var(--font-body);
font-size: 0.85rem;
font-weight: 600;
color: var(--ink-soft);
box-shadow: var(--card-shadow);
transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease, background-color 0.25s ease;
margin-top: 6px;
}

.theme-toggle:hover {
transform: translateY(-2px);
box-shadow: var(--card-shadow-hover);
border-color: var(--violet);
}

.theme-toggle:focus-visible,
.card-link:focus-visible {
outline: 2px solid var(--violet);
outline-offset: 3px;
border-radius: 6px;
}

.toggle-icon {
width: 28px;
height: 28px;
border-radius: 50%;
display: inline-flex;
align-items: center;
justify-content: center;
background: linear-gradient(135deg, var(--violet), var(--accent));
font-size: 0.95rem;
line-height: 1;
}

/_ ---------- Section headings ---------- _/

.section-title {
font-family: var(--font-display);
font-weight: 600;
font-size: 1.6rem;
margin: 48px 0 18px;
color: var(--ink);
display: flex;
align-items: center;
gap: 12px;
}

.section-title::before {
content: "";
width: 8px;
height: 8px;
border-radius: 50%;
background: linear-gradient(135deg, var(--violet), var(--accent));
flex: none;
}

.subsection-title {
font-family: var(--font-display);
font-weight: 600;
font-size: 1.15rem;
color: var(--violet-deep);
margin: 28px 0 16px;
padding-left: 20px;
border-left: 3px solid var(--violet-pale);
}

/_ ---------- Cards ---------- _/

.card-grid {
display: grid;
gap: 16px;
margin: 0 0 8px;
}

.card-grid--wide { grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); }
.card-grid--narrow { grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); }

.card {
background: var(--card-bg);
border: 1px solid var(--card-border);
border-radius: var(--radius-md);
padding: 20px;
box-shadow: var(--card-shadow);
transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease, background-color 0.25s ease;
position: relative;
overflow: hidden;
}

.card::after {
content: "";
position: absolute;
inset: 0;
border-radius: inherit;
padding: 1px;
background: linear-gradient(135deg, var(--violet), var(--accent-2));
opacity: 0;
transition: opacity 0.22s ease;
-webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
-webkit-mask-composite: xor;
mask-composite: exclude;
pointer-events: none;
}

.card:hover {
transform: translateY(-4px);
box-shadow: var(--card-shadow-hover);
border-color: transparent;
}

.card:hover::after { opacity: 1; }

.card--narrow { text-align: center; padding: 18px 12px; }

.card-label {
display: block;
font-weight: 700;
font-size: 1.02rem;
color: var(--violet-deep);
margin-bottom: 12px;
}

.card-links {
display: flex;
align-items: center;
gap: 12px;
flex-wrap: wrap;
position: relative;
z-index: 2;
}

.card--narrow .card-links {
flex-direction: column;
gap: 6px;
}

.card--narrow .card-divider { display: none; }

.card-link {
display: inline-flex;
align-items: center;
gap: 4px;
font-size: 0.88rem;
font-weight: 500;
color: var(--muted);
text-decoration: none;
transition: color 0.2s ease;
}

.card-link:hover { color: var(--accent); }

.card-link .arrow { transition: transform 0.22s ease; }
.card-link:hover .arrow { transform: translateX(3px); }

.card-divider {
color: var(--card-border);
font-size: 0.9rem;
}

.card--new { border-color: var(--accent-2); }

.card--new .card-label::after {
content: "NEW";
margin-left: 8px;
font-size: 0.62rem;
font-weight: 700;
letter-spacing: 0.06em;
color: #fff;
background: linear-gradient(90deg, var(--accent), var(--accent-2));
padding: 2px 7px;
border-radius: 999px;
vertical-align: middle;
}

@media (max-width: 640px) {
.wrap { padding: 36px 18px 72px; }
.page-header { flex-direction: column; gap: 12px; }
.page-title { font-size: 2rem; }
.card-links { gap: 8px; }
}

@media (prefers-reduced-motion: reduce) {

- { transition: none !important; }
html { scroll-behavior: auto; }
}
</style>
</head>
<body>
<main class="wrap">
<header class="page-header">
<div>
<h1 class="page-title">Backend Development</h1>
<p class="page-subtitle">Lab experiments, lecture notes, and resources for the course.</p>
</div>
<button class="theme-toggle" id="theme-toggle" type="button" aria-label="Toggle dark mode">
<span class="toggle-icon" id="toggle-icon">🌙</span>
<span id="toggle-label">Dark mode</span>
</button>
</header>

<h2 class="section-title">Lab Experiments</h2>
<div class="card-grid card-grid--wide">
<div class="card">
<span class="card-label">Experiment 1</span>
<div class="card-links">
<a class="card-link" href="Lab/Exp%201/index.html">Open <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%201/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 5</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%205">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%205/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 7 &amp; 8</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment">GitHub <span class="arrow">→</span></a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 12</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%2012/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 12B</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012B">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%2012B/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card">
<span class="card-label">Experiment 13A</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%2013A/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
</div>

<h2 class="section-title">Assignments</h2>
<div class="card-grid card-grid--wide">
<div class="card">
<span class="card-label">Assignment 1</span>
<div class="card-links">
<a class="card-link" href="Theory/Assignments/Assignment_1/index.html">Open <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Assignments/Assignment_1/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card">
<span class="card-label">Assignment 2</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Assignments/Assignment_2">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Assignments/Assignment_2/Assignment%202%20PostgreSQL%20as%20SQL%20+%20NoSQL%20Working%20with%20JSONB.html">Report <span class="arrow">→</span></a>
</div>
</div>
</div>

<h2 class="section-title">Theory</h2>

<h3 class="subsection-title">Unit 1</h3>
<div class="card-grid card-grid--narrow">
<div class="card card--narrow">
<span class="card-label">Lecture 3</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture3">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture3/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card card--narrow">
<span class="card-label">Lecture 4</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture4/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card card--narrow">
<span class="card-label">Lecture 5</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture5/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card card--narrow">
<span class="card-label">Lecture 6</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture6/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card card--narrow">
<span class="card-label">Lecture 7</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture7">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture7/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card card--narrow">
<span class="card-label">Lecture 8</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit1/Lecture8/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
</div>

<h3 class="subsection-title">Unit 2</h3>
<div class="card-grid card-grid--narrow">
<div class="card card--narrow">
<span class="card-label">Lecture 13</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture13">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit2/Lecture13/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card card--narrow">
<span class="card-label">Lecture 14</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture14">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit2/Lecture14/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
<div class="card card--narrow">
<span class="card-label">Lecture 15</span>
<div class="card-links">
<a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture15">GitHub <span class="arrow">→</span></a>
<span class="card-divider">|</span>
<a class="card-link" href="https://sehajvohra.github.io/BackendDevelopment/Theory/Unit2/Lecture15/Report.html">Report <span class="arrow">→</span></a>
</div>
</div>
</div>
</main>

<script>
(function () {
  var root = document.documentElement;
  var toggleBtn = document.getElementById('theme-toggle');
  var icon = document.getElementById('toggle-icon');
  var label = document.getElementById('toggle-label');
  if (!toggleBtn || !icon || !label) { return; }

  function sync() {
    var dark = root.getAttribute('data-theme') === 'dark';
    icon.textContent = dark ? '☀️' : '🌙';
    label.textContent = dark ? 'Light mode' : 'Dark mode';
  }

  sync();

  toggleBtn.addEventListener('click', function () {
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    sync();
    try { localStorage.setItem('bd-theme', next); } catch (e) {}
  });
})();
</script>
</body>
</html>
