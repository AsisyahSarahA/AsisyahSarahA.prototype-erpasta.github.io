with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# We will use regex to replace everything between <div id="history-list-view"> and <!-- 2. DETAIL VIEW
pattern = re.compile(r'<div id="history-list-view">.*?<!-- 2\. DETAIL VIEW', re.DOTALL)

new_list_view = '''<div id="history-list-view">
                        <div style="margin-bottom: 24px; display:flex; justify-content:space-between; align-items:flex-end;">
                            <div>
                                <h2 style="font-size:20px; font-weight:600;">Riwayat Konten & Arsip</h2>
                                <p style="font-size:13px; color:var(--text-tertiary); margin-top:4px;">Arsip seluruh video dan carousel yang telah berhasil dipublikasikan.</p>
                            </div>
                            <button class="btn btn-primary" style="font-size:13px; padding:8px 16px;"><i class="fa-solid fa-plus"></i> Tambah Manual</button>
                        </div>
                        
                        <div class="card" style="box-shadow:0 4px 12px rgba(0,0,0,0.05); border:1px solid var(--border-light); border-radius:8px; overflow:hidden;">
                            
                            <!-- Filter Bar -->
                            <div style="padding:16px 24px; border-bottom:1px solid var(--border-light); display:flex; justify-content:space-between; align-items:center; background:#fff;">
                                <div style="display:flex; gap:12px;">
                                    <select class="form-control" style="width:130px; font-size:12px; height:32px; padding:0 12px;"><option>Platform</option><option>Instagram</option><option>TikTok</option></select>
                                    <select class="form-control" style="width:120px; font-size:12px; height:32px; padding:0 12px;"><option>Format</option><option>Video</option><option>Carousel</option></select>
                                    <select class="form-control" style="width:120px; font-size:12px; height:32px; padding:0 12px;"><option>Bulan Ini</option><option>Bulan Lalu</option></select>
                                    <button class="btn btn-outline" style="height:32px; font-size:12px; padding:0 12px; color:var(--text-secondary);"><i class="fa-solid fa-sliders"></i> Semua Filter</button>
                                </div>
                                <div style="display:flex; gap:8px;">
                                    <button class="btn btn-outline" style="height:32px; width:32px; padding:0; display:flex; align-items:center; justify-content:center; color:var(--text-secondary);"><i class="fa-solid fa-pen"></i></button>
                                    <button class="btn btn-outline" style="height:32px; width:32px; padding:0; display:flex; align-items:center; justify-content:center; color:var(--status-danger);"><i class="fa-regular fa-trash-can"></i></button>
                                </div>
                            </div>

                            <!-- Table -->
                            <div class="table-responsive" style="background:#fff;">
                                <table class="table" style="cursor:pointer; width:100%; border-collapse:collapse; text-align:left; font-size:13px;">
                                    <thead style="background:#f8fafc; color:var(--text-tertiary); font-size:11px; text-transform:uppercase; letter-spacing:0.5px;">
                                        <tr>
                                            <th style="padding:12px 24px; border-bottom:1px solid var(--border-light); width:40px;"><input type="checkbox"></th>
                                            <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">ID</th>
                                            <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">KONTEN</th>
                                            <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">PLATFORM</th>
                                            <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">VIEWS</th>
                                            <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">ENGAGEMENT</th>
                                            <th style="padding:12px 16px; border-bottom:1px solid var(--border-light); font-weight:600;">STATUS</th>
                                            <th style="padding:12px 24px; border-bottom:1px solid var(--border-light); font-weight:600; text-align:right;">AKSI</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr onclick="document.getElementById('history-list-view').style.display='none'; document.getElementById('history-detail-view').style.display='block';" onmouseover="this.style.background='#f1f5f9';" onmouseout="this.style.background='transparent';" style="border-bottom:1px solid var(--border-light); transition:0.1s;">
                                            <td style="padding:12px 24px;" onclick="event.stopPropagation();"><input type="checkbox"></td>
                                            <td style="padding:12px 16px; color:var(--text-secondary);">#447</td>
                                            <td style="padding:12px 16px; display:flex; align-items:center; gap:12px;">
                                                <div style="width:32px; height:32px; background:linear-gradient(135deg, var(--brand-primary), #60a5fa); border-radius:4px; flex-shrink:0;"></div>
                                                <div>
                                                    <strong style="color:var(--text-primary); font-weight:600; display:block;">Kenapa Next.js? (Tutorial)</strong>
                                                    <span style="color:var(--text-tertiary); font-size:11px;">Oleh Asta Marketing</span>
                                                </div>
                                            </td>
                                            <td style="padding:12px 16px; color:var(--text-secondary);"><i class="fa-brands fa-instagram" style="color:#e11d48; margin-right:4px;"></i> Instagram</td>
                                            <td style="padding:12px 16px; color:var(--text-primary); font-weight:500;">12.4K</td>
                                            <td style="padding:12px 16px; color:var(--status-success); font-weight:600;">9.3% <i class="fa-solid fa-arrow-trend-up" style="font-size:10px;"></i></td>
                                            <td style="padding:12px 16px;"><span class="status-badge badge-done" style="background:#e0e7ff; color:#4338ca;">PUBLISHED</span></td>
                                            <td style="padding:12px 24px; text-align:right;" onclick="event.stopPropagation();">
                                                <div style="display:flex; gap:12px; justify-content:flex-end; color:var(--text-tertiary);">
                                                    <i class="fa-solid fa-chart-line" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                    <i class="fa-solid fa-arrow-up-right-from-square" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                    <i class="fa-solid fa-ellipsis" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                </div>
                                            </td>
                                        </tr>
                                        <tr onclick="document.getElementById('history-list-view').style.display='none'; document.getElementById('history-detail-view').style.display='block';" onmouseover="this.style.background='#f1f5f9';" onmouseout="this.style.background='transparent';" style="border-bottom:1px solid var(--border-light); transition:0.1s;">
                                            <td style="padding:12px 24px;" onclick="event.stopPropagation();"><input type="checkbox"></td>
                                            <td style="padding:12px 16px; color:var(--text-secondary);">#877</td>
                                            <td style="padding:12px 16px; display:flex; align-items:center; gap:12px;">
                                                <div style="width:32px; height:32px; background:linear-gradient(135deg, #0f172a, #334155); border-radius:4px; flex-shrink:0;"></div>
                                                <div>
                                                    <strong style="color:var(--text-primary); font-weight:600; display:block;">React Crash Course 2026</strong>
                                                    <span style="color:var(--text-tertiary); font-size:11px;">Oleh Asta Marketing</span>
                                                </div>
                                            </td>
                                            <td style="padding:12px 16px; color:var(--text-secondary);"><i class="fa-brands fa-tiktok" style="color:#000; margin-right:4px;"></i> TikTok</td>
                                            <td style="padding:12px 16px; color:var(--text-primary); font-weight:500;">8.2K</td>
                                            <td style="padding:12px 16px; color:var(--text-secondary); font-weight:500;">4.5% <i class="fa-solid fa-minus" style="font-size:10px;"></i></td>
                                            <td style="padding:12px 16px;"><span class="status-badge badge-done" style="background:#e0e7ff; color:#4338ca;">PUBLISHED</span></td>
                                            <td style="padding:12px 24px; text-align:right;" onclick="event.stopPropagation();">
                                                <div style="display:flex; gap:12px; justify-content:flex-end; color:var(--text-tertiary);">
                                                    <i class="fa-solid fa-chart-line" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                    <i class="fa-solid fa-arrow-up-right-from-square" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                    <i class="fa-solid fa-ellipsis" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                </div>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            <!-- Pagination -->
                            <div style="padding:12px 24px; background:#fff; border-top:1px solid var(--border-light); display:flex; justify-content:space-between; align-items:center; font-size:12px; color:var(--text-secondary);">
                                <div>1 to 10 of 2000</div>
                                <div style="display:flex; align-items:center; gap:16px;">
                                    <span><i class="fa-solid fa-angle-left" style="color:var(--text-tertiary); cursor:pointer;"></i> <span style="margin:0 8px;">Page 1 of 200</span> <i class="fa-solid fa-angle-right" style="cursor:pointer;"></i></span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 2. DETAIL VIEW'''

content = pattern.sub(new_list_view, content)

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
