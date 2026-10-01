html_content = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Astacode ERP - Modul Finance V3</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Specific Styles for new views */
        .split-screen { display: flex; gap: 24px; height: 100%; }
        .split-half { flex: 1; display: flex; flex-direction: column; background: rgba(255,255,255,0.02); border-radius: 12px; border: 1px solid var(--border-color); padding: 24px; }
        
        .todo-list { list-style: none; padding: 0; margin: 0; }
        .todo-item { display: flex; justify-content: space-between; align-items: center; padding: 16px; border-bottom: 1px solid var(--border-color); }
        .todo-item:last-child { border-bottom: none; }
        
        .termin-list { margin-top: 16px; border-left: 2px solid var(--border-color); margin-left: 20px; padding-left: 20px; }
        .termin-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px dashed var(--border-color); }
        
        .receipt-preview { width: 100%; height: 400px; background: #1e293b; border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-direction: column; color: var(--text-secondary); border: 2px dashed var(--border-color); }
        
        .tinder-card { display: flex; gap: 16px; align-items: stretch; margin-bottom: 16px; }
        .tinder-left, .tinder-right { flex: 1; padding: 16px; border-radius: 8px; background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); }
        
        .toggle-switch { position: relative; display: inline-block; width: 44px; height: 24px; }
        .toggle-switch input { opacity: 0; width: 0; height: 0; }
        .slider { position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #475569; transition: .4s; border-radius: 24px; }
        .slider:before { position: absolute; content: ""; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; transition: .4s; border-radius: 50%; }
        input:checked + .slider { background-color: var(--primary); }
        input:checked + .slider:before { transform: translateX(20px); }
    </style>
</head>
<body>
    <div class="app-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="brand">
                <div class="logo">A</div>
                <h2>Astacode</h2>
            </div>
            
            <nav class="nav-menu">
                <p class="nav-label">FINANCE V3</p>
                <a href="#" class="nav-item active" data-target="view-dashboard"><i class="fa-solid fa-chart-pie"></i> <span>Dashboard</span></a>

                <div class="nav-group">
                    <a href="#" class="nav-item has-submenu"><i class="fa-solid fa-download"></i> <span>Pemasukan (AR)</span><i class="fa-solid fa-chevron-down arrow"></i></a>
                    <div class="submenu">
                        <a href="#" class="submenu-item" data-target="view-penagihan">Daftar Invoice (Termin)</a>
                    </div>
                </div>

                <div class="nav-group">
                    <a href="#" class="nav-item has-submenu"><i class="fa-solid fa-upload"></i> <span>Pengeluaran (AP)</span><i class="fa-solid fa-chevron-down arrow"></i></a>
                    <div class="submenu">
                        <a href="#" class="submenu-item" data-target="view-klaim">Klaim & Struk (Expense)</a>
                        <a href="#" class="submenu-item" data-target="view-generic" data-title="Tagihan Vendor/Freelancer">Tagihan Vendor/Freelancer</a>
                        <a href="#" class="submenu-item" data-target="view-generic" data-title="Penggajian (OPEX)">Penggajian (Payroll)</a>
                    </div>
                </div>

                <div class="nav-group">
                    <a href="#" class="nav-item has-submenu"><i class="fa-solid fa-building-columns"></i> <span>Kas & Bank</span><i class="fa-solid fa-chevron-down arrow"></i></a>
                    <div class="submenu">
                        <a href="#" class="submenu-item" data-target="view-generic" data-title="Daftar Rekening & Saldo">Daftar Rekening</a>
                        <a href="#" class="submenu-item" data-target="view-generic" data-title="Mutasi Internal Bank">Mutasi Internal</a>
                        <a href="#" class="submenu-item" data-target="view-recon">Rekonsiliasi Bank</a>
                    </div>
                </div>

                <div class="nav-group">
                    <a href="#" class="nav-item has-submenu"><i class="fa-solid fa-chart-line"></i> <span>Laporan</span><i class="fa-solid fa-chevron-down arrow"></i></a>
                    <div class="submenu">
                        <a href="#" class="submenu-item" data-target="view-generic" data-title="Laba Rugi Perusahaan">Laba Rugi Perusahaan</a>
                        <a href="#" class="submenu-item" data-target="view-profit">Profitabilitas Proyek</a>
                    </div>
                </div>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <header class="topbar">
                <div class="search-bar">
                    <i class="fa-solid fa-search"></i>
                    <input type="text" placeholder="Cari nomor invoice, nama proyek, atau mutasi...">
                </div>
                <div class="topbar-actions">
                    <button class="icon-btn"><i class="fa-regular fa-bell"></i><span class="badge">2</span></button>
                    <button class="primary-btn open-modal"><i class="fa-solid fa-plus"></i> Transaksi Baru</button>
                </div>
            </header>

            <div class="content-wrapper">
                <!-- VIEW 1: DASHBOARD -->
                <div id="view-dashboard" class="view-section active">
                    <div class="header-title">
                        <h1>Cash Flow Overview</h1>
                        <p>Ringkasan posisi uang tunai, piutang, dan utang secara real-time.</p>
                    </div>

                    <div class="kpi-grid" style="grid-template-columns: repeat(3, 1fr);">
                        <div class="kpi-card glass">
                            <div class="kpi-header">
                                <h3>Total Kas & Bank (Tersedia)</h3>
                                <div class="kpi-icon blue"><i class="fa-solid fa-wallet"></i></div>
                            </div>
                            <h2 class="kpi-value">Rp 255.000.000</h2>
                            <p class="kpi-trend neutral"><i class="fa-solid fa-building-columns"></i> BCA, Mandiri, Kas Kecil</p>
                        </div>
                        <div class="kpi-card glass">
                            <div class="kpi-header">
                                <h3>Piutang Klien (Akan Masuk)</h3>
                                <div class="kpi-icon green"><i class="fa-solid fa-file-invoice-dollar"></i></div>
                            </div>
                            <h2 class="kpi-value">Rp 80.000.000</h2>
                            <p class="kpi-trend positive"><i class="fa-solid fa-clock"></i> 3 Invoice Termin menunggu dibayar</p>
                        </div>
                        <div class="kpi-card glass">
                            <div class="kpi-header">
                                <h3>Utang & Klaim (Akan Keluar)</h3>
                                <div class="kpi-icon red"><i class="fa-solid fa-receipt"></i></div>
                            </div>
                            <h2 class="kpi-value">Rp 15.000.000</h2>
                            <p class="kpi-trend negative"><i class="fa-solid fa-clock"></i> 5 Pengeluaran menunggu di-ACC</p>
                        </div>
                    </div>

                    <div class="split-screen" style="margin-top: 24px;">
                        <div class="split-half" style="flex: 2;">
                            <div class="card-header">
                                <h3>Grafik Arus Kas Bulan Ini</h3>
                            </div>
                            <div class="chart-container" style="height: 300px;">
                                <canvas id="cashflowChart"></canvas>
                            </div>
                        </div>
                        <div class="split-half" style="flex: 1;">
                            <div class="card-header">
                                <h3>⚠️ Jatuh Tempo Minggu Ini (To-Do)</h3>
                            </div>
                            <ul class="todo-list">
                                <li class="todo-item">
                                    <div>
                                        <h4 style="margin: 0; color: #fca5a5;">Invoice DP - RS Medika</h4>
                                        <p style="margin: 4px 0 0; font-size: 13px; color: var(--text-secondary);">Rp 10.000.000</p>
                                    </div>
                                    <button class="primary-btn" style="padding: 6px 12px; font-size: 12px; background: #3b82f6;">Ingatkan Klien</button>
                                </li>
                                <li class="todo-item">
                                    <div>
                                        <h4 style="margin: 0; color: #fca5a5;">Klaim Bensin - Budi</h4>
                                        <p style="margin: 4px 0 0; font-size: 13px; color: var(--text-secondary);">Rp 150.000</p>
                                    </div>
                                    <button class="primary-btn" style="padding: 6px 12px; font-size: 12px;">Review & Bayar</button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- VIEW 2: PENAGIHAN & TERMIN -->
                <div id="view-penagihan" class="view-section" style="display: none;">
                    <div class="header-title" style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h1>Daftar Penagihan & Termin (Invoicing)</h1>
                            <p>Manajemen pemecahan invoice berdasarkan termin/milestone proyek.</p>
                        </div>
                        <button class="primary-btn"><i class="fa-solid fa-plus"></i> Buat Proyek Baru</button>
                    </div>

                    <div class="table-card glass" style="padding: 24px; margin-bottom: 24px;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <h3 style="margin: 0;"><i class="fa-solid fa-folder-open" style="color: var(--primary);"></i> PROYEK: APLIKASI KASIR RS MEDIKA</h3>
                            <span class="badge-total">Total Kontrak: Rp 30.000.000</span>
                        </div>
                        <div class="termin-list">
                            <div class="termin-item">
                                <div><i class="fa-regular fa-file-lines"></i> <b>Termin 1:</b> DP Awal (30%)</div>
                                <div>Rp 9.000.000</div>
                                <div><span class="status paid">LUNAS</span></div>
                            </div>
                            <div class="termin-item">
                                <div><i class="fa-regular fa-file-lines"></i> <b>Termin 2:</b> UAT Selesai (40%)</div>
                                <div>Rp 12.000.000</div>
                                <div><span class="status negative">JATUH TEMPO</span></div>
                            </div>
                            <div class="termin-item">
                                <div><i class="fa-regular fa-file-lines"></i> <b>Termin 3:</b> Pelunasan (30%)</div>
                                <div>Rp 9.000.000</div>
                                <div><span class="status pending" style="background: rgba(255,255,255,0.1); color: var(--text-secondary);">DRAFT (Belum Ditagih)</span></div>
                            </div>
                        </div>
                        <button class="icon-btn-outline" style="margin-top: 16px;"><i class="fa-solid fa-plus"></i> Tambah Termin / Ubah Persentase</button>
                    </div>
                </div>

                <!-- VIEW 3: KLAIM & PENGELUARAN (SPLIT SCREEN) -->
                <div id="view-klaim" class="view-section" style="display: none;">
                    <div class="header-title">
                        <h1>Ajukan Klaim Pengeluaran Baru (Expense Form)</h1>
                        <p>Pisahkan pengeluaran operasional (OPEX) dan beban khusus proyek (HPP).</p>
                    </div>
                    <div class="split-screen">
                        <!-- Left: Receipt -->
                        <div class="split-half">
                            <h3>Area Bukti Pembayaran / Struk</h3>
                            <div class="receipt-preview">
                                <i class="fa-solid fa-image" style="font-size: 48px; margin-bottom: 16px;"></i>
                                <p>Tarik & Letakkan gambar struk di sini</p>
                                <button class="icon-btn-outline" style="margin-top: 16px;"><i class="fa-solid fa-upload"></i> Upload File</button>
                            </div>
                        </div>
                        <!-- Right: Form -->
                        <div class="split-half">
                            <h3>Detail Pengeluaran</h3>
                            <div style="display: flex; flex-direction: column; gap: 16px; margin-top: 16px;">
                                <div>
                                    <label style="display:block; margin-bottom: 8px; font-size: 13px; color: var(--text-secondary);">Judul / Deskripsi</label>
                                    <input type="text" class="search-box input" placeholder="Contoh: Beli Domain RS Medika" style="width: 100%; box-sizing: border-box;">
                                </div>
                                <div>
                                    <label style="display:block; margin-bottom: 8px; font-size: 13px; color: var(--text-secondary);">Kategori</label>
                                    <select class="search-box input" style="width: 100%; background: rgba(0,0,0,0.2); color: white;">
                                        <option>Software / IT Server</option>
                                        <option>Konsumsi & Transportasi</option>
                                    </select>
                                </div>
                                <div>
                                    <label style="display:block; margin-bottom: 8px; font-size: 13px; color: var(--text-secondary);">Nominal</label>
                                    <input type="text" class="search-box input" placeholder="Rp 350.000" style="width: 100%; box-sizing: border-box;">
                                </div>
                                
                                <div style="display: flex; align-items: center; justify-content: space-between; background: rgba(0,0,0,0.2); padding: 12px; border-radius: 8px; border: 1px solid var(--border-color);">
                                    <div>
                                        <b>Bebankan ke Proyek? (HPP)</b>
                                        <p style="margin: 0; font-size: 12px; color: var(--text-secondary);">Jika mati, tercatat sebagai biaya kantor (OPEX).</p>
                                    </div>
                                    <label class="toggle-switch">
                                        <input type="checkbox" id="projectToggle" checked>
                                        <span class="slider"></span>
                                    </label>
                                </div>
                                
                                <div id="projectSelectContainer">
                                    <label style="display:block; margin-bottom: 8px; font-size: 13px; color: var(--text-secondary);">Pilih Proyek Target</label>
                                    <select class="search-box input" style="width: 100%; background: rgba(0,0,0,0.2); color: white;">
                                        <option>RS Medika (Aplikasi Kasir)</option>
                                        <option>Website Company Profile X</option>
                                    </select>
                                </div>

                                <button class="primary-btn" style="margin-top: 16px; width: 100%; justify-content: center;">Submit Klaim</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- VIEW 4: REKONSILIASI BANK -->
                <div id="view-recon" class="view-section" style="display: none;">
                    <div class="header-title" style="display: flex; justify-content: space-between; align-items: center;">
                        <div>
                            <h1>Rekonsiliasi Bank (Dynamic Import & Match)</h1>
                            <p>Cocokkan mutasi bank otomatis dengan tagihan/pengeluaran sistem.</p>
                        </div>
                        <div>
                            <select class="search-box input" style="background: rgba(0,0,0,0.2); color: white; margin-right: 12px;">
                                <option>Filter: Semua Bank</option>
                                <option>BCA Operasional</option>
                            </select>
                            <button class="primary-btn"><i class="fa-solid fa-file-csv"></i> Import CSV Mutasi Baru</button>
                        </div>
                    </div>
                    
                    <div class="table-card glass" style="padding: 24px; background: rgba(139, 92, 246, 0.05);">
                        <h3 style="margin-top: 0;">SALDO BANK BCA: Rp 150.000.000 (2 Transaksi Butuh Dicocokkan)</h3>
                        
                        <div style="display: flex; gap: 24px; border-bottom: 2px solid var(--border-color); padding-bottom: 12px; margin-bottom: 16px; font-weight: bold; color: var(--text-secondary);">
                            <div style="flex: 1;">MUTASI BANK (DARI CSV)</div>
                            <div style="flex: 1;">AKSI SISTEM ERP ASTACODE</div>
                        </div>

                        <!-- Match Row 1 (Income) -->
                        <div class="tinder-card">
                            <div class="tinder-left" style="border-left: 4px solid #10b981;">
                                <h3 style="color: #10b981; margin: 0 0 8px;"><i class="fa-solid fa-arrow-down"></i> UANG MASUK: Rp 10.000.000</h3>
                                <p style="margin: 0; color: var(--text-secondary);"><i class="fa-regular fa-calendar"></i> 01 Sep 2026</p>
                                <p style="margin: 4px 0 0; font-weight: 500;">Deskripsi CSV: TRF DP RS MEDIKA</p>
                            </div>
                            <div class="tinder-right">
                                <p style="margin: 0 0 8px; color: var(--primary);"><i class="fa-solid fa-lightbulb"></i> <b>Sugesti AI Sistem:</b></p>
                                <p style="margin: 0 0 16px;">Apakah ini pembayaran <b style="color: white;">Invoice DP Proyek RS Medika (Rp 10.000.000)</b>?</p>
                                <div style="display: flex; gap: 12px;">
                                    <button class="primary-btn" style="background: #10b981;"><i class="fa-solid fa-check"></i> Ya, Match (Tandai Lunas)</button>
                                    <button class="icon-btn-outline">Cari Manual</button>
                                </div>
                            </div>
                        </div>

                        <!-- Match Row 2 (Expense) -->
                        <div class="tinder-card">
                            <div class="tinder-left" style="border-left: 4px solid #ef4444;">
                                <h3 style="color: #ef4444; margin: 0 0 8px;"><i class="fa-solid fa-arrow-up"></i> UANG KELUAR: Rp 5.000.000</h3>
                                <p style="margin: 0; color: var(--text-secondary);"><i class="fa-regular fa-calendar"></i> 02 Sep 2026</p>
                                <p style="margin: 4px 0 0; font-weight: 500;">Deskripsi CSV: TRF FREELANCER UI</p>
                            </div>
                            <div class="tinder-right">
                                <p style="margin: 0 0 8px; color: var(--text-secondary);"><i class="fa-solid fa-magnifying-glass"></i> <b>Pilih Pengeluaran (Cari Manual):</b></p>
                                <select class="search-box input" style="width: 100%; background: rgba(0,0,0,0.4); color: white; margin-bottom: 16px; padding: 12px;">
                                    <option>Tagihan Budi (Freelancer UI) - Rp 5.000.000</option>
                                    <option>Gaji Staf Andi - Rp 5.000.000</option>
                                </select>
                                <button class="primary-btn"><i class="fa-solid fa-link"></i> Konfirmasi Match Pengeluaran</button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- VIEW 5: PROFITABILITAS PROYEK -->
                <div id="view-profit" class="view-section" style="display: none;">
                    <div class="header-title">
                        <h1>Laporan Profitabilitas Proyek (Real-time P&L)</h1>
                        <p>Kalkulasi otomatis dari [Total Termin Lunas] dikurangi [Total Beban HPP Khusus Proyek].</p>
                    </div>
                    <div class="table-card glass" style="padding: 24px;">
                        <h2 style="margin-top: 0; color: var(--primary);">PROYEK: APLIKASI KASIR RS MEDIKA</h2>
                        <hr style="border-color: var(--border-color); margin: 16px 0;">
                        
                        <div style="display: flex; justify-content: space-between; font-size: 16px; margin-bottom: 8px;">
                            <span>Total Nilai Kontrak Kesepakatan:</span>
                            <b>Rp 30.000.000</b>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 16px; margin-bottom: 24px; color: #10b981;">
                            <span>Total Termin Sudah Dibayar Klien (Masuk):</span>
                            <b>Rp 15.000.000</b>
                        </div>

                        <h4 style="color: var(--text-secondary); margin-bottom: 12px;">PENGELUARAN KHUSUS PROYEK INI (HPP):</h4>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                            <span>- Bayar Freelancer UI (Budi)</span>
                            <span style="color: #ef4444;">Rp 5.000.000</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 24px;">
                            <span>- Beli Domain & Server AWS</span>
                            <span style="color: #ef4444;">Rp 2.000.000</span>
                        </div>
                        
                        <div style="background: rgba(139, 92, 246, 0.15); padding: 16px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; border: 1px solid var(--primary);">
                            <h3 style="margin: 0; color: white;">MARGIN PROYEK SEMENTARA</h3>
                            <h2 style="margin: 0; color: var(--primary);">Rp 23.000.000 (76.6%)</h2>
                        </div>
                    </div>
                </div>

                <!-- VIEW GENERIC -->
                <div id="view-generic" class="view-section" style="display: none;">
                    <div class="header-title">
                        <h1 id="generic-title">Judul Halaman</h1>
                        <p id="generic-subtitle">Data terkait manajemen operasional perusahaan.</p>
                    </div>
                    <div class="table-card glass" style="padding: 40px; text-align: center;">
                        <i class="fa-solid fa-person-digging" style="font-size: 60px; color: var(--text-secondary); margin-bottom: 20px;"></i>
                        <h2>Halaman dalam Konstruksi</h2>
                        <p style="color: var(--text-secondary);">Tampilan khusus untuk menu ini akan disesuaikan pada sprint berikutnya mengikuti panduan Cash Pool System.</p>
                    </div>
                </div>

            </div>
        </main>
    </div>

    <!-- Modals -->
    <div class="modal-overlay" id="dummyModal">
        <div class="modal-content glass">
            <div class="modal-header">
                <h2 id="modalTitle">Tambah Data Baru</h2>
                <button class="icon-btn close-modal"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="modal-body">
                <div class="form-group">
                    <label>Pilih Pihak Terkait (Vendor/Klien)</label>
                    <input type="text" class="form-control" placeholder="Ketik nama entitas...">
                </div>
                <div class="form-group" style="margin-top: 16px;">
                    <label>Nominal (Rp / USD)</label>
                    <input type="number" class="form-control" placeholder="0">
                </div>
                <div class="form-group" style="margin-top: 16px;">
                    <label>Keterangan / Memo</label>
                    <textarea class="form-control" rows="3" placeholder="Tulis rincian deskripsi transaksi..."></textarea>
                </div>
            </div>
            <div class="modal-footer" style="padding: 24px; display: flex; justify-content: flex-end; gap: 12px; border-top: 1px solid var(--border-color);">
                <button class="primary-btn close-modal" style="background: transparent; border: 1px solid var(--border-color); color: var(--text-primary);">Batal</button>
                <button class="primary-btn close-modal">Simpan Transaksi</button>
            </div>
        </div>
    </div>

    <!-- Chart.js & Logic -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Chart initialization (Bar Chart for Cashflow)
            const ctxCashflow = document.getElementById('cashflowChart').getContext('2d');
            new Chart(ctxCashflow, {
                type: 'bar',
                data: {
                    labels: ['Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep'],
                    datasets: [
                        { label: 'Uang Masuk', data: [120, 150, 180, 140, 210, 250], backgroundColor: '#10b981', borderRadius: 4 },
                        { label: 'Uang Keluar', data: [80, 100, 120, 110, 140, 160], backgroundColor: '#ef4444', borderRadius: 4 }
                    ]
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top', labels: { color: 'white' } } }, scales: { y: { grid: { color: 'rgba(255,255,255,0.1)' } }, x: { grid: { display: false } } } }
            });

            // Accordion Logic
            document.querySelectorAll('.has-submenu').forEach(item => {
                item.addEventListener('click', (e) => {
                    e.preventDefault();
                    const parent = item.closest('.nav-group');
                    const isOpen = parent.classList.contains('open');
                    document.querySelectorAll('.nav-group').forEach(g => g.classList.remove('open'));
                    if (!isOpen) parent.classList.add('open');
                });
            });

            // SPA Routing
            function switchView(targetId, title = '') {
                document.querySelectorAll('.view-section').forEach(view => view.style.display = 'none');
                const targetView = document.getElementById(targetId);
                if (targetView) {
                    targetView.style.display = 'block';
                    if (targetId === 'view-generic' && title) {
                        document.getElementById('generic-title').textContent = title;
                        document.getElementById('generic-subtitle').textContent = "Data terkait " + title;
                    }
                }
            }

            document.querySelectorAll('[data-target]').forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    document.querySelectorAll('.nav-item, .submenu-item').forEach(el => el.classList.remove('active'));
                    link.classList.add('active');
                    if (link.classList.contains('submenu-item')) {
                        link.closest('.nav-group').querySelector('.nav-item').classList.add('active');
                    }
                    switchView(link.getAttribute('data-target'), link.getAttribute('data-title') || link.textContent);
                });
            });

            // Expense Project Toggle Logic
            const projectToggle = document.getElementById('projectToggle');
            const projectSelectContainer = document.getElementById('projectSelectContainer');
            if (projectToggle && projectSelectContainer) {
                projectToggle.addEventListener('change', (e) => {
                    projectSelectContainer.style.display = e.target.checked ? 'block' : 'none';
                });
            }

            // Modal Logic
            const modal = document.getElementById('dummyModal');
            document.querySelectorAll('.open-modal').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    document.getElementById('modalTitle').textContent = btn.textContent.trim() || "Transaksi Baru";
                    modal.classList.add('active');
                });
            });

            document.querySelectorAll('.close-modal').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    const openModal = btn.closest('.modal-overlay');
                    if (openModal) openModal.classList.remove('active');
                });
            });

            document.querySelectorAll('.modal-overlay').forEach(m => {
                m.addEventListener('click', (e) => {
                    if (e.target === m) m.classList.remove('active');
                });
            });
        });
    </script>
</body>
</html>
"""
with open('/Users/a123/Documents/Modul Finance/prototype/index.html', 'w') as f:
    f.write(html_content)
