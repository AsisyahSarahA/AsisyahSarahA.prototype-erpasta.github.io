with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_section = '''                <!-- 11. CONTENT HISTORY -->
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

new_section = '''                <!-- 11. CONTENT HISTORY -->
                <section id="view-content-history" class="view-section">
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px;">Riwayat Konten & Arsip</h2>
                        <p style="font-size:13px; color:var(--text-tertiary);">Arsip seluruh video dan carousel yang telah berhasil dipublikasikan. Klik tautan untuk melihat langsung di platform.</p>
                    </div>
                    
                    <div style="display:flex; gap:24px; align-items:flex-start;">
                        <!-- Left: Table/List -->
                        <div class="card" style="flex:1;">
                            <div class="card-header"><div class="card-title">Daftar Konten Terpublikasi</div></div>
                            <div class="table-responsive">
                                <table class="table" style="cursor:default;">
                                    <thead><tr><th>Visual</th><th>Judul & Info</th><th>Platform</th></tr></thead>
                                    <tbody>
                                        <!-- Active Row -->
                                        <tr style="background:#f1f5f9; cursor:pointer; border-left:3px solid var(--brand-primary);">
                                            <td><div style="width:40px; height:40px; background:linear-gradient(135deg, var(--brand-primary), #60a5fa); border-radius:4px;"></div></td>
                                            <td>
                                                <strong class="font-medium" style="display:block;">Kenapa Next.js? (Tutorial)</strong>
                                                <span style="font-size:11px; color:var(--text-tertiary);">Carousel (8 Slide) &bull; Hari ini</span>
                                            </td>
                                            <td><i class="fa-brands fa-instagram" style="color:#e11d48; font-size:16px;"></i></td>
                                        </tr>
                                        <tr style="cursor:pointer; transition:0.2s;" onmouseover="this.style.background='#f8fafc';" onmouseout="this.style.background='transparent';">
                                            <td><div style="width:40px; height:40px; background:linear-gradient(135deg, #0f172a, #334155); border-radius:4px;"></div></td>
                                            <td>
                                                <strong class="font-medium" style="display:block;">React Crash Course 2026</strong>
                                                <span style="font-size:11px; color:var(--text-tertiary);">Short Video &bull; Kemarin</span>
                                            </td>
                                            <td><i class="fa-brands fa-tiktok" style="font-size:16px;"></i></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        <!-- Right: Detail Preview -->
                        <div class="card" style="width:380px; flex-shrink:0; border-top:3px solid var(--brand-primary);">
                            <div class="card-header" style="display:flex; justify-content:space-between; align-items:center; background:#fff;">
                                <div class="card-title">Detail Postingan</div>
                                <a href="https://instagram.com" target="_blank" class="btn btn-outline" style="font-size:11px; padding:6px 10px; text-decoration:none;"><i class="fa-solid fa-arrow-up-right-from-square"></i> Buka IG</a>
                            </div>
                            <div class="card-body p-0">
                                <!-- Preview Visual -->
                                <div style="background:#f8fafc; padding:24px; text-align:center; border-bottom:1px solid var(--border-light);">
                                    <div style="width:100%; aspect-ratio:1/1; background:linear-gradient(135deg, var(--brand-primary), #60a5fa); border-radius:var(--radius-md); display:flex; align-items:center; justify-content:center; color:white; font-size:20px; font-weight:700; box-shadow:var(--shadow-soft);">
                                        Kenapa Next.js?
                                    </div>
                                </div>
                                <!-- Stats -->
                                <div style="padding:20px;">
                                    <h3 style="font-size:13px; font-weight:600; margin-bottom:16px; color:var(--text-secondary); text-transform:uppercase; letter-spacing:0.5px;">Performa Saat Ini (Live)</h3>
                                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:24px;">
                                        <div style="background:#f1f5f9; padding:16px 12px; border-radius:var(--radius-sm); text-align:center;">
                                            <i class="fa-solid fa-eye" style="color:var(--text-tertiary); margin-bottom:8px; font-size:16px;"></i>
                                            <div style="font-size:18px; font-weight:700; color:var(--text-primary); letter-spacing:-0.5px;">12.4K</div>
                                            <div style="font-size:11px; font-weight:500; color:var(--text-secondary); margin-top:2px;">Views</div>
                                        </div>
                                        <div style="background:#fef2f2; padding:16px 12px; border-radius:var(--radius-sm); text-align:center;">
                                            <i class="fa-solid fa-heart" style="color:#e11d48; margin-bottom:8px; font-size:16px;"></i>
                                            <div style="font-size:18px; font-weight:700; color:var(--text-primary); letter-spacing:-0.5px;">1,204</div>
                                            <div style="font-size:11px; font-weight:500; color:#e11d48; margin-top:2px;">Likes</div>
                                        </div>
                                        <div style="background:#eff6ff; padding:16px 12px; border-radius:var(--radius-sm); text-align:center;">
                                            <i class="fa-solid fa-comment" style="color:var(--brand-primary); margin-bottom:8px; font-size:16px;"></i>
                                            <div style="font-size:18px; font-weight:700; color:var(--text-primary); letter-spacing:-0.5px;">89</div>
                                            <div style="font-size:11px; font-weight:500; color:var(--brand-primary); margin-top:2px;">Komentar</div>
                                        </div>
                                        <div style="background:#fefce8; padding:16px 12px; border-radius:var(--radius-sm); text-align:center;">
                                            <i class="fa-solid fa-bookmark" style="color:#ca8a04; margin-bottom:8px; font-size:16px;"></i>
                                            <div style="font-size:18px; font-weight:700; color:var(--text-primary); letter-spacing:-0.5px;">342</div>
                                            <div style="font-size:11px; font-weight:500; color:#ca8a04; margin-top:2px;">Saves</div>
                                        </div>
                                    </div>
                                    <!-- Recent Comments -->
                                    <h3 style="font-size:13px; font-weight:600; margin-bottom:12px; color:var(--text-secondary); text-transform:uppercase; letter-spacing:0.5px;">Komentar Terbaru</h3>
                                    <div style="font-size:13px; color:var(--text-secondary); border-left:3px solid var(--border-light); padding-left:12px; margin-bottom:12px; line-height:1.4;">
                                        <strong style="color:var(--text-primary);">@dev_anjay</strong> Wah gila sih Next.js 14 emang ngebut parah 🔥🔥
                                    </div>
                                    <div style="font-size:13px; color:var(--text-secondary); border-left:3px solid var(--border-light); padding-left:12px; line-height:1.4;">
                                        <strong style="color:var(--text-primary);">@react_noob</strong> Masih bingung bedanya sama Vite bang, bahas dong!
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>'''

content = content.replace(old_section, new_section)

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
