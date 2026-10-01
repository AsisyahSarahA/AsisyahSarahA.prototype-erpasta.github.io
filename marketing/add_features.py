import re

with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Sidebar
old_system_group = r'''                <div class="nav-group">
                    <span class="nav-label">SISTEM</span>
                    <a href="#" class="nav-item" data-target="view-analytics">
                        <i class="fa-solid fa-chart-pie"></i> <span>Analitik & Laporan</span>
                    </a>
                    <a href="#" class="nav-item" data-target="view-settings">
                        <i class="fa-solid fa-sliders"></i> <span>Pengaturan & Rules</span>
                    </a>
                </div>'''

new_system_group = '''                <div class="nav-group">
                    <span class="nav-label">FULL POWER (PRO)</span>
                    <a href="#" class="nav-item" data-target="view-asset-library">
                        <i class="fa-regular fa-folder-open"></i> <span>Brand Asset Library</span>
                    </a>
                    <a href="#" class="nav-item" data-target="view-social-listening">
                        <i class="fa-solid fa-satellite-dish"></i> <span>Social Listening</span>
                    </a>
                    <a href="#" class="nav-item" data-target="view-inbox">
                        <i class="fa-regular fa-comments"></i> <span>Omnichannel Inbox</span>
                    </a>
                    <a href="#" class="nav-item" data-target="view-ads-manager">
                        <i class="fa-solid fa-money-bill-trend-up"></i> <span>Ads Optimizer</span>
                    </a>
                </div>

                <div class="nav-group">
                    <span class="nav-label">SISTEM</span>
                    <a href="#" class="nav-item" data-target="view-analytics">
                        <i class="fa-solid fa-chart-pie"></i> <span>Analitik & Laporan</span>
                    </a>
                    <a href="#" class="nav-item" data-target="view-team">
                        <i class="fa-solid fa-users-gear"></i> <span>Manajemen Tim</span>
                    </a>
                    <a href="#" class="nav-item" data-target="view-settings">
                        <i class="fa-solid fa-sliders"></i> <span>Pengaturan & Rules</span>
                    </a>
                </div>'''

content = content.replace(old_system_group, new_system_group)

# 2. Add New Views
new_views = '''
                <!-- 8. BRAND ASSET LIBRARY -->
                <section id="view-asset-library" class="view-section">
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px;">Brand Asset Library</h2>
                        <p style="font-size:13px; color:var(--text-tertiary);">Pusat media dan identitas brand. AI akan menggunakan aset ini agar desain selalu konsisten.</p>
                    </div>
                    <div class="grid-3">
                        <div class="card" style="display:flex; flex-direction:column; align-items:center; text-align:center;">
                            <i class="fa-solid fa-swatchbook" style="font-size:32px; color:var(--brand-primary); margin-bottom:12px;"></i>
                            <strong style="font-size:14px;">Warna & Tipografi</strong>
                            <p style="font-size:12px; color:var(--text-secondary); margin-top:4px;">Primary: #2563eb, Font: Inter</p>
                        </div>
                        <div class="card" style="display:flex; flex-direction:column; align-items:center; text-align:center;">
                            <i class="fa-solid fa-image" style="font-size:32px; color:var(--status-success); margin-bottom:12px;"></i>
                            <strong style="font-size:14px;">Logo & Watermark</strong>
                            <p style="font-size:12px; color:var(--text-secondary); margin-top:4px;">12 aset tersedia</p>
                        </div>
                        <div class="card" style="display:flex; flex-direction:column; align-items:center; text-align:center; border:2px dashed var(--brand-primary); background:rgba(37,99,235,0.05);">
                            <i class="fa-solid fa-brain" style="font-size:32px; color:var(--brand-primary); margin-bottom:12px;"></i>
                            <strong style="font-size:14px;">AI Model Status</strong>
                            <span class="status-badge badge-done" style="margin-top:8px;">TRAINED (100%)</span>
                        </div>
                    </div>
                </section>

                <!-- 9. SOCIAL LISTENING -->
                <section id="view-social-listening" class="view-section">
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px;">Social Listening & Competitors</h2>
                        <p style="font-size:13px; color:var(--text-tertiary);">Pantau kompetitor secara real-time dan biarkan AI mencari peluang konten.</p>
                    </div>
                    <div class="card">
                        <div class="card-header"><div class="card-title">Live Competitor Feed</div></div>
                        <div class="card-body p-0">
                            <ul class="perf-list" style="padding:0 24px;">
                                <li>
                                    <div>
                                        <strong style="color:var(--status-danger);">@KompetitorA</strong> baru saja memposting video viral (1.2M Views).
                                        <p style="font-size:12px; color:var(--text-tertiary); margin-top:4px;">Topik: "Kesalahan Fatal Pemula di Next.js"</p>
                                    </div>
                                    <button class="btn btn-primary" style="font-size:11px;">Minta AI Buat Tandingan</button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- 10. OMNICHANNEL INBOX -->
                <section id="view-inbox" class="view-section">
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px;">Omnichannel Inbox</h2>
                        <p style="font-size:13px; color:var(--text-tertiary);">Satu kotak masuk untuk semua DM dan komentar. AI akan menyiapkan draf balasan.</p>
                    </div>
                    <div class="grid-2">
                        <div class="card">
                            <div class="card-header"><div class="card-title">Pesan Masuk (Unread)</div></div>
                            <div class="card-body p-0">
                                <div style="padding:16px; border-bottom:1px solid var(--border-light); background:var(--bg-hover);">
                                    <strong style="font-size:13px;"><i class="fa-brands fa-instagram" style="color:#e11d48;"></i> Budi Santoso</strong>
                                    <p style="font-size:12px; margin-top:4px;">"Min, promo yang kemaren masih ada gak ya?"</p>
                                </div>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card-body">
                                <div style="background:var(--bg-input); padding:16px; border-radius:var(--radius-md); margin-bottom:16px;">
                                    <strong style="font-size:11px; color:var(--brand-primary);"><i class="fa-solid fa-robot"></i> Draf Balasan AI:</strong>
                                    <p style="font-size:13px; margin-top:8px;">"Halo Kak Budi! 👋 Promo bulan lalu sudah berakhir, tapi jangan khawatir, kita punya diskon spesial 20% khusus buat Kakak hari ini. Cek link di bio ya!"</p>
                                </div>
                                <button class="btn btn-primary w-100">Kirim Balasan Ini</button>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- 11. ADS OPTIMIZER -->
                <section id="view-ads-manager" class="view-section">
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px;">Ad Spend & Campaign Optimizer</h2>
                        <p style="font-size:13px; color:var(--text-tertiary);">AI otomatis memindahkan budget dari iklan yang boncos ke iklan yang menguntungkan.</p>
                    </div>
                    <div class="card">
                        <div class="card-header"><div class="card-title">Meta Ads Optimization</div></div>
                        <div class="table-responsive">
                            <table class="table">
                                <thead><tr><th>Kampanye</th><th>Budget Asli</th><th>Tindakan AI (Auto)</th><th>Hasil ROAS</th></tr></thead>
                                <tbody>
                                    <tr>
                                        <td class="font-medium">Promo Q4 (Visual A)</td>
                                        <td>Rp 5.000.000</td>
                                        <td><span class="pill-event pill-green"><i class="fa-solid fa-arrow-trend-up"></i> Budget Ditambah +30%</span></td>
                                        <td><strong style="color:var(--status-success);">4.5x</strong></td>
                                    </tr>
                                    <tr>
                                        <td class="font-medium">Promo Q4 (Visual B)</td>
                                        <td>Rp 5.000.000</td>
                                        <td><span class="pill-event pill-orange"><i class="fa-solid fa-pause"></i> Iklan Dihentikan (Boncos)</span></td>
                                        <td><strong style="color:var(--status-danger);">0.8x</strong></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <!-- 12. TEAM MANAGEMENT -->
                <section id="view-team" class="view-section">
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px;">Manajemen Tim & Kolaborasi</h2>
                        <p style="font-size:13px; color:var(--text-tertiary);">Atur siapa yang bisa menyetujui konten dan siapa yang hanya bisa membuat draf.</p>
                    </div>
                    <div class="card">
                        <div class="card-header"><div class="card-title">Daftar Anggota</div><button class="btn btn-primary">Undang Tim</button></div>
                        <div class="table-responsive">
                            <table class="table">
                                <thead><tr><th>Nama</th><th>Peran (Role)</th><th>Akses Approval</th></tr></thead>
                                <tbody>
                                    <tr>
                                        <td class="font-medium">Asta Manager</td>
                                        <td>Admin / Manajer</td>
                                        <td><span class="status-badge badge-done">FULL AKSES</span></td>
                                    </tr>
                                    <tr>
                                        <td class="font-medium">Joko (Freelance)</td>
                                        <td>Copywriter</td>
                                        <td><span class="status-badge badge-review">HANYA DRAF</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>
'''

content = content.replace('            </div>\n        </main>', new_views + '\n            </div>\n        </main>')

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
