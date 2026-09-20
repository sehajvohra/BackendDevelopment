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
  margin-bottom: 12px;
}

.card-links {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.card-link {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--muted);
  text-decoration: none;
  position: relative;
  z-index: 2;
}

.card-link:hover {
  color: var(--accent);
}

.card-link .arrow {
  transition: transform 0.22s ease;
}

.card-link:hover .arrow {
  transform: translateX(3px);
}

.card-divider {
  color: var(--card-border);
  font-size: 0.9rem;
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

  .card-links {
    gap: 8px;
  }

}

</style>

<p class="page-title">Backend Development</p>

<p class="page-subtitle">
  Lab experiments, lecture notes, and resources for the Backend Development course.
</p>


## Lab Experiments

<div class="card-grid card-grid--wide">

<!-- Experiment 1 -->

<div class="card">

  <span class="card-label">Experiment 1</span>

  <div class="card-links">

    <a class="card-link" href="Lab/Exp%201/index.html">
      Open <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%201/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Experiment 12 -->

<div class="card">

  <span class="card-label">Experiment 12</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Experiment 12B -->

<div class="card">

  <span class="card-label">Experiment 12B</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012B">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012B/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Experiment 13A -->

<div class="card">

  <span class="card-label">Experiment 13A</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>

</div>


## Assignments

<div class="card-grid card-grid--wide">

<!-- Assignment 1 -->

<div class="card">

  <span class="card-label">Assignment 1</span>

  <div class="card-links">

    <a class="card-link" href="Theory/Assignments/Assignment_1/index.html">
      Open <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Assignment 2 -->

<div class="card">

  <span class="card-label">Assignment 2</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Assignments/Assignment_2">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_2/Assignment%202%20PostgreSQL%20as%20SQL%20%2B%20NoSQL%20Working%20with%20JSONB.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>

</div>


## Theory

<p class="subsection-title">Unit 1</p>

<div class="card-grid card-grid--narrow">

<!-- Lecture 3 -->

<div class="card card--narrow">

  <span class="card-label">Lecture 3</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture3">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture3/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Lecture 4 -->

<div class="card card--narrow">

  <span class="card-label">Lecture 4</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Lecture 5 -->

<div class="card card--narrow">

  <span class="card-label">Lecture 5</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture5/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Lecture 6 -->

<div class="card card--narrow">

  <span class="card-label">Lecture 6</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture6/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Lecture 7 -->

<div class="card card--narrow">

  <span class="card-label">Lecture 7</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture7">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>


<!-- Lecture 8 -->

<div class="card card--narrow">

  <span class="card-label">Lecture 8</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>

</div>


<p class="subsection-title">Unit 2</p>

<div class="card-grid card-grid--narrow">

<!-- Lecture 13 -->

<div class="card card--narrow card--new">

  <span class="card-label">Lecture 13</span>

  <div class="card-links">

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture13">
      GitHub <span class="arrow">→</span>
    </a>

    <span class="card-divider">|</span>

    <a class="card-link" href="https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture13/Report.md">
      Report <span class="arrow">→</span>
    </a>

  </div>

</div>

</div>