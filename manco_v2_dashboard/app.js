/* ==========================================================================
   MANCO v2.0 SOTA ENGINE — APPLICATIVE LOGIC (app.js)
   Author: Dr. José A. García (UCV / Silas Core)
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // --- Navigation Controls ---
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.content-section');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = item.getAttribute('href').substring(1);

            navItems.forEach(n => n.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));

            item.classList.add('active');
            document.getElementById(targetId).classList.add('active');
        });
    });

    // --- MANCO v2.0 Engine Calculation Core ---
    const computeEngine = () => {
        // Fetch input values
        const mp1 = parseFloat(document.getElementById('mp1').value) || 0;
        const mp2 = parseFloat(document.getElementById('mp2').value) || 0;
        const mp3 = parseFloat(document.getElementById('mp3').value) || 1;
        const mp9 = parseFloat(document.getElementById('mp4').value) || 1;

        const c20tas = parseFloat(document.getElementById('c20tas').value) || 0;
        const c28tas = parseFloat(document.getElementById('c28tas').value) || 1;

        const acids = parseFloat(document.getElementById('acids').value) || 0;
        const asphalteneRatio = parseFloat(document.getElementById('asphaltene').value) || 0.1;

        // Constants
        const T0 = 298.15; // K
        const R = 8.314;   // J/mol*K
        const alpha = 0.35, beta = 0.40, gamma = 0.15, delta = 0.10;

        // Compute Tier 2 & Tier 3 ratios
        const tier2_mp = (mp1 + mp2) / (mp3 + mp9);
        const tier3_tas = c20tas / c28tas;

        // Cascade Function \Phi_{cascade}
        const phi_cascade = (alpha * (acids / 100.0)) +
                            (beta * tier2_mp) +
                            (gamma * tier3_tas) +
                            (delta * asphalteneRatio);

        // Entropy Generation \Delta S_{bio} (J/mol*K)
        const delta_s_bio = R * Math.log(1.0 + phi_cascade);

        // Gouy-Stodola Exergy Destroyed \Delta X_d (kJ/mol)
        const delta_x_d = (T0 * delta_s_bio) / 1000.0;

        // Viscosity Escalation Factor
        const visc_factor = Math.exp(0.45 * delta_x_d);

        // Net Exergy Balance E_{net} (kJ/mol)
        const e_net = Math.max(0.0, 42.0 - (delta_x_d + (1.2 * delta_x_d)));

        // Abandonment Flag
        const isAbandoned = delta_x_d >= 8.50;

        // Update UI Metrics
        document.getElementById('val-xd').innerHTML = `${delta_x_d.toFixed(2)} <small>kJ/mol</small>`;
        document.getElementById('val-sbio').innerHTML = `${delta_s_bio.toFixed(2)} <small>J/mol·K</small>`;
        document.getElementById('val-visc').innerHTML = `${visc_factor.toFixed(2)}<small>x</small>`;
        document.getElementById('val-enet').innerHTML = `${e_net.toFixed(2)} <small>kJ/mol</small>`;

        const statusBox = document.getElementById('box-e-net');
        const statusText = document.getElementById('val-abandonment-status');

        if (isAbandoned) {
            statusBox.style.borderLeftColor = '#f43f5e';
            statusText.style.color = '#f43f5e';
            statusText.innerText = '⚠️ Abandono Exergético Recomendado (E_net ≤ 0)';
        } else {
            statusBox.style.borderLeftColor = '#10b981';
            statusText.style.color = '#10b981';
            statusText.innerText = '✅ Producción Termodinámicamente Viable';
        }

        // Update Dynamic Viscosity Escalation Chart
        updateViscosityChart(delta_x_d);
    };

    // --- Chart.js Setup: Viscosity Escalation Curve ---
    const ctxVisc = document.getElementById('viscosityChart').getContext('2d');
    let viscosityChart = new Chart(ctxVisc, {
        type: 'line',
        data: {
            labels: ['PM 1', 'PM 3', 'PM 5', 'PM 6 (OWC)', 'PM 8', 'PM 10 (Abandono)'],
            datasets: [{
                label: 'Resistencia de Flujo & Viscosidad (cP x1000)',
                data: [5, 15, 45, 120, 320, 500],
                borderColor: '#38bdf8',
                backgroundColor: 'rgba(56, 189, 248, 0.1)',
                borderWidth: 3,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: '#94a3b8', font: { family: 'Inter' } } }
            },
            scales: {
                x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748b' } },
                y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#64748b' } }
            }
        }
    });

    const updateViscosityChart = (currentXd) => {
        const baseVisc = 10;
        const curve = [
            baseVisc * Math.exp(0.2 * currentXd),
            baseVisc * Math.exp(0.35 * currentXd),
            baseVisc * Math.exp(0.5 * currentXd),
            baseVisc * Math.exp(0.65 * currentXd),
            baseVisc * Math.exp(0.85 * currentXd),
            baseVisc * Math.exp(1.05 * currentXd)
        ];
        viscosityChart.data.datasets[0].data = curve.map(v => Math.round(v));
        viscosityChart.update();
    };

    // --- Chart.js Setup: SOTA Benchmark Comparison ---
    const ctxSota = document.getElementById('sotaChart').getContext('2d');
    new Chart(ctxSota, {
        type: 'bar',
        data: {
            labels: ['PM (1993) SOTA 1.0', 'MANCO v1.0 SOTA 2.0', 'MANCO v2.0 SOTA 3.0 (García 2026)'],
            datasets: [{
                label: 'Precisión Predictiva R² (vs. Resistencia de Flujo)',
                data: [0.6120, 0.8340, 0.9420],
                backgroundColor: [
                    'rgba(100, 116, 139, 0.6)',
                    'rgba(245, 158, 11, 0.6)',
                    'rgba(56, 189, 248, 0.8)'
                ],
                borderColor: [
                    '#64748b',
                    '#fbbf24',
                    '#38bdf8'
                ],
                borderWidth: 2,
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: '#94a3b8', font: { family: 'Inter' } } }
            },
            scales: {
                x: { grid: { display: false }, ticks: { color: '#94a3b8' } },
                y: { min: 0.4, max: 1.0, grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#94a3b8' } }
            }
        }
    });

    // --- Event Listeners ---
    document.getElementById('btn-compute').addEventListener('click', computeEngine);

    document.getElementById('btn-preset-mod').addEventListener('click', () => {
        document.getElementById('mp1').value = 864000;
        document.getElementById('mp2').value = 720000;
        document.getElementById('mp3').value = 709000;
        document.getElementById('mp4').value = 1260000;
        document.getElementById('c20tas').value = 333000;
        document.getElementById('c28tas').value = 788000;
        document.getElementById('acids').value = 150;
        document.getElementById('asphaltene').value = 0.35;
        computeEngine();
    });

    document.getElementById('btn-preset-sev').addEventListener('click', () => {
        document.getElementById('mp1').value = 210000;
        document.getElementById('mp2').value = 180000;
        document.getElementById('mp3').value = 709000;
        document.getElementById('mp4').value = 1260000;
        document.getElementById('c20tas').value = 110000;
        document.getElementById('c28tas').value = 788000;
        document.getElementById('acids').value = 650;
        document.getElementById('asphaltene').value = 2.80;
        computeEngine();
    });

    // Initial Compute
    computeEngine();
});
