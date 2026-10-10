# Dielectric Materials & Polarization Interactive Laboratory

An interactive educational and research web application illustrating how dielectric constant ($\varepsilon_r$) and layer thickness ($d$) govern capacitance ($C$), stored charge ($Q$), and stored electrostatic energy ($W$), featuring 3D crystallographic lattice visualizations and field-dependent nonlinear ferroelectric nanoceramic analyses based on *Physical Review B 85, 224111 (2012)*.

---

## 🚀 Quick Start
- **Option 1**: Double-click `index.html` (or run `open_in_browser.bat`) to open directly in your web browser.
- **Option 2 (Local HTTP Server)**:
  ```bash
  python -m http.server 8000
  ```
  Then navigate to `http://localhost:8000` in Google Chrome, Microsoft Edge, or Mozilla Firefox.

---

## 🔬 Web Application Modules

### 1. Part 1: Parallel-Plate Capacitor in Vacuum ($\varepsilon_r = 1.0$)
- **Physical Concept**: Two parallel conducting plates separated by vacuum ($\chi_e = 0$).
- **Derivations & Transcript Script**: Complete theoretical presentation based on Gauss's Law and David J. Griffiths (*Introduction to Electrodynamics*):
  $$C_0 = \frac{\varepsilon_0 A}{d} = \frac{Q}{V}, \quad W = \int_0^Q \left(\frac{q}{C}\right) dq = \frac{1}{2} C V^2$$
- **Adjustable Controls**:
  - Voltage $V$ ($0 \sim 200\text{ V}$)
  - Layer Thickness / Plate Separation $d$ ($0.20 \sim 5.00\text{ mm}$)
  - Plate Electrode Area $A$ ($5 \sim 100\text{ cm}^2$)
- **Interactive Visuals**: 2.5D isometric parallel plates displaying electric field vectors and surface charge symbols ($+Q$ and $-Q$).
- **Live Output Displays**: Electric field $E = V/d$, capacitance $C$, stored charge $Q$, and electrostatic energy $W$.

---

### 2. Part 2: Dielectric Insertion & Polarization Mechanism ($\varepsilon_r > 1$)
- **Physical Concept**: Filling the capacitor gap with an insulating dielectric material.
- **Microscopic Physics**:
  - Dielectric polarization produces a counteracting internal field:
    $$E_{pol} = -\frac{P}{\varepsilon_0}, \quad P = \varepsilon_0 \chi_e E$$
  - Under fixed voltage $V$, total bounded charge on conductor plates increases:
    $$\varepsilon_0 E_{plate} = (1 + \chi_e)\varepsilon_0 E_0 = \varepsilon_0 \varepsilon_r E_0$$
    $$C = \frac{\varepsilon_0 \varepsilon_r A}{d} = \varepsilon_r C_0$$
- **Adjustable Controls**: Voltage $V$, Gap $d$, and Dielectric Constant $\varepsilon_r$ ($1.0 \sim 25.0$ plus quick-presets for Teflon, Silica, Quartz, Alumina).
- **Interactive Visuals**: Toggles for aligned microscopic electric dipoles ($\oplus - \ominus$) and surface bound charges ($\pm \sigma_b$).
- **Dynamic Readouts**: Live recalculation of $E$, $C$, $Q$, and $W$ with dielectric amplification badge ($\times \varepsilon_r$).

---

### 3. Part 3: 4 Key Linear Dielectric Materials & 3D Crystal Structures
- **Selected Materials**:
  1. **Alumina (Al / $\alpha\text{-Al}_2\text{O}_3$)**: Trigonal Corundum ($R\bar{3}c$, $\varepsilon_r \approx 9.50$). $\text{AlO}_6$ octahedral coordination in a hexagonal close-packed oxygen sublattice.
  2. **Silicon Nitride ($\beta\text{-Si}_3\text{N}_4$)**: Hexagonal ($P6_3/m$, $\varepsilon_r \approx 7.50$). Corner-sharing $\text{SiN}_4$ tetrahedra forming distinct hexagonal ring channels along the $c$-axis.
  3. **PET (Polyethylene Terephthalate)**: Triclinic ($P\bar{1}$, $\varepsilon_r \approx 3.20$). Planar aromatic phenylene ring conjugated with ester carbonyl groups ($-\text{COO}-$) and an ethylene bridge.
  4. **Teflon (PTFE / Polytetrafluoroethylene)**: Helical chain conformation ($15/7$ helix, $\varepsilon_r \approx 2.10$). Twisted carbon core shielded by dense outer fluorine atoms.
- **Top Section**:
  - Material selector buttons displaying formula and $\varepsilon_r$.
  - High-fidelity **3D WebGL crystal / molecular structure visualizer (Three.js)**: Click and drag to rotate, mouse wheel to zoom, toggle auto-rotation, reset camera, and live color-coded elemental legend.
  - Parameter cards displaying $\chi_e$, $\varepsilon_r$, polarization mechanism, and verified source citations.
- **Bottom Section**:
  - Interactive capacitor simulator for the selected material (matching Interaction 2), with adjustable $V$ and $d$ sliders, live dipole rendering, and real-time computation of $E$, $C$, $Q$, and $W$.

---

### 4. Part 4: Nonlinear Permittivity in $\text{BaTiO}_3$ Ferroelectrics (PRB Fig. 3)
*Padurariu, Curecheriu, Buscaglia, and Mitoseriu, "Field-dependent permittivity in nanostructured $\mathrm{BaTiO}_3$ ceramics: Modeling and experimental verification", Phys. Rev. B 85, 224111 (2012).*
- **Embedded Figure 3**: Direct extraction of the original Figure 3 and caption from page 4 of the PRB paper (rendered via Base64 for guaranteed zero-breakage offline display).
- **Comprehensive Physical Explanation**:
  1. **Intrinsic Polarization Saturation & Landau-Devonshire Model**: Anharmonic double-well potential; at high electric fields $E$, ferroelectric domain dipoles align completely with the field, leading to $dP/dE \to 0$ and dropping $\varepsilon_r(E)$.
  2. **Johnson's Phenomenological Model**:
     $$\varepsilon_r(E) = \frac{\varepsilon_r(0)}{\left[1 + 3\beta \cdot \varepsilon_r(0)^3 \cdot \varepsilon_0^3 \cdot E^2\right]^{1/3}}$$
  3. **Grain-Size Dependent Core-Shell Model**: Nanostructured ceramics feature ferroelectric grain cores ($\varepsilon_{core} \approx 1000$) separated by non-ferroelectric grain boundary "dead layers" ($\varepsilon_{gb} \approx 100$). When grain size decreases to $100\text{ nm}$, dead-layer boundary volume reaches ~18%, acting as a low-dielectric dilution buffer.
  4. **Local Electric Field Inhomogeneity & Linearization**: Finite Element Method (FEM) and Monte Carlo Potts simulations prove that applied fields crowd into boundary hot spots while grain cores are shielded. Averaging the effective permittivity over this disordered distribution shifts the inflection point to higher fields, flattening $d\varepsilon_r/dE \approx -3\text{ (kV/cm)}^{-1}$ and producing a **remarkable linear $\varepsilon_r(E)$ response** in $100\text{ nm}$ nanoceramics.

---

## 📚 References & Verified Source Citations
- **[1] Wikipedia**: *Capacitor & Dielectric Materials*, [https://en.wikipedia.org/wiki/Capacitor](https://en.wikipedia.org/wiki/Capacitor)
- **[2] David J. Griffiths**: *Introduction to Electrodynamics*, 3rd ed., Prentice Hall, Chapters 2 & 4.
- **[3, 4] L. Padurariu, L. Curecheriu, V. Buscaglia, L. Mitoseriu**: *Field-dependent permittivity in nanostructured BaTiO₃ ceramics: Modeling and experimental verification*, **Physical Review B** 85, 224111 (2012). DOI: [10.1103/PhysRevB.85.224111](https://doi.org/10.1103/PhysRevB.85.224111)
- **NASA NEPP / MRS**: *Polycrystalline Alumina Dielectric Properties*, [NASA NEPP Paper](https://nepp.nasa.gov/docuploads/7cf49e5d-bb68-46d7-9dc6c13544a6747e/2004%20mrs%20fall%20paper%2088011%20g7.pdf)
- **CeramTec Industrial**: *Silicon Nitride Substrate Grade Technical Sheet*, [CeramTec Datasheet](https://www.ceramtec-industrial.com/en/products-applications/substrates/si3n4-substrates)
- **Röchling Sustadur**: *PET Engineering Thermoplastics ASTM D150*, [Röchling Datasheet](https://www.roechling.com/us/industrial/materials/thermoplastics/engineering-plastics/pet/sustadur-pet-tf-astm-717917)
- **Eagle Plastics / ASTM D150**: *PTFE Material Properties*, [Eagle Plastics PTFE](https://eagle-plastics.com/materials/ptfe/)
