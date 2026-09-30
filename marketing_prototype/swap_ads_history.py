import re

with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Sidebar
old_sidebar_ads = '''                    <a href="#" class="nav-item" data-target="view-ads-manager">
                        <i class="fa-solid fa-money-bill-trend-up"></i> <span>Ads Optimizer</span>
                    </a>'''
new_sidebar_history = '''                    <a href="#" class="nav-item" data-target="view-content-history">
                        <i class="fa-solid fa-clock-rotate-left"></i> <span>Riwayat Konten</span>
                    </a>'''
content = content.replace(old_sidebar_ads, new_sidebar_history)

# 2. Replace Section
old_section_ads = '''                <!-- 11. ADS OPTIMIZER -->
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
                </section>'''

new_section_history = '''                <!-- 11. CONTENT HISTORY -->
                <section id="view-content-history" class="view-section">
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px;">Riwayat Konten & Arsip</h2>
                        <p style="font-size:13px; color:var(--text-tertiary);">Arsip seluruh video dan carousel yang telah berhasil dipublikasikan. Klik tautan untuk melihat langsung di platform.</p>
                    </div>
                    <div class="card">
                        <div class="card-header"><div class="card-title">Daftar Konten Terpublikasi</div></div>
                        <div class="table-responsive">
                            <table class="table">
                                <thead><tr><th>Visual</th><th>Judul Konten</th><th>Format</th><th>Tanggal Upload</th><th>Platform</th><th>Aksi</th></tr></thead>
                                <tbody>
                                    <tr>
                                        <td><div style="width:40px; height:40px; background:linear-gradient(135deg, var(--brand-primary), #60a5fa); border-radius:4px;"></div></td>
                                        <td class="font-medium">Kenapa Next.js? (Tutorial)</td>
                                        <td>Carousel (8 Slide)</td>
                                        <td>Hari ini, 10:00</td>
                                        <td><i class="fa-brands fa-instagram" style="color:#e11d48; font-size:16px;"></i> Instagram</td>
                                        <td><a href="https://instagram.com" target="_blank" class="btn btn-outline" style="font-size:11px; padding:6px 12px; text-decoration:none;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Lihat Postingan</a></td>
                                    </tr>
                                    <tr>
                                        <td><div style="width:40px; height:40px; background:linear-gradient(135deg, #0f172a, #334155); border-radius:4px;"></div></td>
                                        <td class="font-medium">React Crash Course 2026</td>
                                        <td>Short Video</td>
                                        <td>Kemarin, 15:30</td>
                                        <td><i class="fa-brands fa-tiktok" style="font-size:16px;"></i> TikTok</td>
                                        <td><a href="https://tiktok.com" target="_blank" class="btn btn-outline" style="font-size:11px; padding:6px 12px; text-decoration:none;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Lihat Postingan</a></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>'''

content = content.replace(old_section_ads, new_section_history)

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)


# Update Markdown
with open(r'd:\laragon\www\marketing_prototype\penjelasan_full_power.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

old_md_ads = '''## 4. Ad Spend & Campaign Optimizer (Robot Pengatur Uang)
**Lokasi di Aplikasi:** Sidebar -> Ads Optimizer
**Fungsi Utama:** Melakukan optimalisasi anggaran (*budget*) iklan Meta/Google secara otomatis tanpa campur tangan manusia.
*   **Mengapa Ini Penting?** Mengelola *budget* iklan A/B Testing itu melelahkan dan sering "boncos" (rugi) jika telat diawasi (misal: saat Anda sedang tidur).
*   **Cara Kerja AI:** Sistem membaca API dari Facebook/Google Ads. Jika ada dua varian iklan (A dan B) berjalan, dan dalam 24 jam iklan B menghabiskan uang tanpa hasil (*Return on Ad Spend/ROAS* < 1), sistem ini secara otomatis akan **mem-pause iklan B** dan menyalurkan sisa uangnya ke iklan A yang sedang laku. Anda akan melihat log tindakannya di dalam tabel UI dengan status *"Iklan Dihentikan (Boncos)"*.'''

new_md_history = '''## 4. Riwayat Konten & Arsip (Published History)
**Lokasi di Aplikasi:** Sidebar -> Riwayat Konten
**Fungsi Utama:** Katalog visual dari semua video dan carousel yang telah berhasil diunggah ke internet.
*   **Mengapa Ini Penting?** Anda butuh satu tempat terpusat untuk melihat hasil akhir konten (bukan sekadar log *error/success* di mesin). Anda bisa dengan cepat mereview konten lama untuk keperluan *repurpose* atau audit.
*   **Cara Kerja:** Setiap konten yang berhasil dipublikasikan oleh *Distribution Manager* akan didata di sini beserta tanggal dan jenis formatnya (Carousel/Video). Terdapat tombol **"Lihat Postingan"** yang akan langsung membuka tautan asli konten tersebut di Instagram atau TikTok, sehingga Anda bisa langsung mengecek komentar atau interaksi publik secara langsung.'''

md_content = md_content.replace(old_md_ads, new_md_history)
md_content = md_content.replace('*media buyer* (*Ads Optimizer*)', '*arsiparis konten* (*Riwayat Konten*)')

with open(r'd:\laragon\www\marketing_prototype\penjelasan_full_power.md', 'w', encoding='utf-8') as f:
    f.write(md_content)
