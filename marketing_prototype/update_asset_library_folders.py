import re

with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

folders = [
    "Backgrounds", "Logo & Watermark", "Fonts & Typography",
    "Icons & Illustrations", "Product Mockups", "Social Media Templates",
    "Office Photos", "Team Portraits", "UI Components"
]

items_html = ""
for f_name in folders:
    items_html += f'''
                <!-- Folder Item -->
                <div style="text-align:center; cursor:pointer;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">
                    <i class="fa-solid fa-folder" style="font-size:64px; color:#3b82f6; margin-bottom:12px;"></i>
                    <div style="font-weight:600; font-size:13px; color:var(--text-primary); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">{f_name}</div>
                    <div style="font-size:11px; color:var(--text-tertiary);">09/28/2026, 10:44 am</div>
                </div>'''

# Add the selected item
items_html += '''
                <!-- File Image (Selected) -->
                <div style="text-align:center; cursor:pointer; background:#eff6ff; padding:12px; border-radius:8px; border:1px solid #93c5fd; box-shadow:0 4px 12px rgba(59,130,246,0.15);">
                    <div style="width:100%; aspect-ratio:4/3; background:linear-gradient(135deg, #cbd5e1, #94a3b8); border-radius:4px; margin-bottom:12px; display:flex; align-items:center; justify-content:center; overflow:hidden;">
                        <i class="fa-solid fa-image" style="font-size:32px; color:#fff;"></i>
                    </div>
                    <div style="font-weight:600; font-size:13px; color:var(--brand-primary); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">office_lobby_bg</div>
                    <div style="font-size:11px; color:var(--brand-primary);">28.09.2026, 13:44</div>
                </div>'''

# Add a few PDFs
for i in range(1, 3):
    items_html += f'''
                <!-- File PDF -->
                <div style="text-align:center; cursor:pointer;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">
                    <div style="width:72px; height:72px; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; margin:0 auto 12px auto; display:flex; align-items:center; justify-content:center;">
                        <span style="font-size:11px; font-weight:bold; color:#cbd5e1; border:1px solid #cbd5e1; padding:2px 4px; border-radius:2px;">pdf</span>
                    </div>
                    <div style="font-weight:600; font-size:13px; color:var(--text-primary); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">brand_guidelines_{i}</div>
                    <div style="font-size:11px; color:var(--text-tertiary);">09/28/2026, 10:44 am</div>
                </div>'''

new_section = f'''<section id="view-asset-library" class="view-section">
                    <!-- Title and Description -->
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px; font-weight:600;">Brand Asset Library</h2>
                        <p style="font-size:13px; color:var(--text-tertiary); margin-top:4px;">Pusat media dan identitas brand. AI akan menggunakan aset ini agar desain selalu konsisten.</p>
                    </div>

                    <!-- Header with Breadcrumbs & Actions -->
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; background:#fff; padding:16px 24px; border-radius:8px; border:1px solid var(--border-light); box-shadow:0 2px 8px rgba(0,0,0,0.02);">
                        <div style="display:flex; align-items:center; gap:12px; font-size:14px; font-weight:600; color:var(--text-secondary);">
                            <i class="fa-solid fa-cloud" style="color:var(--brand-primary); font-size:18px;"></i>
                            <span style="color:var(--text-tertiary);"><i class="fa-solid fa-angle-right"></i></span>
                            <span style="cursor:pointer;" onmouseover="this.style.color='var(--brand-primary)'" onmouseout="this.style.color='var(--text-secondary)'">Semua File</span>
                            <span style="color:var(--text-tertiary);"><i class="fa-solid fa-angle-right"></i></span>
                            <span style="color:var(--text-primary);">Aset Software House</span>
                        </div>
                        <div style="display:flex; gap:16px; align-items:center;">
                            <select class="form-control" style="height:32px; font-size:12px; border:none; background:transparent; font-weight:500;"><option>Sort by: type</option><option>Sort by: date</option></select>
                            <div style="display:flex; gap:12px; color:var(--text-tertiary); border-right:1px solid var(--border-light); padding-right:16px;">
                                <i class="fa-solid fa-table-cells" style="cursor:pointer; color:var(--brand-primary);"></i>
                                <i class="fa-solid fa-list" style="cursor:pointer;"></i>
                            </div>
                            <button class="btn btn-outline" style="font-size:12px; height:32px; padding:0 12px;"><i class="fa-solid fa-folder-plus"></i> Folder Baru</button>
                            <button class="btn btn-primary" style="font-size:12px; height:32px; padding:0 12px;"><i class="fa-solid fa-upload"></i> Upload</button>
                        </div>
                    </div>

                    <!-- Main Content Area -->
                    <div style="display:flex; gap:24px; height:calc(100vh - 220px);">
                        
                        <!-- Grid View -->
                        <div class="card" style="flex:1; overflow-y:auto; padding:32px; box-shadow:0 4px 12px rgba(0,0,0,0.05); border:1px solid var(--border-light); border-radius:8px; background:#fff;">
                            <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(140px, 1fr)); gap:40px 24px;">
                                {items_html}
                            </div>
                        </div>

                        <!-- Sidebar Detail -->
                        <div class="card" style="width:300px; flex-shrink:0; padding:24px; box-shadow:0 4px 12px rgba(0,0,0,0.05); border:1px solid var(--border-light); border-radius:8px; background:#fff; overflow-y:auto;">
                            <!-- Actions -->
                            <div style="display:flex; justify-content:flex-end; gap:16px; color:var(--text-tertiary); margin-bottom:24px; font-size:14px;">
                                <i class="fa-solid fa-bookmark" style="cursor:pointer;" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--text-tertiary)'"></i>
                                <i class="fa-solid fa-pen" style="cursor:pointer;" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--text-tertiary)'"></i>
                                <div style="background:#eff6ff; padding:4px 8px; border-radius:4px; margin-top:-4px;"><i class="fa-solid fa-trash" style="cursor:pointer; color:#3b82f6;"></i></div>
                                <i class="fa-regular fa-envelope" style="cursor:pointer;" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--text-tertiary)'"></i>
                                <i class="fa-solid fa-print" style="cursor:pointer;" onmouseover="this.style.color='var(--text-primary)'" onmouseout="this.style.color='var(--text-tertiary)'"></i>
                            </div>
                            
                            <!-- Title -->
                            <h3 style="font-size:16px; font-weight:700; margin-bottom:4px; color:var(--brand-primary);">office_lobby_bg</h3>
                            <p style="font-size:12px; color:var(--text-tertiary); margin-bottom:20px;">PNG-image - 4.1 MB</p>
                            
                            <!-- Preview -->
                            <div style="width:100%; aspect-ratio:4/3; background:linear-gradient(135deg, #cbd5e1, #94a3b8); border-radius:8px; margin-bottom:24px; display:flex; align-items:center; justify-content:center;">
                                <i class="fa-solid fa-image" style="font-size:48px; color:#fff;"></i>
                            </div>
                            
                            <!-- Information List -->
                            <h4 style="font-size:13px; font-weight:600; color:var(--text-primary); margin-bottom:16px;">Information</h4>
                            
                            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:12px;">
                                <span style="color:var(--text-tertiary);">Created</span>
                                <span style="color:var(--text-primary); font-weight:500;">09/01/2026, 10:44 am</span>
                            </div>
                            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:12px;">
                                <span style="color:var(--text-tertiary);">Last updated</span>
                                <span style="color:var(--text-primary); font-weight:500;">09/12/2026, 5:12 pm</span>
                            </div>
                            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:12px;">
                                <span style="color:var(--text-tertiary);">Last opened</span>
                                <span style="color:var(--text-primary); font-weight:500;">09/15/2026, 6:56 pm</span>
                            </div>
                            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:12px;">
                                <span style="color:var(--text-tertiary);">Image size</span>
                                <span style="color:var(--text-primary); font-weight:500;">3840x2160</span>
                            </div>
                            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:12px;">
                                <span style="color:var(--text-tertiary);">Resolution</span>
                                <span style="color:var(--text-primary); font-weight:500;">300x300</span>
                            </div>
                            <div style="display:flex; justify-content:space-between; font-size:12px; margin-bottom:12px;">
                                <span style="color:var(--text-tertiary);">Color space</span>
                                <span style="color:var(--text-primary); font-weight:500;">RGB</span>
                            </div>
                        </div>

                    </div>
                </section>'''

# Replace using regex looking for <section id="view-asset-library" class="view-section"> ... </section>
pattern = re.compile(r'<section id="view-asset-library" class="view-section">.*?</section>', re.DOTALL)
content = pattern.sub(new_section, content)

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
