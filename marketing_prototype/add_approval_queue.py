import re

file_path = 'd:/laragon/www/marketing_prototype/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add sidebar menu item
sidebar_menu_pattern = r'(<a href="#" class="nav-item" data-target="view-ai-engine">\s*<i class="fa-solid fa-wand-magic-sparkles"></i> <span>AI Content Engine</span>\s*</a>)'
sidebar_menu_replacement = r'\1\n                    <a href="#" class="nav-item" data-target="view-approval-queue">\n                        <i class="fa-solid fa-list-check"></i> <span>Antrean Persetujuan</span>\n                    </a>'

content = re.sub(sidebar_menu_pattern, sidebar_menu_replacement, content)

# 2. Add the view section
# We'll inject it right before <!-- 2. AI CONTENT ENGINE -->
view_section_html = '''
                <!-- NEW SECTION: ANTREAN PERSETUJUAN (DEDICATED MENU) -->
                <section id="view-approval-queue" class="view-section">
                    <div style="margin-bottom: 24px; display:flex; justify-content:space-between; align-items:flex-end;">
                        <div>
                            <h2 style="font-size:20px; font-weight:600;">Antrean Persetujuan (Approval Queue)</h2>
                            <p style="font-size:13px; color:var(--text-tertiary); margin-top:4px;">Tinjau konten yang dihasilkan AI. AI akan otomatis menyetujui konten dengan bobot kualitas dan edukasi tinggi.</p>
                        </div>
                        <div style="display:flex; align-items:center; gap:10px;">
                            <span style="font-size:12px; font-weight:600; color:var(--text-secondary);">AI Auto-Approve Master:</span>
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
                                <select class="form-control" style="width:140px; font-size:12px; height:32px; padding:0 12px;"><option>Semua Platform</option><option>Instagram</option><option>TikTok</option></select>
                                <select class="form-control" style="width:140px; font-size:12px; height:32px; padding:0 12px;"><option>Status AI</option><option>Butuh Review</option><option>Auto-Approved</option></select>
                            </div>
                            <div style="position:relative;">
                                <i class="fa-solid fa-magnifying-glass" style="position:absolute; left:10px; top:50%; transform:translateY(-50%); color:var(--text-tertiary); font-size:12px;"></i>
                                <input type="text" placeholder="Cari konten..." style="height:32px; padding:0 12px 0 32px; font-size:12px; border:1px solid var(--border-light); border-radius:6px; outline:none; width:220px;">
                            </div>
                        </div>

                        <div class="table-responsive" style="background:#fff;">
                            <table class="table" style="width:100%; border-collapse:collapse; text-align:left; font-size:13px;">
                                <thead style="background:#f8fafc; color:var(--text-tertiary); font-size:11px; text-transform:uppercase; letter-spacing:0.5px;">
                                    <tr>
                                        <th style="padding:12px 24px; border-bottom:1px solid var(--border-light);">Konten</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light);">Platform</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light);">Bobot Kebagusan</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light);">Nilai Edukasi</th>
                                        <th style="padding:12px 16px; border-bottom:1px solid var(--border-light);">Keputusan AI</th>
                                        <th style="padding:12px 24px; border-bottom:1px solid var(--border-light); text-align:right;">Aksi</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <!-- Auto Approved -->
                                    <tr style="border-bottom:1px solid var(--border-light); background:#f0fdf4;">
                                        <td style="padding:12px 24px; font-weight:500; color:var(--brand-primary);">5 Prinsip Laravel untuk Pemula</td>
                                        <td style="padding:12px 16px;"><i class="fa-brands fa-instagram" style="color:#e11d48;"></i> Instagram</td>
                                        <td style="padding:12px 16px;"><span style="color:#16a34a; font-weight:600;">95/100</span> <i class="fa-solid fa-caret-up" style="color:#16a34a;"></i></td>
                                        <td style="padding:12px 16px;"><span style="color:#16a34a; font-weight:600;">90/100</span> <i class="fa-solid fa-caret-up" style="color:#16a34a;"></i></td>
                                        <td style="padding:12px 16px;"><span class="status-badge" style="background:#dcfce7; color:#166534;"><i class="fa-solid fa-robot"></i> AUTO-APPROVED</span></td>
                                        <td style="padding:12px 24px; text-align:right;">
                                            <span style="font-size:11px; color:var(--text-tertiary); font-weight:500;"><i class="fa-solid fa-check-double"></i> Diproses</span>
                                        </td>
                                    </tr>
                                    <!-- Needs Review 1 -->
                                    <tr style="border-bottom:1px solid var(--border-light); background:#fffbeb;">
                                        <td style="padding:12px 24px; font-weight:500; color:var(--brand-primary);">Trend: AI Agents vs Framework</td>
                                        <td style="padding:12px 16px;"><i class="fa-brands fa-tiktok" style="color:#000;"></i> TikTok</td>
                                        <td style="padding:12px 16px;"><span style="color:#d97706; font-weight:600;">72/100</span></td>
                                        <td style="padding:12px 16px;"><span style="color:#d97706; font-weight:600;">68/100</span></td>
                                        <td style="padding:12px 16px;"><span class="status-badge badge-review" style="background:#fef3c7; color:#92400e;">BUTUH REVIEW MANUSIA</span></td>
                                        <td style="padding:12px 24px; text-align:right;">
                                            <button class="btn btn-outline" style="padding:4px 8px; font-size:11px; height:auto; margin-right:4px; color:#16a34a; border-color:#16a34a; background:#fff;" title="Setujui"><i class="fa-solid fa-check"></i></button>
                                            <button class="btn btn-outline" style="padding:4px 8px; font-size:11px; height:auto; color:#e11d48; border-color:#e11d48; background:#fff;" title="Tolak / Revisi"><i class="fa-solid fa-xmark"></i></button>
                                        </td>
                                    </tr>
                                    <!-- Needs Review 2 (Low Education) -->
                                    <tr style="border-bottom:1px solid var(--border-light); background:#fffbeb;">
                                        <td style="padding:12px 24px; font-weight:500; color:var(--brand-primary);">Meme Kodingan Error di Produksi</td>
                                        <td style="padding:12px 16px;"><i class="fa-brands fa-instagram" style="color:#e11d48;"></i> Instagram</td>
                                        <td style="padding:12px 16px;"><span style="color:#d97706; font-weight:600;">80/100</span></td>
                                        <td style="padding:12px 16px;"><span style="color:#dc2626; font-weight:600;">45/100</span> <i class="fa-solid fa-caret-down" style="color:#dc2626;"></i></td>
                                        <td style="padding:12px 16px;"><span class="status-badge badge-review" style="background:#fef3c7; color:#92400e;">BUTUH REVIEW MANUSIA</span></td>
                                        <td style="padding:12px 24px; text-align:right;">
                                            <button class="btn btn-outline" style="padding:4px 8px; font-size:11px; height:auto; margin-right:4px; color:#16a34a; border-color:#16a34a; background:#fff;" title="Setujui"><i class="fa-solid fa-check"></i></button>
                                            <button class="btn btn-outline" style="padding:4px 8px; font-size:11px; height:auto; color:#e11d48; border-color:#e11d48; background:#fff;" title="Tolak / Revisi"><i class="fa-solid fa-xmark"></i></button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>
'''

content = content.replace('<!-- 2. AI CONTENT ENGINE -->', view_section_html + '\n                <!-- 2. AI CONTENT ENGINE -->', 1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Approval Queue View injected successfully!")
