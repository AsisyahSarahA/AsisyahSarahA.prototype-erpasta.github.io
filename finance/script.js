document.addEventListener('DOMContentLoaded', function() {
    // Styling base for charts
    Chart.defaults.color = '#94a3b8';
    Chart.defaults.font.family = "'Inter', sans-serif";

    // Cashflow Chart (Line)
    const ctxCashflow = document.getElementById('cashflowChart').getContext('2d');
    
    const gradientIn = ctxCashflow.createLinearGradient(0, 0, 0, 400);
    gradientIn.addColorStop(0, 'rgba(16, 185, 129, 0.5)');
    gradientIn.addColorStop(1, 'rgba(16, 185, 129, 0.0)');
    
    const gradientOut = ctxCashflow.createLinearGradient(0, 0, 0, 400);
    gradientOut.addColorStop(0, 'rgba(239, 68, 68, 0.5)');
    gradientOut.addColorStop(1, 'rgba(239, 68, 68, 0.0)');

    new Chart(ctxCashflow, {
        type: 'line',
        data: {
            labels: ['Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep'],
            datasets: [
                {
                    label: 'Kas Masuk',
                    data: [120, 150, 180, 140, 210, 250],
                    borderColor: '#10b981',
                    backgroundColor: gradientIn,
                    borderWidth: 2,
                    tension: 0.4,
                    fill: true
                },
                {
                    label: 'Kas Keluar',
                    data: [80, 100, 120, 110, 140, 160],
                    borderColor: '#ef4444',
                    backgroundColor: gradientOut,
                    borderWidth: 2,
                    tension: 0.4,
                    fill: true
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    align: 'end',
                    labels: { boxWidth: 12, usePointStyle: true }
                }
            },
            scales: {
                y: {
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    border: { display: false }
                },
                x: {
                    grid: { display: false },
                    border: { display: false }
                }
            }
        }
    });

    // Profitability Chart (Doughnut)
    const ctxProfit = document.getElementById('profitabilityChart').getContext('2d');
    new Chart(ctxProfit, {
        type: 'doughnut',
        data: {
            labels: ['ERP E-Commerce V2', 'Sistem HRIS', 'Mobile App', 'Maintenance SLA'],
            datasets: [{
                data: [45, 25, 15, 15],
                backgroundColor: [
                    '#8b5cf6',
                    '#3b82f6',
                    '#10b981',
                    '#f59e0b'
                ],
                borderWidth: 0,
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '75%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { 
                        color: '#f8fafc',
                        padding: 20,
                        usePointStyle: true,
                        font: { size: 12 }
                    }
                }
            }
        }
    });

    // --- ACCORDION LOGIC ---
    const hasSubmenuItems = document.querySelectorAll('.has-submenu');
    hasSubmenuItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const parent = item.closest('.nav-group');
            const isOpen = parent.classList.contains('open');
            
            document.querySelectorAll('.nav-group').forEach(group => {
                group.classList.remove('open');
            });

            if (!isOpen) {
                parent.classList.add('open');
            }
        });
    });

    // --- SPA ROUTING LOGIC ---
    function switchView(targetId, title = '') {
        // Hide all views
        document.querySelectorAll('.view-section').forEach(view => {
            view.style.display = 'none';
        });

        // Show target view
        const targetView = document.getElementById(targetId);
        if (targetView) {
            targetView.style.display = 'block';
            
            // If it's the generic view, update the text to look customized
            if (targetId === 'view-generic' && title) {
                document.getElementById('generic-title').textContent = title;
                document.getElementById('generic-subtitle').textContent = title;
            }
        }
    }

    // Attach click listeners to all links with data-target
    const navLinks = document.querySelectorAll('[data-target]');
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            
            // Handle active states visually
            document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
            document.querySelectorAll('.submenu-item').forEach(sub => sub.classList.remove('active'));
            
            if (link.classList.contains('submenu-item')) {
                link.classList.add('active');
                // Highlight parent menu as well
                link.closest('.nav-group').querySelector('.nav-item').classList.add('active');
            } else {
                link.classList.add('active');
            }
            
            // Routing
            const targetId = link.getAttribute('data-target');
            const title = link.getAttribute('data-title') || link.textContent;
            
            switchView(targetId, title);
        });
    });

    // --- MODAL LOGIC ---
    const modal = document.getElementById('dummyModal');
    const modalTitle = document.getElementById('modalTitle');
    
    // Listen for all buttons with .primary-btn
    document.querySelectorAll('.primary-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            
            // If the button is inside the modal itself, don't trigger open
            if (btn.closest('.modal-content')) return;

            // Update title based on button text
            const btnText = btn.textContent.trim();
            modalTitle.textContent = btnText || "Tambah Data Baru";
            
            modal.classList.add('active');
        });
    });

    // Close modal
    document.querySelectorAll('.close-modal').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const openModal = btn.closest('.modal-overlay');
            if (openModal) {
                openModal.classList.remove('active');
            }
        });
    });

    // Close on click outside
    document.querySelectorAll('.modal-overlay').forEach(m => {
        m.addEventListener('click', (e) => {
            if (e.target === m) {
                m.classList.remove('active');
            }
        });
    });
});
