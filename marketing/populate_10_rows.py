import re

with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

table_pattern = re.compile(r'<table class="table" style="cursor:pointer; width:100%; border-collapse:collapse; text-align:left; font-size:13px;">.*?</tbody>\s*</table>', re.DOTALL)

rows_data = [
    ("#447", "Kenapa Next.js? (Tutorial)", "Instagram", "fa-instagram", "#e11d48", "12.4K", "9.3%", "fa-arrow-trend-up", "var(--status-success)", "var(--brand-primary), #60a5fa"),
    ("#877", "React Crash Course 2026", "TikTok", "fa-tiktok", "#000", "8.2K", "4.5%", "fa-minus", "var(--text-secondary)", "#0f172a, #334155"),
    ("#556", "Panduan SEO 2026", "Blog CMS", "fa-wordpress", "#2563eb", "1.2K", "2.1%", "fa-arrow-trend-up", "var(--status-success)", "#10b981, #34d399"),
    ("#432", "Behind the Scene Kantor", "Instagram", "fa-instagram", "#e11d48", "15.6K", "12.4%", "fa-arrow-trend-up", "var(--status-success)", "#f59e0b, #fbbf24"),
    ("#536", "Tips Ngoding Malam", "TikTok", "fa-tiktok", "#000", "24.0K", "18.2%", "fa-arrow-trend-up", "var(--status-success)", "#8b5cf6, #a78bfa"),
    ("#703", "Promo Diskon Web", "Meta Ads", "fa-facebook", "#1877f2", "45.1K", "5.0%", "fa-arrow-trend-down", "var(--status-danger)", "#ec4899, #f472b6"),
    ("#922", "Cara Deploy ke Vercel", "Instagram", "fa-instagram", "#e11d48", "5.5K", "8.7%", "fa-arrow-trend-up", "var(--status-success)", "#14b8a6, #2dd4bf"),
    ("#540", "Tutorial Python Pemula", "TikTok", "fa-tiktok", "#000", "30.1K", "15.3%", "fa-arrow-trend-up", "var(--status-success)", "#f43f5e, #fb7185"),
    ("#426", "Memilih Framework Frontend", "Blog CMS", "fa-wordpress", "#2563eb", "3.4K", "1.5%", "fa-minus", "var(--text-secondary)", "#6366f1, #818cf8"),
    ("#883", "Q&A: Bootcamp Worth it?", "Instagram", "fa-instagram", "#e11d48", "18.2K", "11.1%", "fa-arrow-trend-up", "var(--status-success)", "#d946ef, #e879f9")
]

rows_html = ""
for r in rows_data:
    rows_html += f'''
                                        <tr onclick="document.getElementById('history-list-view').style.display='none'; document.getElementById('history-detail-view').style.display='block';" onmouseover="this.style.background='#f1f5f9';" onmouseout="this.style.background='transparent';" style="border-bottom:1px solid var(--border-light); transition:0.1s;">
                                            <td style="padding:12px 24px;" onclick="event.stopPropagation();"><input type="checkbox"></td>
                                            <td style="padding:12px 16px; color:var(--text-secondary);">{r[0]}</td>
                                            <td style="padding:12px 16px; display:flex; align-items:center; gap:12px;">
                                                <div style="width:32px; height:32px; background:linear-gradient(135deg, {r[9]}); border-radius:4px; flex-shrink:0;"></div>
                                                <div>
                                                    <strong style="color:var(--text-primary); font-weight:600; display:block;">{r[1]}</strong>
                                                    <span style="color:var(--text-tertiary); font-size:11px;">Oleh Asta Marketing</span>
                                                </div>
                                            </td>
                                            <td style="padding:12px 16px; color:var(--text-secondary);"><i class="fa-brands {r[3]}" style="color:{r[4]}; margin-right:4px;"></i> {r[2]}</td>
                                            <td style="padding:12px 16px; color:var(--text-primary); font-weight:500;">{r[5]}</td>
                                            <td style="padding:12px 16px; color:{r[8]}; font-weight:600;">{r[6]} <i class="fa-solid {r[7]}" style="font-size:10px;"></i></td>
                                            <td style="padding:12px 16px;"><span class="status-badge badge-done" style="background:#e0e7ff; color:#4338ca;">PUBLISHED</span></td>
                                            <td style="padding:12px 24px; text-align:right;" onclick="event.stopPropagation();">
                                                <div style="display:flex; gap:12px; justify-content:flex-end; color:var(--text-tertiary);">
                                                    <i class="fa-solid fa-chart-line" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                    <i class="fa-solid fa-arrow-up-right-from-square" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                    <i class="fa-solid fa-ellipsis" style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)';" onmouseout="this.style.color='var(--text-tertiary)';"></i>
                                                </div>
                                            </td>
                                        </tr>'''

new_table = f'''<table class="table" style="cursor:pointer; width:100%; border-collapse:collapse; text-align:left; font-size:13px;">
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
                                    <tbody>{rows_html}
                                    </tbody>
                                </table>'''

content = table_pattern.sub(new_table, content)

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
