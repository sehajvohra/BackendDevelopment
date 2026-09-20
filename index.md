---
layout: home
title: Backend Development
---

<style>

:root {
  --bg:            #faf8fb;
  --bg-soft:       #f2eefb;
  --ink:           #201a2b;
  --ink-soft:      #5b5468;
  --muted:         #8b8496;
  --violet:        #5b3ec8;
  --violet-deep:   #3d2896;
  --violet-pale:   #ece6fb;
  --accent:        #ff6f61;
  --accent-2:      #ffb648;
  --card-bg:       #ffffff;
  --card-border:   #e7e1f4;
  --card-shadow:   0 2px 6px rgba(61, 40, 150, 0.06);
  --card-shadow-hover: 0 14px 30px rgba(61, 40, 150, 0.16);
  --radius-lg:     18px;
  --radius-md:     14px;
  --font-display:  "Poppins", "Segoe UI", system-ui, sans-serif;
  --font-body:     "Inter", "Segoe UI", system-ui, sans-serif;
}

.page-wrap-inner * {
  box-sizing: border-box;
}

body {
  background: var(--bg);
  background-image:
    radial-gradient(circle at 12% 8%, rgba(91, 62, 200, 0.08), transparent 40%),
    radial-gradient(circle at 88% 0%, rgba(255, 111, 97, 0.10), transparent 45%);
  background-attachment: fixed;
  color: var(--ink);
  font-family: var(--font-body);
}

.page-title {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 2.6rem;
  letter-spacing: -0.03em;
  margin: 0 0 8px;
  color: var(--ink);
}

.page-subtitle {
  color: var(--muted);
  font-size: 1.05rem;
  margin: 0 0 40px;
}

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

.card-grid {
  display: grid;
  gap: 16px;
  margin: 0 0 8px;
}

.card-grid--wide {
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.card-grid--narrow {
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}

.card {
  display: block;
  text-decoration: none;
  color: inherit;
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--radius-md);
  padding: 20px;
  box-shadow: var(--card-shadow);
  transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
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

.card:hover::after {
  opacity: 1;
}

.card--narrow {
  text-align: center;
}

.card-label {
  display: block;
  font-weight: 700;
  font-size: 1.02rem;
  color: var(--violet-deep);
  margin-bottom: 6px;
}

.card-action {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--muted);
}

.card:hover .card-action {
  color: var(--accent);
}

.card-action .arrow {
  transition: transform 0.22s ease;
}

.card:hover .card-action .arrow {
  transform: translateX(3px);
}

.card--new {
  border-color: var(--accent-2);
}

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
  .page-title {
    font-size: 2rem;
  }
}

</style>

<p class="page-title">Backend Development</p>

<p class="page-subtitle">
  Lab experiments, lecture notes, and resources for the Backend Development course.
</p>

## Lab Experiments

<div class="card-grid card-grid--wide">

<a class="card" href="Lab/Exp%201/index.html">

  <span class="card-label">Experiment 1</span>

  <span class="card-action">
    Open <span class="arrow">→</span>
  </span>

</a>

<a class="card" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012">

  <span class="card-label">Experiment 12</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012B">

  <span class="card-label">Experiment 12B</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A">

  <span class="card-label">Experiment 13A</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

</div>

## Assignments

<div class="card-grid card-grid--wide">

<a class="card" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Assignments/Assignment_1">

  <span class="card-label">Assignment 1</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/index.html">

  <span class="card-label">Assignment 1 Preview</span>

  <span class="card-action">
    Preview <span class="arrow">→</span>
  </span>

</a>

<a class="card" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Assignments/Assignment_2">

  <span class="card-label">Assignment 2</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_2/Assignment%202%20PostgreSQL%20as%20SQL%20%2B%20NoSQL%20Working%20with%20JSONB.md">

  <span class="card-label">Assignment 2 Preview</span>

  <span class="card-action">
    Preview <span class="arrow">→</span>
  </span>

</a>

</div>

## Theory

<p class="subsection-title">Unit 1</p>

<div class="card-grid card-grid--narrow">

<a class="card card--narrow" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture3">

  <span class="card-label">Lecture 3</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card card--narrow" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4">

  <span class="card-label">Lecture 4</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card card--narrow" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5">

  <span class="card-label">Lecture 5</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card card--narrow" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6">

  <span class="card-label">Lecture 6</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card card--narrow" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture7">

  <span class="card-label">Lecture 7</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

<a class="card card--narrow" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8">

  <span class="card-label">Lecture 8</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

</div>

<p class="subsection-title">Unit 2</p>

<div class="card-grid card-grid--narrow">

<a class="card card--narrow card--new" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture13">

  <span class="card-label">Lecture 13</span>

  <span class="card-action">
    GitHub <span class="arrow">→</span>
  </span>

</a>

</div>