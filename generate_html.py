# Python generator to create index.html cleanly
import base64

with open('dielectric-lab/fig3_b64.txt', 'r', encoding='utf-8') as f:
    fig3_b64 = f.read().strip()

parts = []

parts.append('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dielectric Materials & Polarization Laboratory</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- KaTeX for crisp LaTeX formulas -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <!-- Three.js and OrbitControls for 3D Crystal / Molecular Lattice Visualizer -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>

  <style>
    html {
      scroll-behavior: smooth;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: #0f172a;
      color: #f8fafc;
    }
    .glass-card {
      background: rgba(30, 41, 59, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .glass-card-subtle {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.08);
    }
    .speech-box {
      background: rgba(15, 23, 42, 0.7);
      border-left: 4px solid #38bdf8;
      border-radius: 0 0.75rem 0.75rem 0;
    }
    input[type=range] {
      accent-color: #38bdf8;
    }
    .canvas-container {
      position: relative;
      background: radial-gradient(circle at center, #1e293b 0%, #0b1120 100%);
      border-radius: 0.75rem;
      overflow: hidden;
      border: 1px solid rgba(56, 189, 248, 0.2);
    }
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #0f172a;
    }
    ::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #475569;
    }
  </style>
</head>
<body class="min-h-screen text-slate-100 flex flex-col selection:bg-cyan-500 selection:text-white">

  <!-- TOP NAVIGATION BAR -->
  <header class="sticky top-0 z-50 glass-card border-b border-slate-700/60 shadow-xl">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-lg bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/30">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
          </svg>
        </div>
        <div>
          <span class="font-bold text-lg text-white tracking-wide">Dielectric Materials & Polarization</span>
          <span class="hidden md:inline-block text-xs text-cyan-400 ml-2 px-2 py-0.5 rounded-full bg-cyan-950/80 border border-cyan-800">Interactive Physical Laboratory</span>
        </div>
      </div>
      <nav class="hidden lg:flex items-center space-x-1 text-sm font-medium text-slate-300">
        <a href="#section-1" class="px-3 py-1.5 rounded-md hover:text-white hover:bg-slate-800 transition">1. Vacuum Model</a>
        <a href="#section-2" class="px-3 py-1.5 rounded-md hover:text-white hover:bg-slate-800 transition">2. Dielectric Insertion</a>
        <a href="#section-3" class="px-3 py-1.5 rounded-md hover:text-white hover:bg-slate-800 transition">3. Linear Materials & Lattices</a>
        <a href="#section-4" class="px-3 py-1.5 rounded-md hover:text-white hover:bg-slate-800 transition text-amber-400 hover:text-amber-300">4. Nonlinear BaTiO₃ (PRB Fig. 3)</a>
        <a href="#references" class="px-3 py-1.5 rounded-md hover:text-white hover:bg-slate-800 transition">References</a>
      </nav>
      <div class="flex items-center space-x-2">
        <a href="#section-3" class="text-xs bg-cyan-600 hover:bg-cyan-500 text-white font-semibold px-3 py-1.5 rounded-lg transition shadow-md shadow-cyan-600/30">
          Material Explorer
        </a>
      </div>
    </div>
  </header>

  <!-- MAIN CONTAINER -->
  <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-16">

    <!-- HERO / TITLE SECTION -->
    <section class="glass-card rounded-2xl p-6 sm:p-10 shadow-2xl relative overflow-hidden">
      <div class="absolute -top-24 -right-24 w-96 h-96 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-24 -left-24 w-96 h-96 bg-blue-600/10 rounded-full blur-3xl pointer-events-none"></div>

      <div class="relative z-10 max-w-4xl">
        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-semibold mb-4">
          <span>Fundamental Principles of Electrostatics & Materials Science</span>
        </div>
        <h1 class="text-3xl sm:text-5xl font-extrabold text-white tracking-tight leading-tight">
          Dielectric Materials Store Electrical Energy Through Polarization
        </h1>
        <p class="mt-4 text-base sm:text-lg text-slate-300 leading-relaxed">
          Show how dielectric constant (\\(\\varepsilon_r\\)) and layer thickness (\\(d\\)) affect capacitance, stored charge, and energy storage capacity. Follow the scientific walkthrough below from ideal vacuum geometry to microscopic dipole polarization, linear crystallographic structures, and ferroelectric field-dependent nonlinearity.
        </p>
      </div>
    </section>

    <!-- SECTION 1: VACUUM CAPACITOR -->
    <section id="section-1" class="glass-card rounded-2xl p-6 sm:p-8 shadow-xl border border-slate-700/70 space-y-6">
      
      <div class="border-b border-slate-700/60 pb-3">
        <span class="text-xs font-bold uppercase tracking-widest text-cyan-400">Part 1</span>
        <h2 class="text-2xl font-bold text-white mt-1">Capacitance in a Two-Parallel Plate Model (Vacuum Baseline)</h2>
      </div>

      <!-- Explanatory Script from PDF -->
      <div class="speech-box p-5 space-y-3 text-slate-200 text-sm sm:text-base leading-relaxed">
        <div class="flex items-center space-x-2 text-cyan-400 font-semibold text-xs uppercase tracking-wider mb-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
          <span>Physical Concept & Derivation</span>
        </div>
        <p>
          Capacitor is a kind of electric component, which can be used to store the electric energy in the electric field <a href="#ref-1" class="text-cyan-400 font-semibold hover:underline">[1]</a>. A common capacitor is made of two opposite charged conductors, for example: a two parallel-plate model. The physical quantity for the capacitors is called <strong>Capacitance</strong>.
        </p>
        <p>
          Capacitance is a purely geometrical quantity <a href="#ref-2" class="text-cyan-400 font-semibold hover:underline">[2]</a>. It only depends on the size, shape and separation of physical distance for the two opposite charge conductors. Such electric component, we call it &ndash; capacitor. Capacitance in a two-parallel plate model can be described by:
        </p>
        <p class="text-slate-300">
          The model is composed of two equal area plates with opposite charge to each other, separated by distance \\(d\\). The gap between the two plates now can be considered to be filled with vacuum / air (or nothing). The unit is Farad (F):
        </p>
        <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-700/80 font-mono text-center text-cyan-300 text-lg font-bold">
          \\[C = \\frac{\\epsilon_0 A}{d} = \\frac{Q}{V}\\]
        </div>
        <p>
          And the electric energy stored in the field is <a href="#ref-2" class="text-cyan-400 font-semibold hover:underline">[2]</a>:
        </p>
        <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-700/80 font-mono text-center text-amber-300 text-sm sm:text-base font-semibold">
          \\[dW = \\left(\\frac{q}{C}\\right) dq \\implies W = \\int_0^Q \\left(\\frac{q}{C}\\right) dq = \\frac{1}{2}\\left(\\frac{Q^2}{C}\\right) = \\frac{1}{2} C V^2\\]
        </div>
      </div>

      <!-- [互動圖片-1] -->
      <div class="pt-2">
        <div class="flex items-center space-x-2 mb-4">
          <span class="px-2.5 py-1 rounded bg-cyan-950 border border-cyan-800 text-cyan-300 text-xs font-mono font-bold">[Interaction Picture 1]</span>
          <h3 class="text-lg font-bold text-white">Vacuum Parallel-Plate Simulator</h3>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-7 flex flex-col space-y-2">
            <div class="canvas-container h-[400px] w-full flex items-center justify-center shadow-inner relative">
              <canvas id="canvas-module1" class="w-full h-full block"></canvas>
              <div class="absolute top-3 left-3 bg-slate-900/85 backdrop-blur px-2.5 py-1 rounded text-xs border border-slate-700 text-slate-300">
                <span class="inline-block w-2 h-2 rounded-full bg-cyan-400 animate-pulse mr-1.5"></span> Medium: <strong class="text-white">Vacuum (\\(\\varepsilon_r = 1.0000\\))</strong>
              </div>
            </div>
            <p class="text-xs text-slate-400 italic">
              * Charges \\(+Q\\) and \\(-Q\\) accumulate on electrodes as voltage \\(V\\) increases or gap thickness \\(d\\) decreases.
            </p>
          </div>

          <div class="lg:col-span-5 flex flex-col space-y-5 bg-slate-900/60 p-6 rounded-xl border border-slate-800">
            <div class="p-3 bg-slate-800/80 rounded-lg border border-slate-700 flex justify-between items-center text-sm">
              <span class="text-slate-400 font-medium">Electric Field Relation:</span>
              <span class="text-cyan-400 font-bold font-mono text-base">\\(E_{field} = \\frac{V}{d}\\)</span>
            </div>

            <div class="space-y-4">
              <div>
                <div class="flex justify-between items-center text-sm font-medium mb-1">
                  <label for="m1-v" class="text-slate-300">Voltage (\\(V\\)):</label>
                  <span id="m1-v-val" class="font-mono text-cyan-400 font-bold">50.0 V</span>
                </div>
                <input type="range" id="m1-v" min="0" max="200" step="1" value="50" class="w-full h-2 bg-slate-700 rounded-lg cursor-pointer">
              </div>

              <div>
                <div class="flex justify-between items-center text-sm font-medium mb-1">
                  <label for="m1-d" class="text-slate-300">Distance / Gap (\\(d\\)):</label>
                  <span id="m1-d-val" class="font-mono text-amber-400 font-bold">1.00 mm</span>
                </div>
                <input type="range" id="m1-d" min="0.2" max="5.0" step="0.1" value="1.0" class="w-full h-2 bg-slate-700 rounded-lg cursor-pointer">
              </div>

              <div>
                <div class="flex justify-between items-center text-sm font-medium mb-1">
                  <label for="m1-a" class="text-slate-300">Plate Area (\\(A\\)):</label>
                  <span id="m1-a-val" class="font-mono text-emerald-400 font-bold">25.0 cm²</span>
                </div>
                <input type="range" id="m1-a" min="5" max="100" step="1" value="25" class="w-full h-2 bg-slate-700 rounded-lg cursor-pointer">
              </div>
            </div>

            <div class="border-t border-slate-800 pt-4 space-y-2.5">
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400">Output Parameters:</h4>
              
              <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/70 border border-slate-700/60">
                <span class="font-bold text-sky-400 font-mono text-base">E =</span>
                <span id="m1-res-e" class="font-mono text-base font-bold text-sky-300">50.00 kV/m</span>
              </div>

              <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/70 border border-slate-700/60">
                <span class="font-bold text-cyan-400 font-mono text-base">C =</span>
                <span id="m1-res-c" class="font-mono text-base font-bold text-cyan-300">22.14 pF</span>
              </div>

              <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/70 border border-slate-700/60">
                <span class="font-bold text-emerald-400 font-mono text-base">Q =</span>
                <span id="m1-res-q" class="font-mono text-base font-bold text-emerald-300">1.107 nC</span>
              </div>

              <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/70 border border-slate-700/60">
                <span class="font-bold text-amber-400 font-mono text-base">Stored Energy W =</span>
                <span id="m1-res-u" class="font-mono text-base font-bold text-amber-300">27.67 nJ</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: DIELECTRIC INSERTION -->
    <section id="section-2" class="glass-card rounded-2xl p-6 sm:p-8 shadow-xl border border-slate-700/70 space-y-6">
      
      <div class="border-b border-slate-700/60 pb-3">
        <span class="text-xs font-bold uppercase tracking-widest text-emerald-400">Part 2</span>
        <h2 class="text-2xl font-bold text-white mt-1">Dielectric Material Insertion & Polarization Mechanism</h2>
      </div>

      <!-- Explanatory Script from PDF -->
      <div class="speech-box p-5 space-y-3 text-slate-200 text-sm sm:text-base leading-relaxed border-emerald-500">
        <div class="flex items-center space-x-2 text-emerald-400 font-semibold text-xs uppercase tracking-wider mb-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
          <span>Physical Concept & Derivation</span>
        </div>
        <p>
          However, if we fill the gap with different material instead of air, which will alter the physical state of origin capacitor. Such material is called <strong>dielectric</strong>. The material of dielectric is insulator, so the two conductor plates will not touch each other.
        </p>
        <p>
          On the other hand, the insulator dielectric will be polarized, producing an electric field antiparallel to the charge field \\(E\\):
        </p>
        <div class="p-2.5 bg-slate-900/80 rounded-lg border border-slate-700/80 font-mono text-center text-emerald-300 font-semibold">
          \\[E_{pol} = -\\frac{P}{\\epsilon_0}\\]
        </div>
        <p>
          The polarization is governed by the original field \\(E\\) and the property of dielectric material (\\(\\chi_e\\): electric susceptibility):
        </p>
        <div class="p-2.5 bg-slate-900/80 rounded-lg border border-slate-700/80 font-mono text-center text-emerald-300 font-semibold">
          \\[P = \\epsilon_0 \\chi_e E\\]
        </div>
        <p>
          The voltage between two plates is fixed. To keep the electric field \\(E\\) static, the amount of bounded charge at two plates will increase:
        </p>
        <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-700/80 font-mono text-center text-slate-300 text-sm sm:text-base">
          \\[\\frac{V}{d} = E_{total} = E_{plate} + E_{pol} \\implies \\frac{V}{d} = E_0 = E_{plate} - \\chi_e E_0\\]
        </div>
        <p>
          Now we can calculate the total bounded charge on the two plates:
        </p>
        <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-700/80 font-mono text-center text-emerald-300 text-base font-bold">
          \\[\\epsilon_0 E_{plate} = (1 + \\chi_e)\\epsilon_0 E_0 = \\epsilon_0 \\epsilon_r E_0\\]
        </div>
        <p>
          Where \\(\\epsilon_r = (1 + \\chi_e)\\) is the topic of our presentation: <strong>dielectric constant, or relative permittivity</strong>.
        </p>
        <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-700/80 font-mono text-center text-cyan-300 text-base font-bold">
          \\[Q_{total} = \\oint \\epsilon_0 \\epsilon_r E_0 \\cdot dA = \\epsilon_0 \\epsilon_r E_0 A = \\epsilon_0 \\epsilon_r \\frac{V}{d} A\\]
          \\[C = \\frac{Q_{total}}{V} = \\frac{\\epsilon_0 \\epsilon_r A}{d}\\]
        </div>
        <p class="text-slate-300">
          Adding dielectric material within the gap modifies the capacitance. Now we can visualize how dielectric change the behavior of capacitors, especially for the stored energy and bounded charge.
        </p>
      </div>

      <!-- [互動圖片 2] -->
      <div class="pt-2">
        <div class="flex items-center space-x-2 mb-4">
          <span class="px-2.5 py-1 rounded bg-emerald-950 border border-emerald-800 text-emerald-300 text-xs font-mono font-bold">[Interaction Picture 2]</span>
          <h3 class="text-lg font-bold text-white">Dielectric Medium Capacitor Simulator</h3>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-7 flex flex-col space-y-2">
            <div class="canvas-container h-[400px] w-full flex items-center justify-center shadow-inner relative">
              <canvas id="canvas-module2" class="w-full h-full block"></canvas>
              
              <div class="absolute top-3 left-3 bg-slate-900/85 backdrop-blur px-2.5 py-1 rounded text-xs border border-slate-700 text-slate-300">
                <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse mr-1.5"></span> Medium: <strong class="text-white">Dielectric Slab (\\(\\varepsilon_r > 1\\))</strong>
              </div>

              <div class="absolute top-3 right-3 bg-slate-900/90 backdrop-blur p-1 rounded-lg border border-slate-700 flex space-x-1 text-xs">
                <button id="m2-view-dipoles" class="px-2 py-1 rounded bg-emerald-600 text-white font-medium">Show Dipoles</button>
                <button id="m2-view-charges" class="px-2 py-1 rounded text-slate-300 hover:text-white">Bound Charges</button>
              </div>

              <div class="absolute bottom-3 left-3 bg-slate-900/80 backdrop-blur px-2.5 py-1 rounded text-xs text-slate-300 border border-slate-700">
                Capacitance Boost Factor: <span id="m2-gain-badge" class="text-emerald-400 font-bold font-mono">× 5.00</span>
              </div>
            </div>
            <p class="text-xs text-slate-400 italic">
              * Dipoles align with the electric field, generating surface bound charge \\(\\sigma_b = P\\). Free charge on electrodes is amplified by factor of \\(\\varepsilon_r\\).
            </p>
          </div>

          <div class="lg:col-span-5 flex flex-col space-y-5 bg-slate-900/60 p-6 rounded-xl border border-slate-800">
            <div class="p-3 bg-slate-800/80 rounded-lg border border-slate-700 flex justify-between items-center text-sm">
              <span class="text-slate-400 font-medium">Electric Field:</span>
              <span class="text-cyan-400 font-bold font-mono text-base">\\(E_{field} = \\frac{V}{d}\\)</span>
            </div>

            <div class="space-y-4">
              <div>
                <div class="flex justify-between items-center text-sm font-medium mb-1">
                  <label for="m2-v" class="text-slate-300">Voltage (\\(V\\)):</label>
                  <span id="m2-v-val" class="font-mono text-cyan-400 font-bold">50.0 V</span>
                </div>
                <input type="range" id="m2-v" min="0" max="200" step="1" value="50" class="w-full h-2 bg-slate-700 rounded-lg cursor-pointer">
              </div>

              <div>
                <div class="flex justify-between items-center text-sm font-medium mb-1">
                  <label for="m2-d" class="text-slate-300">Distance / Gap (\\(d\\)):</label>
                  <span id="m2-d-val" class="font-mono text-amber-400 font-bold">1.00 mm</span>
                </div>
                <input type="range" id="m2-d" min="0.2" max="5.0" step="0.1" value="1.0" class="w-full h-2 bg-slate-700 rounded-lg cursor-pointer">
              </div>

              <div>
                <div class="flex justify-between items-center text-sm font-medium mb-1">
                  <label for="m2-er" class="text-slate-300">Dielectric Constant (\\(\\varepsilon_r\\)):</label>
                  <span id="m2-er-val" class="font-mono text-purple-300 font-bold">5.00</span>
                </div>
                <input type="range" id="m2-er" min="1.0" max="25.0" step="0.1" value="5.0" class="w-full h-2 bg-slate-700 rounded-lg cursor-pointer">
                <div class="flex flex-wrap gap-1 mt-2">
                  <button type="button" class="preset-btn px-2 py-0.5 rounded text-[11px] bg-slate-800 hover:bg-slate-700 text-slate-300" data-er="1.0">Vacuum (1.0)</button>
                  <button type="button" class="preset-btn px-2 py-0.5 rounded text-[11px] bg-slate-800 hover:bg-slate-700 text-slate-300" data-er="2.1">PTFE (2.1)</button>
                  <button type="button" class="preset-btn px-2 py-0.5 rounded text-[11px] bg-slate-800 hover:bg-slate-700 text-slate-300" data-er="3.8">Silica (3.8)</button>
                  <button type="button" class="preset-btn px-2 py-0.5 rounded text-[11px] bg-slate-800 hover:bg-slate-700 text-slate-300" data-er="4.5">Quartz (4.5)</button>
                  <button type="button" class="preset-btn px-2 py-0.5 rounded text-[11px] bg-slate-800 hover:bg-slate-700 text-slate-300" data-er="9.5">Alumina (9.5)</button>
                </div>
              </div>
            </div>

            <div class="border-t border-slate-800 pt-4 space-y-2.5">
              <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400">Output Parameters:</h4>
              
              <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/70 border border-slate-700/60">
                <span class="font-bold text-sky-400 font-mono text-base">E =</span>
                <span id="m2-res-e" class="font-mono text-base font-bold text-sky-300">50.00 kV/m</span>
              </div>

              <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/70 border border-slate-700/60">
                <span class="font-bold text-cyan-400 font-mono text-base">C =</span>
                <span id="m2-res-c" class="font-mono text-base font-bold text-cyan-300">110.68 pF</span>
              </div>

              <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/70 border border-slate-700/60">
                <span class="font-bold text-emerald-400 font-mono text-base">Q =</span>
                <span id="m2-res-q" class="font-mono text-base font-bold text-emerald-300">5.534 nC</span>
              </div>

              <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/70 border border-slate-700/60">
                <span class="font-bold text-amber-400 font-mono text-base">Stored Energy W =</span>
                <span id="m2-res-u" class="font-mono text-base font-bold text-amber-300">138.35 nJ</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: COMMON LINEAR DIELECTRIC MATERIALS -->
    <section id="section-3" class="glass-card rounded-2xl p-6 sm:p-8 shadow-xl border border-slate-700/70 space-y-6">
      
      <div class="border-b border-slate-700/60 pb-3">
        <span class="text-xs font-bold uppercase tracking-widest text-purple-400">Part 3</span>
        <h2 class="text-2xl font-bold text-white mt-1">Common Linear Dielectric Materials & Crystallographic Structures</h2>
      </div>

      <!-- Explanatory Script from PDF -->
      <div class="speech-box p-5 space-y-3 text-slate-200 text-sm sm:text-base leading-relaxed border-purple-500">
        <div class="flex items-center space-x-2 text-purple-400 font-semibold text-xs uppercase tracking-wider mb-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
          <span>Physical Concept & Motivation</span>
        </div>
        <p>
          As a result, with dielectric, it would be easier for us to produce a high capacitance in smaller size. Then it is crucial for us to study how to manufacture a high dielectric constant material &ndash; the higher the electric constant is, the smaller a capacitor could be. We then can fill more electric components in the same physical volume.
        </p>
        <p class="font-medium text-slate-100">
          Let’s study some common materials used for making dielectric materials:
        </p>
      </div>

      <!-- [互動圖片三] -->
      <div class="pt-2">
        <div class="flex items-center space-x-2 mb-4">
          <span class="px-2.5 py-1 rounded bg-purple-950 border border-purple-800 text-purple-300 text-xs font-mono font-bold">[Interaction Picture 3]</span>
          <h3 class="text-lg font-bold text-white">Linear Material Selection, 3D Lattice Viewer & Implementation</h3>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-stretch mb-8">
          
          <!-- Column 1: Option Buttons for Linear Materials -->
          <div class="lg:col-span-3 flex flex-col bg-slate-900/60 p-4 rounded-xl border border-slate-800">
            <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-800">
              <span class="text-xs font-bold uppercase tracking-wider text-purple-400">Option Buttons</span>
              <span class="text-[10px] text-emerald-400 font-mono">Linear Dielectrics</span>
            </div>
            <p class="text-[11px] text-slate-400 mb-2">Select a linear dielectric material to view its crystal/molecular lattice and parameters:</p>
            <div id="material-buttons-grid" class="flex flex-col space-y-1.5 max-h-[380px] overflow-y-auto pr-1">
            </div>
          </div>

          <!-- Column 2: 3D Crystal / Molecular Structure Visualizer -->
          <div class="lg:col-span-5 flex flex-col">
            <div class="canvas-container h-[420px] w-full flex items-center justify-center shadow-inner relative" id="threejs-container">
              <div id="three-loading" class="absolute inset-0 flex items-center justify-center bg-slate-900/60 backdrop-blur z-20 text-slate-400 text-xs">
                Initializing 3D Unit Cell...
              </div>
              <div class="absolute top-3 left-3 bg-slate-900/85 backdrop-blur px-3 py-1.5 rounded-lg border border-slate-700 text-xs z-10">
                <span class="font-bold text-white" id="lattice-title">Alumina (α-Al₂O₃) Corundum</span>
                <span class="block text-[11px] text-slate-400" id="lattice-system">Trigonal (R3̄c)</span>
              </div>
              <div class="absolute top-3 right-3 bg-slate-900/85 backdrop-blur px-2 py-1 rounded-lg border border-slate-700 text-xs z-10 flex space-x-1.5">
                <button id="btn-toggle-rotate" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-[11px] text-cyan-300">Pause</button>
                <button id="btn-reset-cam" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded text-[11px] text-slate-300">Reset</button>
              </div>
              <div id="lattice-legend" class="absolute bottom-3 left-3 bg-slate-900/85 backdrop-blur px-3 py-1.5 rounded-lg border border-slate-700 text-[11px] text-slate-300 z-10 flex flex-wrap gap-2.5">
              </div>
            </div>
            <div class="flex items-center justify-between text-[11px] text-slate-400 px-1 mt-1.5">
              <span>💡 <em>Drag with mouse to rotate in 3D • Scroll wheel to zoom</em></span>
              <span id="lattice-formula" class="font-mono font-semibold text-cyan-400">α-Al₂O₃</span>
            </div>
          </div>

          <!-- Column 3: Material Parameter Readouts -->
          <div class="lg:col-span-4 flex flex-col justify-between bg-slate-900/60 p-5 rounded-xl border border-slate-800 space-y-3">
            <div>
              <div class="flex items-baseline justify-between border-b border-slate-800 pb-2 mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-slate-400">Material Parameters</span>
                <span id="mat-disp-type" class="text-[10px] px-2 py-0.5 rounded bg-purple-950 text-purple-300 border border-purple-800">Linear Ceramic</span>
              </div>

              <div class="space-y-2.5">
                <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/60 border border-slate-700/60">
                  <span class="text-xs text-slate-400 font-medium">Name:</span>
                  <span id="mat-card-name" class="font-mono text-sm font-bold text-white">Alumina (α-Al₂O₃)</span>
                </div>

                <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/60 border border-slate-700/60">
                  <div class="flex flex-col">
                    <span class="text-xs text-slate-400 font-medium">\\(\\chi_e\\):</span>
                    <span class="text-[10px] text-slate-500">Susceptibility</span>
                  </div>
                  <span id="mat-card-chi" class="font-mono text-base font-bold text-amber-300">8.50</span>
                </div>

                <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-800/60 border border-slate-700/60">
                  <div class="flex flex-col">
                    <span class="text-xs text-slate-400 font-medium">\\(\\varepsilon_r = (\\chi_e + 1)\\):</span>
                    <span class="text-[10px] text-slate-500">Dielectric Constant</span>
                  </div>
                  <span id="mat-card-er" class="font-mono text-lg font-bold text-cyan-300">9.50</span>
                </div>
              </div>

              <div class="mt-3 p-3 rounded-lg bg-slate-800/40 border border-slate-700/40 text-xs text-slate-300 space-y-1">
                <div class="font-semibold text-slate-200">Polarization Mechanism:</div>
                <p id="mat-desc-text" class="text-slate-400 leading-relaxed text-[11px]">
                  Ionic polarization: displacement of Al³⁺ cations within the hexagonal oxygen octahedron cages.
                </p>
              </div>
            </div>

            <div class="p-2.5 rounded-lg bg-slate-950/80 border border-slate-800 text-xs space-y-1">
              <div class="text-[10px] text-slate-400 uppercase font-semibold">Verified Literature Citation:</div>
              <a id="mat-ref-link" href="#" target="_blank" rel="noopener noreferrer" class="text-cyan-400 hover:text-cyan-300 font-medium inline-flex items-center space-x-1 group text-[11px]">
                <span id="mat-ref-text">NASA NEPP / MRS Paper</span>
                <svg class="w-3 h-3 group-hover:translate-x-0.5 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                </svg>
              </a>
              <div id="mat-ref-cond" class="text-[10px] text-slate-500 italic">96% Al₂O₃: ~9.5 at RT; single-crystal sapphire 9.0–9.8</div>
            </div>

          </div>
        </div>

        <!-- Bottom Row: Generated Capacitor Simulator for the selected material -->
        <div class="pt-6 border-t border-slate-700/60">
          <h4 class="text-sm font-bold uppercase tracking-wider text-slate-300 mb-4 flex items-center">
            <svg class="w-4 h-4 text-cyan-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2zM9 9h6v6H9V9z"/>
            </svg>
            Capacitor Implementation with Selected Material (<span id="m3-cap-matname" class="text-cyan-400">Alumina</span>)
          </h4>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <div class="lg:col-span-7 canvas-container h-[360px] w-full flex items-center justify-center relative">
              <canvas id="canvas-module3" class="w-full h-full block"></canvas>
              <div class="absolute bottom-3 right-3 bg-slate-900/80 px-2.5 py-1 rounded text-xs text-slate-300 border border-slate-700">
                Dielectric in Gap: <span id="m3-slab-label" class="text-white font-mono font-bold">Alumina (\\(\\varepsilon_r=9.50\\))</span>
              </div>
            </div>

            <div class="lg:col-span-5 flex flex-col space-y-4 bg-slate-900/60 p-6 rounded-xl border border-slate-800">
              <div class="p-3 bg-slate-800/80 rounded-lg border border-slate-700 flex justify-between items-center text-sm">
                <span class="text-slate-400 font-medium">Electric Field:</span>
                <span class="text-cyan-400 font-bold font-mono text-base">\\(E_{field} = \\frac{V}{d}\\)</span>
              </div>

              <div class="space-y-4">
                <div>
                  <div class="flex justify-between text-sm font-medium mb-1">
                    <label for="m3-v" class="text-slate-300">Voltage (\\(V\\)):</label>
                    <span id="m3-v-val" class="font-mono text-cyan-400 font-bold">50.0 V</span>
                  </div>
                  <input type="range" id="m3-v" min="0" max="200" step="1" value="50" class="w-full h-2 bg-slate-700 rounded-lg cursor-pointer">
                </div>

                <div>
                  <div class="flex justify-between text-sm font-medium mb-1">
                    <label for="m3-d" class="text-slate-300">Distance / Gap (\\(d\\)):</label>
                    <span id="m3-d-val" class="font-mono text-amber-400 font-bold">1.00 mm</span>
                  </div>
                  <input type="range" id="m3-d" min="0.2" max="5.0" step="0.1" value="1.0" class="w-full h-2 bg-slate-700 rounded-lg cursor-pointer">
                </div>
              </div>

              <div class="border-t border-slate-800 pt-3 space-y-2">
                <div class="flex items-center justify-between p-2 rounded bg-slate-800/60 border border-slate-700/60">
                  <span class="font-mono font-bold text-sky-400 text-sm">E =</span>
                  <span id="m3-res-e" class="font-mono text-sm font-bold text-sky-300">50.00 kV/m</span>
                </div>
                <div class="flex items-center justify-between p-2 rounded bg-slate-800/60 border border-slate-700/60">
                  <span class="font-mono font-bold text-cyan-400 text-sm">C =</span>
                  <span id="m3-res-c" class="font-mono text-sm font-bold text-cyan-300">210.29 pF</span>
                </div>
                <div class="flex items-center justify-between p-2 rounded bg-slate-800/60 border border-slate-700/60">
                  <span class="font-mono font-bold text-emerald-400 text-sm">Q =</span>
                  <span id="m3-res-q" class="font-mono text-sm font-bold text-emerald-300">10.514 nC</span>
                </div>
                <div class="flex items-center justify-between p-2 rounded bg-slate-800/60 border border-slate-700/60">
                  <span class="font-mono font-bold text-amber-400 text-sm">Stored Energy W =</span>
                  <span id="m3-res-u" class="font-mono text-sm font-bold text-amber-300">262.86 nJ</span>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: NONLINEAR FIELD-DEPENDENT PERMITTIVITY IN BaTiO3 (PRB FIGURE 3) -->
    <section id="section-4" class="glass-card rounded-2xl p-6 sm:p-8 shadow-xl border border-amber-500/30 space-y-8">
      
      <div class="border-b border-slate-700/60 pb-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-amber-400">Part 4 (Scientific Case Study)</span>
          <h2 class="text-2xl font-bold text-white mt-1">Field-Dependent Permittivity in Ferroelectric BaTiO₃: Modeling & Grain Size Verification</h2>
        </div>
        <a href="https://doi.org/10.1103/PhysRevB.85.224111" target="_blank" rel="noopener noreferrer" class="inline-flex items-center px-3 py-1.5 rounded-lg bg-amber-600/20 hover:bg-amber-600/30 text-amber-300 text-xs font-semibold border border-amber-500/40 transition">
          PRB 85, 224111 (2012)
          <svg class="w-3.5 h-3.5 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
        </a>
      </div>

      <!-- Explanatory Script from PDF -->
      <div class="speech-box p-5 space-y-3 text-slate-200 text-sm sm:text-base leading-relaxed border-amber-500">
        <div class="flex items-center space-x-2 text-amber-400 font-semibold text-xs uppercase tracking-wider mb-1">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
          <span>Nonlinear Polarization Theory</span>
        </div>
        <p>
          In the previous case, the value of dielectric constant is static. However, for some material, the polarization to field is not a simple linear relation but follows a higher-order power series:
        </p>
        <div class="p-3 bg-slate-900/80 rounded-lg border border-slate-700/80 font-mono text-center text-amber-300 text-sm sm:text-base font-bold">
          \\[P = \\epsilon_0 \\left(a_0 + a_1 \\chi_e^{(1)} E + a_2 \\chi_e^{(2)} E^2 + \\dots\\right)\\]
        </div>
        <p>
          The dielectric constant is a function of \\(E\\), \\(\\epsilon_r(E)\\). A typical case is \\(\\text{BaTiO}_3\\) <a href="#ref-3" class="text-amber-400 font-semibold hover:underline">[3]</a>. The picture below is referred to the article <a href="#ref-3" class="text-amber-400 font-semibold hover:underline">[3, 4]</a>, where we could find the non-linearity relation of \\(\\epsilon_r(E)\\) for different grain sizes:
        </p>
      </div>

      <!-- Paper Figure 3 Showcase -->
      <div class="bg-slate-900/80 p-6 rounded-2xl border border-slate-800 shadow-2xl space-y-4">
        
        <div class="flex items-center justify-between pb-3 border-b border-slate-800">
          <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Figure 3 from Publication</span>
            <h3 class="text-lg font-bold text-white">Permittivity vs. Applied Electric Field for BaTiO₃ Nanoceramics</h3>
          </div>
          <span class="text-xs px-2.5 py-1 rounded-md bg-amber-950/80 text-amber-300 border border-amber-800 font-mono">Phys. Rev. B 85, 224111 (2012)</span>
        </div>

        <div class="flex flex-col items-center justify-center p-4 bg-slate-950 rounded-xl border border-slate-800/80">
          <img 
            id="fig3-img"
            src="figure3_with_caption.png" 
''')

# Insert base64 fallback for the image
parts.append(f'''            onerror="this.onerror=null; this.src='data:image/png;base64,{fig3_b64}';"''')

parts.append('''
            alt="Figure 3: Permittivity vs field dependence of BaTiO3 ceramics with various GS in the range of 100-5000 nm. Inset: field dependence of the derivative dεr/dE." 
            class="max-w-full md:max-w-2xl h-auto rounded-lg shadow-lg border border-slate-800"
          />
          <div class="mt-3 text-xs text-slate-400 text-center max-w-2xl leading-relaxed">
            <strong class="text-slate-200">FIG. 3.</strong> Permittivity vs field dependence of \\(\\text{BaTiO}_3\\) ceramics with various grain sizes (GS) in the range of 100–5000 nm. <em>Inset:</em> field dependence of the numerical derivative \\(d\\varepsilon_r/dE\\). (Reprinted with permission from Padurariu et al., <em>Phys. Rev. B</em> <strong>85</strong>, 224111, &copy;2012 American Physical Society).
          </div>
        </div>

      </div>

      <!-- Comprehensive Scientific Explanation -->
      <div class="space-y-6 pt-2">
        <h3 class="text-xl font-bold text-white flex items-center">
          <span class="w-2.5 h-2.5 rounded-full bg-amber-400 mr-2.5"></span>
          Detailed Scientific Explanation: Why Does the Dielectric Constant Exhibit a Nonlinear Field-Dependence?
        </h3>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          
          <!-- Box 1 -->
          <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-3">
            <div class="text-amber-400 font-bold text-sm uppercase tracking-wide flex items-center">
              <span class="w-6 h-6 rounded-full bg-amber-500/20 text-amber-300 flex items-center justify-center font-bold mr-2 text-xs">1</span>
              Microscopic Ferroelectric Domain Switching & Polarization Saturation
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              In linear dielectrics (e.g. Quartz, Alumina), the induced polarization is solely due to tiny, harmonic elastic displacements of electron clouds and ions, yielding a constant \\(\\varepsilon_r\\).
            </p>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              In contrast, <strong>Barium Titanate (\\(\\text{BaTiO}_3\\))</strong> is a ferroelectric perovskite with permanent electric dipoles caused by the spontaneous off-center displacement of \\(\\text{Ti}^{4+}\\) ions.
            </p>
            <ul class="text-xs sm:text-sm text-slate-400 space-y-1.5 list-disc list-inside">
              <li><strong>At low electric fields (\\(E \\approx 0\\)):</strong> Ferroelectric domain walls move freely, and dipole orientations switch easily, resulting in an enormous relative permittivity (\\(\\varepsilon_r(0) \\sim 1000 - 5200\\)).</li>
              <li><strong>At high electric fields (\\(E > 20\\text{ kV/cm}\\)):</strong> Most ferroelectric domains become fully aligned along the external field vector. As the polarization approaches complete <strong>saturation</strong> (\\(P \\to P_s\\)), the differential polarizability \\(\\frac{dP}{dE}\\) drops dramatically.</li>
              <li>Since \\(\\varepsilon_r(E) = 1 + \\frac{1}{\\epsilon_0}\\frac{dP}{dE}\\), the permittivity decreases sharply under strong DC bias fields (termed <em>dielectric tunability</em> \\(n(E) = \\varepsilon_r(0)/\\varepsilon_r(E)\\)).</li>
            </ul>
          </div>

          <!-- Box 2 -->
          <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-3">
            <div class="text-amber-400 font-bold text-sm uppercase tracking-wide flex items-center">
              <span class="w-6 h-6 rounded-full bg-amber-500/20 text-amber-300 flex items-center justify-center font-bold mr-2 text-xs">2</span>
              Landau-Devonshire Theory & Johnson's Phenomenological Equation
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              From the thermodynamic Landau-Ginzburg-Devonshire free energy expansion, Johnson derived the classical analytical expression describing ferroelectric field-dependent permittivity:
            </p>
            <div class="p-3 bg-slate-950 rounded-lg border border-slate-800 font-mono text-center text-cyan-300 text-sm font-semibold">
              \\[\\varepsilon_r(E) = \\frac{\\varepsilon_r(0)}{\\left[1 + 3\\beta \\cdot \\varepsilon_r(0)^3 \\cdot \\epsilon_0^3 \\cdot E^2\\right]^{1/3}}\\]
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Where \\(\\beta\\) is the phenomenological coefficient of ferroelectric nonlinearity (\\(\\sim 10^{10}\\text{ V}\\cdot\\text{m}^5/\\text{C}^3\\)). For coarse ceramics (\\(GS = 5000\\text{ nm}\\)), Johnson's equation provides an excellent fit (correlation factor &gt;0.9999), predicting a 2.5× permittivity reduction at only \\(20\\text{ kV/cm}\\).
            </p>
          </div>

          <!-- Box 3 -->
          <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-3">
            <div class="text-amber-400 font-bold text-sm uppercase tracking-wide flex items-center">
              <span class="w-6 h-6 rounded-full bg-amber-500/20 text-amber-300 flex items-center justify-center font-bold mr-2 text-xs">3</span>
              Grain Size (GS) Dependence & Core-Shell Grain Boundary Model
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              As observed in <strong>Figure 3</strong>, reducing the ceramic grain size from \\(5000\\text{ nm}\\) down to \\(100\\text{ nm}\\) suppresses the zero-field permittivity below \\(1000\\) and drastically curtails tunability:
            </p>
            <ul class="text-xs sm:text-sm text-slate-400 space-y-1.5 list-disc list-inside">
              <li><strong>Coarse ceramics (\\(GS = 5000\\text{ nm}\\)):</strong> \\(\\varepsilon_r\\) drops from \\(\\sim 4700\\) down to \\(\\sim 1900\\) at \\(20\\text{ kV/cm}\\) (\\(2.5\\times\\) drop).</li>
              <li><strong>Ultrafine ceramics (\\(GS = 100\\text{ nm}\\)):</strong> \\(\\varepsilon_r\\) drops by <em>only ~5% below 40 kV/cm</em>, maintaining nearly constant permittivity!</li>
            </ul>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              <strong>Core-Shell Composite Structure:</strong> Dense nanostructured ceramics consist of ferroelectric grain cores (\\(\\varepsilon_{core}(0) \\approx 1000\\)) separated by non-ferroelectric grain boundary "dead layers" (\\(\\varepsilon_{boundary} \\approx 100\\)). When grain size decreases to \\(100\\text{ nm}\\), low-permittivity grain boundaries increase to ~18% of total volume, acting as a low-dielectric dilution buffer.
            </p>
          </div>

          <!-- Box 4 -->
          <div class="p-5 rounded-xl bg-slate-900/60 border border-slate-800 space-y-3">
            <div class="text-amber-400 font-bold text-sm uppercase tracking-wide flex items-center">
              <span class="w-6 h-6 rounded-full bg-amber-500/20 text-amber-300 flex items-center justify-center font-bold mr-2 text-xs">4</span>
              Local Field Inhomogeneity & Linearization of Permittivity Response
            </div>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
              Finite Element Method (FEM) and Monte Carlo Potts simulations in the paper revealed that applied electric field distributions inside nanoceramics are <strong>highly inhomogeneous</strong>:
            </p>
            <ul class="text-xs sm:text-sm text-slate-400 space-y-1.5 list-disc list-inside">
              <li><strong>Grain Boundary Hot Spots:</strong> The highest electric fields concentrate across grain boundaries perpendicular to the field direction, while local fields inside ferroelectric grain cores are heavily shielded.</li>
              <li><strong>Linearization Mechanism:</strong> Averaging the effective permittivity over this disordered local field distribution shifts the inflection point (minimum of \\(d\\varepsilon/dE\\)) toward much higher electric fields.</li>
              <li>As seen in the <em>Inset of Figure 3</em>, for \\(GS = 100\\text{ nm}\\), \\(d\\varepsilon_r/dE\\) is practically flat and constant (\\(\\sim -3\\text{ (kV/cm)}^{-1}\\)), resulting in a <strong>remarkable linear \\(\\varepsilon_r(E)\\) dependence</strong>.</li>
            </ul>
            <p class="text-xs sm:text-sm text-amber-300/90 font-medium leading-relaxed">
              <strong>Technological Significance:</strong> A linear permittivity-field response is highly sought after for high-power tunable microwave circuits and communication filters to eliminate nonlinear harmonic distortion!
            </p>
          </div>

        </div>
      </div>

    </section>

    <!-- SECTION 5: REFERENCES -->
    <section id="references" class="glass-card rounded-2xl p-6 sm:p-8 shadow-xl border border-slate-700/70 space-y-6">
      <div class="border-b border-slate-700/60 pb-3 flex items-center justify-between">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-slate-400">Literature Citations</span>
          <h2 class="text-2xl font-bold text-white mt-1">References & Authoritative Material Sources</h2>
        </div>
      </div>

      <div class="p-4 rounded-xl bg-slate-900/80 border border-slate-800 text-xs sm:text-sm space-y-2 text-slate-300">
        <div class="font-bold text-white uppercase tracking-wider text-xs mb-2">Core References:</div>
        <div id="ref-1"><strong>[1]</strong> Wikipedia, <em>Capacitor & Dielectric Materials</em>. <a href="https://en.wikipedia.org/wiki/Capacitor" target="_blank" rel="noopener noreferrer" class="text-cyan-400 hover:underline">https://en.wikipedia.org/wiki/Capacitor</a></div>
        <div id="ref-2"><strong>[2]</strong> David J. Griffiths, <em>Introduction to Electrodynamics</em>, 3rd edition, Prentice Hall, Chapter 2 (Electrostatics) & Chapter 4 (Electric Fields in Matter).</div>
        <div id="ref-3"><strong>[3, 4]</strong> L. Padurariu, L. Curecheriu, V. Buscaglia, and L. Mitoseriu, <em>"Field-dependent permittivity in nanostructured BaTiO₃ ceramics: Modeling and experimental verification,"</em> <strong>Physical Review B</strong>, vol. 85, no. 22, p. 224111, 2012. DOI: <a href="https://doi.org/10.1103/PhysRevB.85.224111" target="_blank" rel="noopener noreferrer" class="text-cyan-400 hover:underline">10.1103/PhysRevB.85.224111</a></div>
      </div>

      <div>
        <h4 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Linear Dielectrics Property Database & Literature Citations:</h4>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-sm border-collapse">
            <thead>
              <tr class="border-b border-slate-700 text-xs font-bold uppercase tracking-wider text-slate-400 bg-slate-900/60">
                <th class="py-3 px-4">Material</th>
                <th class="py-3 px-3 text-center">\\(\\varepsilon_r\\)</th>
                <th class="py-3 px-3 text-center">\\(\\chi_e\\)</th>
                <th class="py-3 px-4">Structure / Crystal System</th>
                <th class="py-3 px-4">Recommended Citation Source</th>
                <th class="py-3 px-4">Measurement Conditions / Notes</th>
              </tr>
            </thead>
            <tbody id="references-table-body" class="divide-y divide-slate-800 text-slate-300">
            </tbody>
          </table>
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="glass-card border-t border-slate-800 py-6 mt-16 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
      <div>Dielectric Physics & Polarization Interactive Laboratory • Created for Advanced Materials Science Education</div>
      <div class="text-slate-400 font-mono">Vacuum Permittivity \\(\\varepsilon_0 = 8.8541878128 \\times 10^{-12}\\text{ F/m}\\)</div>
    </div>
  </footer>

  <script>
    const EPS_0 = 8.8541878128e-12;

    const LINEAR_MATERIALS = [
      {
        id: "alumina",
        name: "Alumina (Sapphire)",
        formula: "α-Al₂O₃",
        er: 9.50,
        chi: 8.50,
        type: "Linear Oxide Ceramic",
        crystalSystem: "Trigonal Corundum (R3̄c)",
        mechanism: "Ionic polarization: Al³⁺ cation displacement inside oxygen octahedral cages.",
        sourceTitle: "NASA NEPP / MRS Paper",
        sourceCondition: "96% Al₂O₃: ~9.5 at RT; single crystal sapphire 9.0–9.8",
        url: "https://nepp.nasa.gov/docuploads/7cf49e5d-bb68-46d7-9dc6c13544a6747e/2004%20mrs%20fall%20paper%2088011%20g7.pdf"
      },
      {
        id: "si3n4",
        name: "Silicon Nitride",
        formula: "Si₃N₄",
        er: 7.50,
        chi: 6.50,
        type: "Linear Covalent Ceramic",
        crystalSystem: "Hexagonal (β-phase P6₃/m)",
        mechanism: "Ionic-covalent polarizability in rigid SiN₄ tetrahedral network.",
        sourceTitle: "CeramTec Industrial Substrates",
        sourceCondition: "7.8 at 1 MHz; substrate grade 7.5–7.8",
        url: "https://www.ceramtec-industrial.com/en/products-applications/substrates/si3n4-substrates"
      },
      {
        id: "mica",
        name: "Muscovite Mica",
        formula: "KAl₂(AlSi₃O₁₀)(OH)₂",
        er: 6.00,
        chi: 5.00,
        type: "Linear Layered Silicate",
        crystalSystem: "Monoclinic (C2/c) 2:1 Sheet",
        mechanism: "Ionic polarization in T-O-T aluminosilicate sheets with K⁺ interlayer cations.",
        sourceTitle: "S&R Optic Muscovite Mica Data",
        sourceCondition: "Typical dielectric constant ~6.0 across RF frequencies",
        url: "https://www.sr-optic.com/Materials/Mica/"
      },
      {
        id: "alpha_quartz",
        name: "α-Quartz",
        formula: "SiO₂ (crystalline)",
        er: 4.50,
        chi: 3.50,
        type: "Linear Piezoelectric Crystal",
        crystalSystem: "Trigonal (P3₁21)",
        mechanism: "Ionic displacement in helical chains of SiO₄ tetrahedra.",
        sourceTitle: "IEEE UFFC Review Paper",
        sourceCondition: "~4.5 perpendicular to Z-axis, ~4.6 parallel at RT",
        url: "https://ieee-uffc.org/frequency-control/educational-resources/review-papers/constants-alpha-quartz"
      },
      {
        id: "fused_silica",
        name: "Fused Silica",
        formula: "SiO₂ (amorphous)",
        er: 3.80,
        chi: 2.80,
        type: "Linear Inorganic Glass",
        crystalSystem: "Continuous Random Network",
        mechanism: "Ionic and electronic polarizability in corner-sharing tetrahedral glass network.",
        sourceTitle: "Dynasil Fused Silica Properties",
        sourceCondition: "3.826 from 100 Hz–10 MHz at 25°C, approx. 3.8",
        url: "https://www.dynasilfusedsilica.com/assets/Fused-Silica-Properties.pdf"
      },
      {
        id: "pet",
        name: "PET (Mylar)",
        formula: "-(C₁₀H₈O₄)-ₙ",
        er: 3.20,
        chi: 2.20,
        type: "Linear Polyester",
        crystalSystem: "Triclinic Semicrystalline",
        mechanism: "Dipolar orientation of ester groups (-COO-) and aromatic rings.",
        sourceTitle: "Röchling Sustadur PET Datasheet",
        sourceCondition: "3.2 at 1 MHz, ASTM D150 at 23°C",
        url: "https://www.roechling.com/us/industrial/materials/thermoplastics/engineering-plastics/pet/sustadur-pet-tf-astm-717917"
      },
      {
        id: "ps",
        name: "Polystyrene (PS)",
        formula: "-(CH₂-CH(C₆H₅))-ₙ",
        er: 2.60,
        chi: 1.60,
        type: "Linear Aromatic Polymer",
        crystalSystem: "Amorphous / Atactic",
        mechanism: "Delocalized π-electron cloud electronic polarizability in phenyl rings.",
        sourceTitle: "AZoM / RAPRA Data",
        sourceCondition: "2.6 at 1 kHz, Room Temperature",
        url: "https://www.azom.com/article.aspx?ArticleID=798"
      },
      {
        id: "pe",
        name: "Polyethylene (PE)",
        formula: "-(CH₂-CH₂)-ₙ",
        er: 2.30,
        chi: 1.30,
        type: "Linear Polyolefin",
        crystalSystem: "Orthorhombic Zigzag Chains",
        mechanism: "Electronic polarization of nonpolar C-C and C-H sigma bonds.",
        sourceTitle: "Goodfellow Material Data",
        sourceCondition: "LDPE 2.2–2.35 at 1 MHz; HDPE 2.3–2.4 at 1 MHz",
        url: "https://www.goodfellow.com/global/ldpe-powder-group"
      },
      {
        id: "pp",
        name: "Polypropylene (PP)",
        formula: "-(CH₂-CH(CH₃))-ₙ",
        er: 2.20,
        chi: 1.20,
        type: "Linear Thermoplastic",
        crystalSystem: "Isotactic Semicrystalline",
        mechanism: "Electronic polarization of saturated aliphatic polymer backbone.",
        sourceTitle: "WIMA Main Catalogue 2016",
        sourceCondition: "2.2 at 1 kHz, 23°C (capacitor film grade)",
        url: "https://www.wima.com.tw/pdf/WIMA_Main_Catalogue_2016.pdf"
      },
      {
        id: "ptfe",
        name: "PTFE (Teflon)",
        formula: "-(CF₂-CF₂)-ₙ",
        er: 2.10,
        chi: 1.10,
        type: "Linear Fluoropolymer",
        crystalSystem: "Semicrystalline Helical",
        mechanism: "Electronic polarization along dense fluorine helical sheath.",
        sourceTitle: "ASTM D150 / Eagle Plastics",
        sourceCondition: "2.1 at 1 MHz; Room Temp (literature 2.0–2.2)",
        url: "https://eagle-plastics.com/materials/ptfe/"
      },
      {
        id: "air",
        name: "Air",
        formula: "N₂ (78%), O₂ (21%)",
        er: 1.0006,
        chi: 0.0006,
        type: "Linear Gas Mixture",
        crystalSystem: "Gaseous State",
        mechanism: "Weak electronic and rotational polarization of gas molecules.",
        sourceTitle: "NIST Technical Note 1294",
        sourceCondition: "Standard laboratory conditions (approx. 1.0006 at 20°C, 101.325 kPa)",
        url: "https://nvlpubs.nist.gov/nistpubs/Legacy/TN/nbstechnicalnote1294.pdf"
      },
      {
        id: "vacuum",
        name: "Vacuum",
        formula: "Empty Space",
        er: 1.0000,
        chi: 0.0000,
        type: "Free Space",
        crystalSystem: "Free Space Void",
        mechanism: "No physical matter present; zero polarization (P = 0).",
        sourceTitle: "SI Definition",
        sourceCondition: "ε_r ≡ ε / ε_0 = 1 for vacuum by fundamental SI definition",
        url: "https://physics.nist.gov/cuu/Units/index.html"
      }
    ];

    let currentSelectedMaterial = LINEAR_MATERIALS[0];

    // Three.js Setup
    let threeScene, threeCamera, threeRenderer, threeControls, structureGroup;
    let isAutoRotating = true;

    function initThreeJS() {
      const container = document.getElementById("threejs-container");
      const width = container.clientWidth || 500;
      const height = container.clientHeight || 420;

      threeScene = new THREE.Scene();
      threeCamera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
      threeCamera.position.set(3.5, 2.8, 4.5);

      threeRenderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
      threeRenderer.setSize(width, height);
      threeRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      container.appendChild(threeRenderer.domElement);

      threeControls = new THREE.OrbitControls(threeCamera, threeRenderer.domElement);
      threeControls.enableDamping = true;
      threeControls.dampingFactor = 0.05;
      threeControls.autoRotate = true;
      threeControls.autoRotateSpeed = 1.2;

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.75);
      threeScene.add(ambientLight);

      const dirLight1 = new THREE.DirectionalLight(0xffffff, 0.9);
      dirLight1.position.set(10, 15, 10);
      threeScene.add(dirLight1);

      const dirLight2 = new THREE.DirectionalLight(0x38bdf8, 0.4);
      dirLight2.position.set(-10, -5, -10);
      threeScene.add(dirLight2);

      structureGroup = new THREE.Group();
      threeScene.add(structureGroup);

      window.addEventListener("resize", () => {
        if (!container || !threeCamera || !threeRenderer) return;
        const w = container.clientWidth;
        const h = container.clientHeight;
        threeCamera.aspect = w / h;
        threeCamera.updateProjectionMatrix();
        threeRenderer.setSize(w, h);
      });

      document.getElementById("btn-toggle-rotate").addEventListener("click", function() {
        isAutoRotating = !isAutoRotating;
        threeControls.autoRotate = isAutoRotating;
        this.textContent = isAutoRotating ? "Pause" : "Resume";
      });

      document.getElementById("btn-reset-cam").addEventListener("click", () => {
        threeCamera.position.set(3.5, 2.8, 4.5);
        threeControls.target.set(0, 0, 0);
        threeControls.update();
      });

      document.getElementById("three-loading").style.display = "none";

      animateThree();
      buildCrystalModel(currentSelectedMaterial);
    }

    function animateThree() {
      requestAnimationFrame(animateThree);
      threeControls.update();
      threeRenderer.render(threeScene, threeCamera);
    }

    function clearStructure() {
      while (structureGroup.children.length > 0) {
        const obj = structureGroup.children[0];
        if (obj.geometry) obj.geometry.dispose();
        if (obj.material) {
          if (Array.isArray(obj.material)) obj.material.forEach(m => m.dispose());
          else obj.material.dispose();
        }
        structureGroup.remove(obj);
      }
    }

    function createAtomSphere(x, y, z, radius, colorHex) {
      const geom = new THREE.SphereGeometry(radius, 24, 24);
      const mat = new THREE.MeshStandardMaterial({ color: colorHex, roughness: 0.25, metalness: 0.15 });
      const mesh = new THREE.Mesh(geom, mat);
      mesh.position.set(x, y, z);
      structureGroup.add(mesh);
      return mesh;
    }

    function createBond(p1, p2, radius = 0.04, colorHex = 0x94a3b8) {
      const v1 = new THREE.Vector3(p1.x, p1.y, p1.z);
      const v2 = new THREE.Vector3(p2.x, p2.y, p2.z);
      const distance = v1.distanceTo(v2);
      const geom = new THREE.CylinderGeometry(radius, radius, distance, 12);
      const mat = new THREE.MeshStandardMaterial({ color: colorHex, roughness: 0.4 });
      const mesh = new THREE.Mesh(geom, mat);
      const mid = v1.clone().add(v2).multiplyScalar(0.5);
      mesh.position.copy(mid);
      mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), v2.clone().sub(v1).normalize());
      structureGroup.add(mesh);
      return mesh;
    }

    function addUnitCellBox(sx, sy, sz, colorHex = 0x38bdf8) {
      const geom = new THREE.BoxGeometry(sx, sy, sz);
      const wireframe = new THREE.WireframeGeometry(geom);
      const line = new THREE.LineSegments(wireframe);
      line.material.color.setHex(colorHex);
      line.material.opacity = 0.45;
      line.material.transparent = true;
      structureGroup.add(line);
    }

    function buildCrystalModel(mat) {
      clearStructure();
      const legend = document.getElementById("lattice-legend");
      legend.innerHTML = "";

      const addLegendItem = (name, colorHex) => {
        const item = document.createElement("div");
        item.className = "flex items-center space-x-1";
        const dot = document.createElement("span");
        dot.className = "inline-block w-3 h-3 rounded-full border border-slate-600";
        dot.style.backgroundColor = "#" + colorHex.toString(16).padStart(6, "0");
        const lbl = document.createElement("span");
        lbl.textContent = name;
        item.appendChild(dot);
        item.appendChild(lbl);
        legend.appendChild(item);
      };

      if (mat.id === "alumina") {
        addUnitCellBox(2.2, 3.0, 2.2, 0xa855f7);
        const alColor = 0x8b5cf6;
        const oColor = 0xef4444;
        addLegendItem("Al³⁺ (Alumina)", alColor);
        addLegendItem("O²⁻ (Oxygen)", oColor);

        const oPoints = [
          {x: -0.7, y: -0.8, z: -0.5}, {x: 0.7, y: -0.8, z: -0.5}, {x: 0, y: -0.8, z: 0.8},
          {x: -0.7, y: 0.8, z: 0.5}, {x: 0.7, y: 0.8, z: 0.5}, {x: 0, y: 0.8, z: -0.8}
        ];
        oPoints.forEach(p => createAtomSphere(p.x, p.y, p.z, 0.22, oColor));

        const alPoints = [{x: 0, y: -0.4, z: 0}, {x: 0, y: 0.4, z: 0}];
        alPoints.forEach(p => {
          createAtomSphere(p.x, p.y, p.z, 0.18, alColor);
          oPoints.forEach(op => {
            const d = Math.hypot(p.x - op.x, p.y - op.y, p.z - op.z);
            if (d < 1.3) createBond(p, op, 0.035, 0xc4b5fd);
          });
        });

      } else if (mat.id === "si3n4") {
        addUnitCellBox(2.4, 2.0, 2.4, 0x14b8a6);
        const siColor = 0x0d9488;
        const nColor = 0x3b82f6;
        addLegendItem("Si (Silicon)", siColor);
        addLegendItem("N (Nitrogen)", nColor);

        const siPos = [
          {x: 0, y: 0, z: 0}, {x: 0.8, y: 0.4, z: 0.5}, {x: -0.8, y: -0.4, z: -0.5},
          {x: -0.6, y: 0.5, z: 0.6}, {x: 0.6, y: -0.5, z: -0.6}
        ];
        const nPos = [
          {x: 0.4, y: 0.2, z: 0.2}, {x: -0.4, y: -0.2, z: -0.2},
          {x: -0.3, y: 0.3, z: 0.3}, {x: 0.3, y: -0.3, z: -0.3}
        ];
        siPos.forEach(p => createAtomSphere(p.x, p.y, p.z, 0.2, siColor));
        nPos.forEach(p => createAtomSphere(p.x, p.y, p.z, 0.18, nColor));

        siPos.forEach(sp => {
          nPos.forEach(np => {
            const d = Math.hypot(sp.x - np.x, sp.y - np.y, sp.z - np.z);
            if (d < 0.95) createBond(sp, np, 0.035, 0x5eead4);
          });
        });

      } else if (mat.id === "alpha_quartz") {
        addUnitCellBox(2.2, 2.5, 2.2, 0x06b6d4);
        const siColor = 0x0ea5e9;
        const oColor = 0xef4444;
        addLegendItem("Si (Trigonal Core)", siColor);
        addLegendItem("O (Helical Bridges)", oColor);

        const steps = 7;
        const siList = [];
        for (let i = 0; i < steps; i++) {
          const t = i / (steps - 1);
          const angle = t * Math.PI * 2.2;
          const r = 0.7;
          const x = Math.cos(angle) * r;
          const z = Math.sin(angle) * r;
          const y = (t - 0.5) * 2.0;
          createAtomSphere(x, y, z, 0.2, siColor);
          siList.push({x, y, z});
        }
        for (let i = 0; i < siList.length - 1; i++) {
          const mid = {
            x: (siList[i].x + siList[i+1].x)/2 + 0.1,
            y: (siList[i].y + siList[i+1].y)/2,
            z: (siList[i].z + siList[i+1].z)/2 + 0.1
          };
          createAtomSphere(mid.x, mid.y, mid.z, 0.16, oColor);
          createBond(siList[i], mid, 0.04, 0x93c5fd);
          createBond(mid, siList[i+1], 0.04, 0x93c5fd);
        }

      } else if (mat.id === "fused_silica") {
        const siColor = 0x0ea5e9;
        const oColor = 0xef4444;
        addLegendItem("Si (Amorphous)", siColor);
        addLegendItem("O (Random Network)", oColor);

        const nodes = [
          {x: -0.9, y: 0.5, z: -0.4}, {x: 0.1, y: 0.8, z: 0.3},
          {x: -0.3, y: -0.6, z: -0.2}, {x: 0.8, y: -0.3, z: -0.5},
          {x: 0.7, y: 0.4, z: 0.8}, {x: -0.8, y: -0.4, z: 0.7}
        ];
        nodes.forEach(n => createAtomSphere(n.x, n.y, n.z, 0.2, siColor));
        const bonds = [[0,1], [0,2], [1,3], [2,3], [1,4], [2,5]];
        bonds.forEach(([i, j]) => {
          const p1 = nodes[i];
          const p2 = nodes[j];
          const ox = (p1.x + p2.x)/2 + 0.12;
          const oy = (p1.y + p2.y)/2 - 0.1;
          const oz = (p1.z + p2.z)/2 + 0.12;
          createAtomSphere(ox, oy, oz, 0.15, oColor);
          createBond(p1, {x: ox, y: oy, z: oz}, 0.035, 0x94a3b8);
          createBond({x: ox, y: oy, z: oz}, p2, 0.035, 0x94a3b8);
        });

      } else if (mat.id === "mica") {
        addUnitCellBox(2.5, 2.8, 2.0, 0xf59e0b);
        const kColor = 0xeab308;
        const siColor = 0x0284c7;
        const oColor = 0xef4444;
        addLegendItem("K⁺ Interlayer", kColor);
        addLegendItem("Si/Al Tetrahedra", siColor);
        addLegendItem("Oxygen Sheets", oColor);

        [-0.8, 0, 0.8].forEach(x => {
          [-0.6, 0.6].forEach(z => {
            createAtomSphere(x, 0.7, z, 0.18, siColor);
            createAtomSphere(x, 0.95, z, 0.14, oColor);
            createAtomSphere(x, -0.7, z, 0.18, siColor);
            createAtomSphere(x, -0.95, z, 0.14, oColor);
          });
        });
        [-0.5, 0.5].forEach(x => createAtomSphere(x, 0, 0, 0.28, kColor));

      } else if (mat.id === "ptfe") {
        const cColor = 0x334155;
        const fColor = 0x06b6d4;
        addLegendItem("Carbon (C Backbone)", cColor);
        addLegendItem("Fluorine (F Sheath)", fColor);

        const count = 10;
        const carbons = [];
        for (let i = 0; i < count; i++) {
          const t = i / (count - 1);
          const y = (t - 0.5) * 2.8;
          const angle = t * Math.PI * 3.5;
          const cx = Math.cos(angle) * 0.25;
          const cz = Math.sin(angle) * 0.25;
          createAtomSphere(cx, y, cz, 0.18, cColor);
          carbons.push({x: cx, y, z: cz});

          const f1x = Math.cos(angle + 0.8) * 0.75;
          const f1z = Math.sin(angle + 0.8) * 0.75;
          const f2x = Math.cos(angle - 0.8) * 0.75;
          const f2z = Math.sin(angle - 0.8) * 0.75;
          createAtomSphere(f1x, y, f1z, 0.15, fColor);
          createAtomSphere(f2x, y, f2z, 0.15, fColor);
          createBond({x: cx, y, z: cz}, {x: f1x, y, z: f1z}, 0.03, 0x67e8f9);
          createBond({x: cx, y, z: cz}, {x: f2x, y, z: f2z}, 0.03, 0x67e8f9);
        }
        for (let i = 0; i < carbons.length - 1; i++) {
          createBond(carbons[i], carbons[i+1], 0.05, 0x64748b);
        }

      } else if (mat.id === "pe" || mat.id === "pp" || mat.id === "ps" || mat.id === "pet") {
        const cColor = 0x334155;
        const hColor = 0xf8fafc;
        addLegendItem("Carbon (C)", cColor);
        addLegendItem("Hydrogen (H)", hColor);

        const count = 8;
        const carbons = [];
        for (let i = 0; i < count; i++) {
          const y = (i - 3.5) * 0.35;
          const x = (i % 2 === 0) ? -0.3 : 0.3;
          createAtomSphere(x, y, 0, 0.18, cColor);
          carbons.push({x, y, z: 0});

          if (mat.id === "pe") {
            createAtomSphere(x - 0.35, y, 0.3, 0.12, hColor);
            createAtomSphere(x - 0.35, y, -0.3, 0.12, hColor);
            createBond({x, y, z: 0}, {x: x - 0.35, y, z: 0.3}, 0.025, 0xcbd5e1);
            createBond({x, y, z: 0}, {x: x - 0.35, y, z: -0.3}, 0.025, 0xcbd5e1);
          } else if (mat.id === "pp" && i % 2 === 0) {
            const ch3Color = 0xf59e0b;
            if (i === 0) addLegendItem("Methyl (-CH₃)", ch3Color);
            createAtomSphere(x + 0.6, y, 0, 0.24, ch3Color);
            createBond({x, y, z: 0}, {x: x + 0.6, y, z: 0}, 0.04, 0xfcd34d);
          } else if (mat.id === "ps" && i % 2 === 0) {
            const ringColor = 0xec4899;
            if (i === 0) addLegendItem("Phenyl Ring (-C₆H₅)", ringColor);
            for (let a = 0; a < 6; a++) {
              const ang = (a / 6) * Math.PI * 2;
              createAtomSphere(x + 0.7 + Math.cos(ang)*0.4, y, Math.sin(ang)*0.4, 0.12, ringColor);
            }
            createBond({x, y, z: 0}, {x: x + 0.7, y, z: 0}, 0.035, 0xf472b6);
          } else if (mat.id === "pet") {
            const oColor = 0xef4444;
            if (i === 0) addLegendItem("Ester Oxygen (-COO-)", oColor);
            if (i % 3 === 0) {
              createAtomSphere(x + 0.45, y, 0.3, 0.16, oColor);
              createBond({x, y, z: 0}, {x: x + 0.45, y, z: 0.3}, 0.03, 0xf87171);
            }
          }
        }
        for (let i = 0; i < carbons.length - 1; i++) {
          createBond(carbons[i], carbons[i+1], 0.045, 0x64748b);
        }

      } else if (mat.id === "air") {
        addLegendItem("Nitrogen N₂", 0x3b82f6);
        addLegendItem("Oxygen O₂", 0xef4444);
        const molecules = [
          { type: "N", x: -0.8, y: 0.6, z: 0.2, ang: 0.4 },
          { type: "N", x: 0.7, y: -0.5, z: -0.4, ang: 1.2 },
          { type: "O", x: -0.3, y: -0.7, z: 0.6, ang: 2.1 },
          { type: "N", x: 0.5, y: 0.8, z: -0.2, ang: -0.8 }
        ];
        molecules.forEach(m => {
          const col = (m.type === "N") ? 0x3b82f6 : 0xef4444;
          const dx = Math.cos(m.ang) * 0.22;
          const dy = Math.sin(m.ang) * 0.22;
          createAtomSphere(m.x - dx, m.y - dy, m.z, 0.18, col);
          createAtomSphere(m.x + dx, m.y + dy, m.z, 0.18, col);
          createBond({x: m.x - dx, y: m.y - dy, z: m.z}, {x: m.x + dx, y: m.y + dy, z: m.z}, 0.04, col);
        });

      } else if (mat.id === "vacuum") {
        addLegendItem("Vacuum Grid (Free Space)", 0x64748b);
        addUnitCellBox(2.4, 2.4, 2.4, 0x334155);
      }
    }

    // 2D Canvas Engine
    function drawIsometricCapacitor(ctx, width, height, opts) {
      ctx.clearRect(0, 0, width, height);

      const {
        voltage,
        d_mm,
        er,
        hasDielectric,
        dielectricLabel,
        dielectricColor = "rgba(168, 85, 247, 0.35)",
        showDipoles = true,
        showBoundCharges = true
      } = opts;

      const centerX = width * 0.5;
      const centerY = height * 0.52;
      const plateW = Math.min(width * 0.55, 260);
      const plateD = plateW * 0.45;
      const d_px = 40 + ((d_mm - 0.2) / 4.8) * 110;
      const halfGap = d_px * 0.5;
      const plateThick = 12;

      const topPlateY = centerY - halfGap;
      const botPlateY = centerY + halfGap;
      const fieldIntensity = Math.min(voltage / 100, 1.0);

      ctx.save();
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = "#475569";
      ctx.beginPath();
      ctx.moveTo(centerX - plateW * 0.5 + 20, topPlateY - plateThick);
      ctx.lineTo(centerX - plateW * 0.5 - 60, topPlateY - plateThick);
      ctx.lineTo(centerX - plateW * 0.5 - 60, centerY - 25);
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(centerX - plateW * 0.5 + 20, botPlateY + plateThick);
      ctx.lineTo(centerX - plateW * 0.5 - 60, botPlateY + plateThick);
      ctx.lineTo(centerX - plateW * 0.5 - 60, centerY + 25);
      ctx.stroke();

      const batX = centerX - plateW * 0.5 - 60;
      ctx.strokeStyle = "#38bdf8";
      ctx.beginPath();
      ctx.moveTo(batX - 16, centerY - 8);
      ctx.lineTo(batX + 16, centerY - 8);
      ctx.stroke();

      ctx.strokeStyle = "#94a3b8";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(batX - 8, centerY + 8);
      ctx.lineTo(batX + 8, centerY + 8);
      ctx.stroke();

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px sans-serif";
      ctx.textAlign = "right";
      ctx.fillText(voltage.toFixed(0) + " V", batX - 22, centerY + 4);
      ctx.fillText("+", batX - 22, centerY - 10);
      ctx.fillText("-", batX - 22, centerY + 20);
      ctx.restore();

      function drawSlab(yCenter, thickness, fillColor, strokeColor) {
        const yTop = yCenter - thickness / 2;
        const pTop = [
          { x: centerX, y: yTop - plateD * 0.5 },
          { x: centerX + plateW * 0.5, y: yTop },
          { x: centerX, y: yTop + plateD * 0.5 },
          { x: centerX - plateW * 0.5, y: yTop }
        ];

        ctx.fillStyle = fillColor;
        ctx.strokeStyle = strokeColor;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(pTop[0].x, pTop[0].y);
        ctx.lineTo(pTop[1].x, pTop[1].y);
        ctx.lineTo(pTop[2].x, pTop[2].y);
        ctx.lineTo(pTop[3].x, pTop[3].y);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = fillColor;
        ctx.beginPath();
        ctx.moveTo(pTop[1].x, pTop[1].y);
        ctx.lineTo(pTop[1].x, pTop[1].y + thickness);
        ctx.lineTo(pTop[2].x, pTop[2].y + thickness);
        ctx.lineTo(pTop[2].x, pTop[2].y);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(pTop[3].x, pTop[3].y);
        ctx.lineTo(pTop[3].x, pTop[3].y + thickness);
        ctx.lineTo(pTop[2].x, pTop[2].y + thickness);
        ctx.lineTo(pTop[2].x, pTop[2].y);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();
      }

      drawSlab(botPlateY, plateThick, "#1e293b", "#3b82f6");

      if (hasDielectric) {
        drawSlab(centerY, d_px, dielectricColor, "rgba(216, 180, 254, 0.8)");

        if (showDipoles && voltage > 0) {
          const rows = 3, cols = 5;
          ctx.save();
          for (let r = 0; r < rows; r++) {
            for (let c = 0; c < cols; c++) {
              const u = (c + 0.5) / cols - 0.5;
              const v = (r + 0.5) / rows - 0.5;
              const isoX = centerX + u * (plateW * 0.7);
              const isoY = centerY + v * (d_px * 0.6) + (u * 10);
              const dipoleLen = 14 * Math.min(er / 5, 1.4);

              ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
              ctx.fillStyle = "rgba(30, 41, 59, 0.7)";
              ctx.beginPath();
              ctx.ellipse(isoX, isoY, 7, dipoleLen * 0.5, 0, 0, Math.PI * 2);
              ctx.fill();
              ctx.stroke();

              ctx.fillStyle = "#ef4444";
              ctx.font = "bold 9px monospace";
              ctx.textAlign = "center";
              ctx.fillText("-", isoX, isoY - dipoleLen * 0.25 + 3);

              ctx.fillStyle = "#38bdf8";
              ctx.fillText("+", isoX, isoY + dipoleLen * 0.25 + 3);
            }
          }
          ctx.restore();
        }

        if (showBoundCharges && voltage > 0) {
          ctx.save();
          ctx.font = "bold 11px sans-serif";
          ctx.textAlign = "center";
          ctx.fillStyle = "#f87171";
          for (let i = -3; i <= 3; i++) {
            ctx.fillText("⊖", centerX + i * 28, topPlateY + 14);
          }
          ctx.fillStyle = "#38bdf8";
          for (let i = -3; i <= 3; i++) {
            ctx.fillText("⊕", centerX + i * 28, botPlateY - 6);
          }
          ctx.restore();
        }

        ctx.fillStyle = "#f8fafc";
        ctx.font = "bold 13px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(dielectricLabel + " (ε_r = " + er.toFixed(er < 2 ? 4 : 2) + ")", centerX, centerY + 4);

      } else {
        if (voltage > 0) {
          ctx.save();
          ctx.strokeStyle = "rgba(56, 189, 248, " + (0.3 + fieldIntensity * 0.6) + ")";
          ctx.lineWidth = 1.5;
          ctx.setLineDash([4, 4]);
          const lines = 7;
          for (let i = 0; i < lines; i++) {
            const frac = (i + 0.5) / lines - 0.5;
            const lx = centerX + frac * (plateW * 0.7);
            const lyStart = topPlateY + plateThick * 0.5;
            const lyEnd = botPlateY - plateThick * 0.5;

            ctx.beginPath();
            ctx.moveTo(lx, lyStart);
            ctx.lineTo(lx, lyEnd);
            ctx.stroke();

            ctx.fillStyle = "#38bdf8";
            ctx.beginPath();
            ctx.moveTo(lx, lyEnd - 8);
            ctx.lineTo(lx - 4, lyEnd - 14);
            ctx.lineTo(lx + 4, lyEnd - 14);
            ctx.closePath();
            ctx.fill();
          }
          ctx.setLineDash([]);
          ctx.restore();
        }

        ctx.fillStyle = "#94a3b8";
        ctx.font = "italic 13px sans-serif";
        ctx.textAlign = "center";
        ctx.fillText("Vacuum (ε_r = 1.0)", centerX, centerY + 4);
      }

      drawSlab(topPlateY, plateThick, "#1e293b", "#ef4444");

      if (voltage > 0) {
        ctx.save();
        const numCharges = Math.min(Math.max(Math.round(voltage / 15 * Math.min(er || 1, 5)), 3), 11);
        ctx.font = "bold 12px sans-serif";
        ctx.textAlign = "center";

        ctx.fillStyle = "#ef4444";
        for (let i = 0; i < numCharges; i++) {
          const frac = (i + 0.5) / numCharges - 0.5;
          ctx.fillText("+Q", centerX + frac * (plateW * 0.75), topPlateY - 4);
        }

        ctx.fillStyle = "#3b82f6";
        for (let i = 0; i < numCharges; i++) {
          const frac = (i + 0.5) / numCharges - 0.5;
          ctx.fillText("-Q", centerX + frac * (plateW * 0.75), botPlateY + plateThick + 14);
        }
        ctx.restore();
      }

      ctx.save();
      const dimX = centerX + plateW * 0.5 + 25;
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(dimX, topPlateY);
      ctx.lineTo(dimX, botPlateY);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(dimX - 6, topPlateY);
      ctx.lineTo(dimX + 6, topPlateY);
      ctx.moveTo(dimX - 6, botPlateY);
      ctx.lineTo(dimX + 6, botPlateY);
      ctx.stroke();

      ctx.fillStyle = "#f59e0b";
      ctx.font = "bold 12px monospace";
      ctx.textAlign = "left";
      ctx.fillText("d = " + d_mm.toFixed(2) + " mm", dimX + 10, centerY + 4);
      ctx.restore();
    }

    // Module 1 Controller
    const m1_v_slider = document.getElementById("m1-v");
    const m1_d_slider = document.getElementById("m1-d");
    const m1_a_slider = document.getElementById("m1-a");

    function updateModule1() {
      const v = parseFloat(m1_v_slider.value);
      const d_mm = parseFloat(m1_d_slider.value);
      const a_cm2 = parseFloat(m1_a_slider.value);

      document.getElementById("m1-v-val").textContent = v.toFixed(1) + " V";
      document.getElementById("m1-d-val").textContent = d_mm.toFixed(2) + " mm";
      document.getElementById("m1-a-val").textContent = a_cm2.toFixed(1) + " cm²";

      const d_m = d_mm * 1e-3;
      const a_m2 = a_cm2 * 1e-4;
      const e_Vm = d_m > 0 ? v / d_m : 0;
      const c_F = (EPS_0 * a_m2) / d_m;
      const q_C = c_F * v;
      const u_J = 0.5 * c_F * v * v;

      document.getElementById("m1-res-e").textContent = (e_Vm / 1e3).toFixed(2) + " kV/m";
      document.getElementById("m1-res-c").textContent = (c_F * 1e12).toFixed(2) + " pF";
      document.getElementById("m1-res-q").textContent = (q_C * 1e9).toFixed(3) + " nC";
      document.getElementById("m1-res-u").textContent = (u_J * 1e9).toFixed(2) + " nJ";

      const cvs = document.getElementById("canvas-module1");
      if (cvs) {
        cvs.width = cvs.clientWidth * window.devicePixelRatio || 500;
        cvs.height = cvs.clientHeight * window.devicePixelRatio || 400;
        const ctx = cvs.getContext("2d");
        drawIsometricCapacitor(ctx, cvs.width, cvs.height, {
          voltage: v,
          d_mm: d_mm,
          er: 1.0,
          hasDielectric: false
        });
      }
    }
    [m1_v_slider, m1_d_slider, m1_a_slider].forEach(el => el.addEventListener("input", updateModule1));

    // Module 2 Controller
    const m2_v_slider = document.getElementById("m2-v");
    const m2_d_slider = document.getElementById("m2-d");
    const m2_er_slider = document.getElementById("m2-er");
    let m2_viewDipoles = true, m2_viewCharges = true;

    document.getElementById("m2-view-dipoles").addEventListener("click", function() {
      m2_viewDipoles = !m2_viewDipoles;
      this.className = m2_viewDipoles ? "px-2 py-1 rounded bg-emerald-600 text-white font-medium" : "px-2 py-1 rounded text-slate-300 hover:text-white";
      updateModule2();
    });

    document.getElementById("m2-view-charges").addEventListener("click", function() {
      m2_viewCharges = !m2_viewCharges;
      this.className = m2_viewCharges ? "px-2 py-1 rounded bg-emerald-600 text-white font-medium" : "px-2 py-1 rounded text-slate-300 hover:text-white";
      updateModule2();
    });

    document.querySelectorAll(".preset-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        m2_er_slider.value = btn.dataset.er;
        updateModule2();
      });
    });

    function updateModule2() {
      const v = parseFloat(m2_v_slider.value);
      const d_mm = parseFloat(m2_d_slider.value);
      const er = parseFloat(m2_er_slider.value);
      const a_m2 = 25.0 * 1e-4;
      const d_m = d_mm * 1e-3;

      document.getElementById("m2-v-val").textContent = v.toFixed(1) + " V";
      document.getElementById("m2-d-val").textContent = d_mm.toFixed(2) + " mm";
      document.getElementById("m2-er-val").textContent = er.toFixed(2);
      document.getElementById("m2-gain-badge").textContent = "× " + er.toFixed(2);

      const e_Vm = d_m > 0 ? v / d_m : 0;
      const c_F = (er * EPS_0 * a_m2) / d_m;
      const q_C = c_F * v;
      const u_J = 0.5 * c_F * v * v;

      document.getElementById("m2-res-e").textContent = (e_Vm / 1e3).toFixed(2) + " kV/m";
      document.getElementById("m2-res-c").textContent = (c_F * 1e12).toFixed(2) + " pF";
      document.getElementById("m2-res-q").textContent = (q_C * 1e9).toFixed(3) + " nC";
      document.getElementById("m2-res-u").textContent = (u_J * 1e9).toFixed(2) + " nJ";

      const cvs = document.getElementById("canvas-module2");
      if (cvs) {
        cvs.width = cvs.clientWidth * window.devicePixelRatio || 500;
        cvs.height = cvs.clientHeight * window.devicePixelRatio || 400;
        const ctx = cvs.getContext("2d");
        drawIsometricCapacitor(ctx, cvs.width, cvs.height, {
          voltage: v,
          d_mm: d_mm,
          er: er,
          hasDielectric: true,
          dielectricLabel: "Dielectric Slab",
          dielectricColor: "rgba(16, 185, 129, 0.4)",
          showDipoles: m2_viewDipoles,
          showBoundCharges: m2_viewCharges
        });
      }
    }
    [m2_v_slider, m2_d_slider, m2_er_slider].forEach(el => el.addEventListener("input", updateModule2));

    // Module 3 Controller
    const m3_v_slider = document.getElementById("m3-v");
    const m3_d_slider = document.getElementById("m3-d");

    function renderMaterialButtons() {
      const container = document.getElementById("material-buttons-grid");
      container.innerHTML = "";

      LINEAR_MATERIALS.forEach(mat => {
        const btn = document.createElement("button");
        const isActive = mat.id === currentSelectedMaterial.id;
        btn.className = `p-2 rounded-lg text-left transition flex items-center justify-between border w-full ${
          isActive 
            ? "bg-purple-900/70 border-purple-500 text-white shadow-md shadow-purple-950" 
            : "bg-slate-800/60 border-slate-700/60 text-slate-300 hover:bg-slate-700/80 hover:text-white"
        }`;
        
        btn.innerHTML = `
          <div class="flex flex-col min-w-0 pr-2">
            <span class="font-bold text-xs truncate">${mat.name}</span>
            <span class="text-[10px] text-slate-400 truncate">${mat.formula}</span>
          </div>
          <span class="text-[10px] font-mono font-semibold px-2 py-0.5 rounded whitespace-nowrap ${isActive ? 'bg-purple-800 text-purple-200' : 'bg-slate-900 text-slate-400'}">ε_r: ${mat.er.toFixed(mat.er < 2 ? 4 : 2)}</span>
        `;

        btn.addEventListener("click", () => {
          selectMaterial(mat);
        });

        container.appendChild(btn);
      });
    }

    function selectMaterial(mat) {
      currentSelectedMaterial = mat;
      renderMaterialButtons();

      document.getElementById("mat-disp-type").textContent = mat.type;
      document.getElementById("mat-card-name").textContent = `${mat.name} (${mat.formula})`;
      document.getElementById("mat-card-chi").textContent = mat.chi.toFixed(mat.chi < 1 ? 4 : 2);
      document.getElementById("mat-card-er").textContent = mat.er.toFixed(mat.er < 2 ? 4 : 2);
      document.getElementById("mat-desc-text").textContent = mat.mechanism;
      
      document.getElementById("mat-ref-text").textContent = mat.sourceTitle;
      document.getElementById("mat-ref-link").href = mat.url;
      document.getElementById("mat-ref-cond").textContent = mat.sourceCondition;

      document.getElementById("lattice-title").textContent = `${mat.name} Structure`;
      document.getElementById("lattice-system").textContent = mat.crystalSystem;
      document.getElementById("lattice-formula").textContent = mat.formula;

      buildCrystalModel(mat);
      updateModule3();
    }

    function updateModule3() {
      const v = parseFloat(m3_v_slider.value);
      const d_mm = parseFloat(m3_d_slider.value);
      const mat = currentSelectedMaterial;

      document.getElementById("m3-v-val").textContent = v.toFixed(1) + " V";
      document.getElementById("m3-d-val").textContent = d_mm.toFixed(2) + " mm";
      document.getElementById("m3-cap-matname").textContent = mat.name;
      document.getElementById("m3-slab-label").textContent = `${mat.name} (ε_r = ${mat.er.toFixed(mat.er < 2 ? 4 : 2)})`;

      const d_m = d_mm * 1e-3;
      const a_m2 = 25.0 * 1e-4;
      const e_Vm = d_m > 0 ? v / d_m : 0;
      const c_F = (mat.er * EPS_0 * a_m2) / d_m;
      const q_C = c_F * v;
      const u_J = 0.5 * c_F * v * v;

      document.getElementById("m3-res-e").textContent = (e_Vm / 1e3).toFixed(2) + " kV/m";
      document.getElementById("m3-res-c").textContent = (c_F * 1e12).toFixed(2) + " pF";
      document.getElementById("m3-res-q").textContent = (q_C * 1e9).toFixed(3) + " nC";
      document.getElementById("m3-res-u").textContent = (u_J * 1e9).toFixed(2) + " nJ";

      const cvs = document.getElementById("canvas-module3");
      if (cvs) {
        cvs.width = cvs.clientWidth * window.devicePixelRatio || 500;
        cvs.height = cvs.clientHeight * window.devicePixelRatio || 360;
        const ctx = cvs.getContext("2d");
        drawIsometricCapacitor(ctx, cvs.width, cvs.height, {
          voltage: v,
          d_mm: d_mm,
          er: mat.er,
          hasDielectric: mat.id !== "vacuum",
          dielectricLabel: mat.name,
          dielectricColor: "rgba(168, 85, 247, 0.4)",
          showDipoles: mat.id !== "vacuum",
          showBoundCharges: mat.id !== "vacuum"
        });
      }
    }
    [m3_v_slider, m3_d_slider].forEach(el => el.addEventListener("input", updateModule3));

    function populateReferencesTable() {
      const tbody = document.getElementById("references-table-body");
      tbody.innerHTML = "";

      LINEAR_MATERIALS.forEach(mat => {
        const tr = document.createElement("tr");
        tr.className = "hover:bg-slate-800/40 transition";
        tr.innerHTML = `
          <td class="py-3 px-4 font-semibold text-white flex items-center space-x-2">
            <span>${mat.name}</span>
            <span class="text-[10px] text-slate-400 font-mono">(${mat.formula})</span>
          </td>
          <td class="py-3 px-3 text-center font-mono font-bold text-cyan-300">
            ${mat.er.toFixed(mat.er < 2 ? 4 : 2)}
          </td>
          <td class="py-3 px-3 text-center font-mono text-amber-300">
            ${mat.chi.toFixed(mat.chi < 1 ? 4 : 2)}
          </td>
          <td class="py-3 px-4 text-xs text-slate-300">
            ${mat.crystalSystem}
          </td>
          <td class="py-3 px-4 text-xs font-medium">
            <a href="${mat.url}" target="_blank" rel="noopener noreferrer" class="text-cyan-400 hover:underline flex items-center">
              ${mat.sourceTitle}
              <svg class="w-3 h-3 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </td>
          <td class="py-3 px-4 text-xs text-slate-400 italic">
            ${mat.sourceCondition}
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    window.addEventListener("DOMContentLoaded", () => {
      if (typeof renderMathInElement === "function") {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "\\[", right: "\\]", display: true },
            { left: "\\(", right: "\\)", display: false },
            { left: "$", right: "$", display: false }
          ],
          throwOnError: false
        });
      }

      renderMaterialButtons();
      populateReferencesTable();

      updateModule1();
      updateModule2();
      updateModule3();

      initThreeJS();
    });
  </script>
</body>
</html>''')

with open('dielectric-lab/index.html', 'w', encoding='utf-8') as f:
    f.write(''.join(parts))

print('Wrote index.html cleanly!')
