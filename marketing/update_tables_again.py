import re

with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Social Listening section
pattern_social = re.compile(r'<!-- 9\. SOCIAL LISTENING -->\s*<section id="view-social-listening" class="view-section">.*?</section>', re.DOTALL)

new_social = '''<!-- 9. SOCIAL LISTENING -->
                <section id="view-social-listening" class="view-section">
                    <div style="margin-bottom: 24px; display:flex; justify-content:space-between; align-items:flex-end;">
                        <div>
                            <h2 style="font-size:20px; font-weight:600;">Social Listening & Competitors</h2>
                            <p style="font-size:13px; color:var(--text-tertiary); margin-top:4px;">Pantau kompetitor secara real-time dan biarkan AI mencari peluang konten.</p>
                        </div>
                        <button class="btn btn-primary" style="font-size:13px; padding:8px 16px;"><i class="fa-solid fa-plus"></i> Tambah Kompetitor</button>
                    </div>

                    <div class="card" style="box-shadow:0 4px 12px rgba(0,0,0,0.05); border:1px solid var(--border-light); border-radius:8px; overflow:hidden;">
                        <!-- Filter Bar -->
                        <div style="padding:16px 24px; border-bottom:1px solid var(--border-light); display:flex; justify-content:space-between; align-items:center; background:#fff;">
                            <div style="display:flex; gap:12px;">
                                <select class="form-control" style="width:130px; font-size:12px; height:32px; padding:0 12px;"><option>Semua Platform</option><option>Instagram</option><option>TikTok</option></select>
                                <select class="form-control" style="width:120px; font-size:12px; height:32px; padding:0 12px;"><option>Status Trend</option><option>Viral (Naik)</option><option>Turun</option></select>
                                <button class="btn btn-outline" style="height:32px; font-size:12px; padding:0 12px; color:var(--text-secondary);"><i class="fa-solid fa-sliders"></i> Semua Filter</button>
                            </div>
                            <div style="display:flex; gap:8px;">
                                <button class="btn btn-outline" style="height:32px; width:32px; padding:0; display:flex; align-items:center; justify-content:center; color:var(--text-secondary);"><i class="fa-solid fa-pen"></i></button>
                                <button class="btn btn-outline" style="height:32px; width:32px; padding:0; display:flex; align-items:center; justify-content:center; color:var(--status-danger);"><i class="fa-regular fa-trash-can"></i></button>
                            </div>
                        </div>

                        <div class="table-responsive" style="background:#fff;">
                            <table class="table" style="width:100%; border-collapse:collapse; text-align:left; font-size:13px;">
                                <thead style="background:#f8fafc; color:var(--text-tertiary); font-size:11px; text-transform:uppercase; letter-spacing:0.5px;">
                                    <tr>
                                        <th style="padding:12px 24px; border-bottom:1px solid var(--border-light); width:40px;"><input type="checkbox"></th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">KOMPETITOR</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">TOPIK VIRAL TERBARU</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">VIEWS/ENGAGEMENT</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">REKOMENDASI AI</th>
                                        <th style="padding:12px 24px; border-bottom:1px solid var(--border-light); font-weight:600; text-align:right;">AKSI</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom:1px solid var(--border-light); background:#fefce8;">
                                        <td style="padding:12px 24px;"><input type="checkbox"></td>
                                        <td style="padding:12px 16px; display:flex; align-items:center; gap:12px;">
                                            <div style="width:32px; height:32px; background:#e11d48; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">K</div>
                                            <div>
                                                <strong style="color:var(--text-primary); font-weight:600; display:block;">@KompetitorA</strong>
                                                <span style="color:var(--text-tertiary); font-size:11px;">Instagram</span>
                                            </div>
                                        </td>
                                        <td style="padding:12px 16px; color:var(--text-secondary);">"Kesalahan Fatal Pemula di Next.js"</td>
                                        <td style="padding:12px 16px; color:var(--status-danger); font-weight:600;">1.2M <i class="fa-solid fa-arrow-trend-up" style="font-size:10px;"></i></td>
                                        <td style="padding:12px 16px;"><span class="status-badge badge-warning" style="background:#fef9c3; color:#a16207;">⚡ BUAT TANDINGAN</span></td>
                                        <td style="padding:12px 24px; text-align:right;">
                                            <button class="btn btn-primary" style="font-size:11px; padding:4px 12px; height:auto;">Eksekusi AI</button>
                                        </td>
                                    </tr>
                                    <tr style="border-bottom:1px solid var(--border-light);">
                                        <td style="padding:12px 24px;"><input type="checkbox"></td>
                                        <td style="padding:12px 16px; display:flex; align-items:center; gap:12px;">
                                            <div style="width:32px; height:32px; background:#000; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">T</div>
                                            <div>
                                                <strong style="color:var(--text-primary); font-weight:600; display:block;">@TokoTech</strong>
                                                <span style="color:var(--text-tertiary); font-size:11px;">TikTok</span>
                                            </div>
                                        </td>
                                        <td style="padding:12px 16px; color:var(--text-secondary);">"Review Macbook M3 2026"</td>
                                        <td style="padding:12px 16px; color:var(--text-primary); font-weight:500;">450K <i class="fa-solid fa-minus" style="font-size:10px; color:var(--text-tertiary);"></i></td>
                                        <td style="padding:12px 16px;"><span class="status-badge" style="background:#f1f5f9; color:var(--text-secondary);">Pantau Dulu</span></td>
                                        <td style="padding:12px 24px; text-align:right;">
                                            <button class="btn btn-outline" style="font-size:11px; padding:4px 12px; height:auto;">Lihat Data</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>'''
content = pattern_social.sub(new_social, content)

# 2. Update Inbox section
pattern_inbox = re.compile(r'<!-- 10\. OMNICHANNEL INBOX -->\s*<section id="view-inbox" class="view-section">.*?</section>', re.DOTALL)

new_inbox = '''<!-- 10. OMNICHANNEL INBOX -->
                <section id="view-inbox" class="view-section">
                    <div style="margin-bottom: 24px; display:flex; justify-content:space-between; align-items:flex-end;">
                        <div>
                            <h2 style="font-size:20px; font-weight:600;">Omnichannel Inbox (Auto-Reply AI)</h2>
                            <p style="font-size:13px; color:var(--text-tertiary); margin-top:4px;">AI otomatis membalas DM & komentar berdasarkan Knowledge Base (Data Produk).</p>
                        </div>
                        <div style="display:flex; align-items:center; gap:10px;">
                            <span style="font-size:12px; font-weight:600; color:var(--text-secondary);">AI Auto-Reply Master:</span>
                            <label class="switch">
                                <input type="checkbox" checked>
                                <span class="slider"></span>
                            </label>
                        </div>
                    </div>

                    <div class="card" style="box-shadow:0 4px 12px rgba(0,0,0,0.05); border:1px solid var(--border-light); border-radius:8px; overflow:hidden;">
                        <!-- Filter Bar -->
                        <div style="padding:16px 24px; border-bottom:1px solid var(--border-light); display:flex; justify-content:space-between; align-items:center; background:#fff;">
                            <div style="display:flex; gap:12px;">
                                <select class="form-control" style="width:130px; font-size:12px; height:32px; padding:0 12px;"><option>Platform</option><option>IG DM</option><option>TikTok Chat</option></select>
                                <select class="form-control" style="width:120px; font-size:12px; height:32px; padding:0 12px;"><option>Status AI</option><option>Terbalas Otomatis</option><option>Butuh Manusia</option></select>
                                <button class="btn btn-outline" style="height:32px; font-size:12px; padding:0 12px; color:var(--text-secondary);"><i class="fa-solid fa-sliders"></i> Semua Filter</button>
                            </div>
                            <div style="display:flex; gap:8px;">
                                <button class="btn btn-outline" style="height:32px; width:32px; padding:0; display:flex; align-items:center; justify-content:center; color:var(--text-secondary);"><i class="fa-solid fa-check-double"></i></button>
                            </div>
                        </div>

                        <div class="table-responsive" style="background:#fff;">
                            <table class="table" style="width:100%; border-collapse:collapse; text-align:left; font-size:13px;">
                                <thead style="background:#f8fafc; color:var(--text-tertiary); font-size:11px; text-transform:uppercase; letter-spacing:0.5px;">
                                    <tr>
                                        <th style="padding:12px 24px; border-bottom:1px solid var(--border-light); width:40px;"><input type="checkbox"></th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">PELANGGAN</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">PESAN TERAKHIR</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">TINDAKAN AI</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">WAKTU</th>
                                        <th style="padding:12px 24px; border-bottom:1px solid var(--border-light); font-weight:600; text-align:right;">AKSI</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr style="border-bottom:1px solid var(--border-light); background:#f0fdf4;">
                                        <td style="padding:12px 24px;"><input type="checkbox"></td>
                                        <td style="padding:12px 16px; display:flex; align-items:center; gap:12px;">
                                            <div style="width:32px; height:32px; background:#3b82f6; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">B</div>
                                            <div>
                                                <strong style="color:var(--text-primary); font-weight:600; display:block;">Budi Santoso</strong>
                                                <span style="color:var(--text-tertiary); font-size:11px;"><i class="fa-brands fa-instagram" style="color:#e11d48;"></i> Instagram DM</span>
                                            </div>
                                        </td>
                                        <td style="padding:12px 16px; color:var(--text-secondary); max-width:250px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">"Min, promo yang kemaren masih ada gak ya?"</td>
                                        <td style="padding:12px 16px;"><span class="status-badge badge-done" style="background:#dcfce7; color:#166534;"><i class="fa-solid fa-robot"></i> TERBALAS OTOMATIS</span></td>
                                        <td style="padding:12px 16px; color:var(--text-tertiary);">2 mnt lalu</td>
                                        <td style="padding:12px 24px; text-align:right;">
                                            <button class="btn btn-outline" style="font-size:11px; padding:4px 12px; height:auto;">Lihat Chat</button>
                                        </td>
                                    </tr>
                                    <tr style="border-bottom:1px solid var(--border-light);">
                                        <td style="padding:12px 24px;"><input type="checkbox"></td>
                                        <td style="padding:12px 16px; display:flex; align-items:center; gap:12px;">
                                            <div style="width:32px; height:32px; background:#10b981; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">S</div>
                                            <div>
                                                <strong style="color:var(--text-primary); font-weight:600; display:block;">Siska Media</strong>
                                                <span style="color:var(--text-tertiary); font-size:11px;"><i class="fa-brands fa-tiktok"></i> TikTok Comment</span>
                                            </div>
                                        </td>
                                        <td style="padding:12px 16px; color:var(--text-secondary); max-width:250px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">"Kerja sama endorsement kak, bisa cek ratecard?"</td>
                                        <td style="padding:12px 16px;"><span class="status-badge badge-review" style="background:#fee2e2; color:#b91c1c;"><i class="fa-solid fa-user-tie"></i> BUTUH MANUSIA</span></td>
                                        <td style="padding:12px 16px; color:var(--text-tertiary);">15 mnt lalu</td>
                                        <td style="padding:12px 24px; text-align:right;">
                                            <button class="btn btn-primary" style="font-size:11px; padding:4px 12px; height:auto;">Balas Manual</button>
                                        </td>
                                    </tr>
                                    <tr style="border-bottom:1px solid var(--border-light); background:#f0fdf4;">
                                        <td style="padding:12px 24px;"><input type="checkbox"></td>
                                        <td style="padding:12px 16px; display:flex; align-items:center; gap:12px;">
                                            <div style="width:32px; height:32px; background:#8b5cf6; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:bold; font-size:14px;">A</div>
                                            <div>
                                                <strong style="color:var(--text-primary); font-weight:600; display:block;">Agus Setiawan</strong>
                                                <span style="color:var(--text-tertiary); font-size:11px;"><i class="fa-brands fa-instagram" style="color:#e11d48;"></i> Instagram DM</span>
                                            </div>
                                        </td>
                                        <td style="padding:12px 16px; color:var(--text-secondary); max-width:250px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">"Barang udh sampai min, makasih ya!"</td>
                                        <td style="padding:12px 16px;"><span class="status-badge badge-done" style="background:#dcfce7; color:#166534;"><i class="fa-solid fa-robot"></i> TERBALAS OTOMATIS</span></td>
                                        <td style="padding:12px 16px; color:var(--text-tertiary);">1 jam lalu</td>
                                        <td style="padding:12px 24px; text-align:right;">
                                            <button class="btn btn-outline" style="font-size:11px; padding:4px 12px; height:auto;">Lihat Chat</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>'''
content = pattern_inbox.sub(new_inbox, content)

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
