import re

file_path = 'd:/laragon/www/marketing_prototype/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the table action buttons to include a View button
view_btn = '<button class="btn btn-outline" style="padding:4px 8px; font-size:11px; height:auto; margin-right:4px; color:var(--brand-primary); border-color:var(--brand-primary); background:#fff;" title="Lihat Detail" onclick="openReviewModal()"><i class="fa-solid fa-eye"></i></button>'

# Find the actions column for "Trend: AI Agents vs Framework" and "Meme Kodingan Error di Produksi"
# The string to replace is:
# <td style="padding:12px 24px; text-align:right;">
#                                             <button class="btn btn-outline" style="padding:4px 8px; font-size:11px; height:auto; margin-right:4px; color:#16a34a; border-color:#16a34a; background:#fff;" title="Setujui"><i class="fa-solid fa-check"></i></button>

action_pattern = r'(<td style="padding:12px 24px; text-align:right;">)\s*(<button class="btn btn-outline" style="padding:4px 8px; font-size:11px; height:auto; margin-right:4px; color:#16a34a; border-color:#16a34a; background:#fff;" title="Setujui">)'
action_replacement = r'\1\n                                            ' + view_btn + r'\n                                            \2'

content = re.sub(action_pattern, action_replacement, content)

# 2. Add Modal HTML and CSS at the end of the file, right before </body> or <script src="app.js">
modal_html = '''
    <!-- Review Content Modal -->
    <div id="reviewModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15, 23, 42, 0.6); z-index:9999; align-items:center; justify-content:center; backdrop-filter:blur(4px);">
        <div style="background:#fff; width:900px; max-width:95%; border-radius:12px; box-shadow:0 20px 40px rgba(0,0,0,0.2); overflow:hidden; display:flex; flex-direction:column; animation: modalFadeIn 0.3s ease-out;">
            <!-- Modal Header -->
            <div style="padding:16px 24px; border-bottom:1px solid var(--border-light); display:flex; justify-content:space-between; align-items:center; background:#f8fafc;">
                <div>
                    <h3 style="margin:0; font-size:18px; color:var(--text-primary); font-weight:700;">Review Konten: Trend AI Agents vs Framework</h3>
                    <div style="font-size:12px; color:var(--text-tertiary); margin-top:4px;"><i class="fa-brands fa-tiktok" style="color:#000;"></i> TikTok • Draft dibuat 1 jam lalu oleh AI Agent</div>
                </div>
                <button onclick="closeReviewModal()" style="background:transparent; border:none; font-size:20px; color:var(--text-tertiary); cursor:pointer; padding:4px;"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <!-- Modal Body -->
            <div style="display:flex; height:500px; overflow:hidden;">
                <!-- Left: Media Preview -->
                <div style="flex:1; background:#000; position:relative; display:flex; align-items:center; justify-content:center;">
                    <div style="width:280px; height:490px; border-radius:16px; border:8px solid #333; background:#111; overflow:hidden; position:relative; display:flex; align-items:center; justify-content:center; flex-direction:column;">
                        <i class="fa-brands fa-tiktok" style="color:#fff; font-size:40px; opacity:0.2; margin-bottom:16px;"></i>
                        <span style="color:#fff; font-size:12px; opacity:0.5;">[Pratinjau Video TikTok]</span>
                        <div style="position:absolute; bottom:16px; left:16px; right:16px; display:flex; gap:8px;">
                            <div style="width:100%; height:4px; background:rgba(255,255,255,0.3); border-radius:2px;"><div style="width:40%; height:100%; background:#fff; border-radius:2px;"></div></div>
                        </div>
                    </div>
                </div>
                
                <!-- Right: Details & Analysis -->
                <div style="flex:1; padding:24px; overflow-y:auto; background:#fff;">
                    <!-- AI Analysis Card -->
                    <div style="background:#fffbeb; border:1px solid #fde68a; border-radius:8px; padding:16px; margin-bottom:24px;">
                        <div style="display:flex; align-items:center; gap:8px; margin-bottom:12px;">
                            <i class="fa-solid fa-robot" style="color:#d97706; font-size:16px;"></i>
                            <h4 style="margin:0; font-size:14px; color:#92400e; font-weight:700;">Catatan AI (Butuh Review)</h4>
                        </div>
                        <p style="font-size:13px; color:#92400e; margin:0; line-height:1.5;">Konten ini memiliki <strong>Bobot Kebagusan (72/100)</strong> dan <strong>Nilai Edukasi (68/100)</strong>. AI mendeteksi penggunaan istilah teknis yang mungkin terlalu berat untuk audiens TikTok umum. <em>Saran: Sederhanakan caption atau tambahkan hook yang lebih menarik di 3 detik pertama.</em></p>
                    </div>

                    <!-- Caption Section -->
                    <h4 style="margin:0 0 8px 0; font-size:14px; color:var(--text-secondary);">Caption (Generated by AI)</h4>
                    <div style="background:#f1f5f9; padding:16px; border-radius:8px; font-size:13px; color:var(--text-primary); line-height:1.6; margin-bottom:24px; border:1px solid var(--border-light);">
                        Zaman sekarang bikin aplikasi masih ngetik dari nol? 😱<br><br>
                        Kenalin nih era AI Agents! Framework lawas udah mulai tergantikan sama AI yang bisa nulis kode sendiri. Tapi tunggu dulu, apakah benar-benar bisa menggantikan programmer seutuhnya?<br><br>
                        Tonton sampai habis untuk tau jawabannya! 👇<br><br>
                        #AITech #Coding #ProgrammerLife #TechTrends #WebDev
                    </div>

                    <!-- Hashtag Analysis -->
                    <h4 style="margin:0 0 8px 0; font-size:14px; color:var(--text-secondary);">Analisis Hashtag</h4>
                    <div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:24px;">
                        <span style="background:#dcfce7; color:#166534; padding:4px 10px; border-radius:4px; font-size:11px; font-weight:600;"><i class="fa-solid fa-arrow-trend-up"></i> #AITech (Viral)</span>
                        <span style="background:#f1f5f9; color:var(--text-secondary); padding:4px 10px; border-radius:4px; font-size:11px; font-weight:500;">#Coding (Stabil)</span>
                    </div>
                </div>
            </div>

            <!-- Modal Footer (Actions) -->
            <div style="padding:16px 24px; border-top:1px solid var(--border-light); background:#f8fafc; display:flex; justify-content:flex-end; gap:12px;">
                <button class="btn btn-outline" style="color:#e11d48; border-color:#e11d48;" onclick="closeReviewModal()"><i class="fa-solid fa-xmark"></i> Tolak / Revisi</button>
                <button class="btn btn-primary" style="background:#10b981; border:none; box-shadow:0 4px 12px rgba(16,185,129,0.3);" onclick="approveAndClose()"><i class="fa-solid fa-check"></i> Setujui & Jadwalkan</button>
            </div>
        </div>
    </div>
    
    <style>
        @keyframes modalFadeIn {
            from { opacity: 0; transform: translateY(20px) scale(0.95); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }
    </style>
    <script>
        function openReviewModal() {
            document.getElementById('reviewModal').style.display = 'flex';
        }
        function closeReviewModal() {
            document.getElementById('reviewModal').style.display = 'none';
        }
        function approveAndClose() {
            alert('Konten berhasil disetujui dan masuk ke jadwal (Content Calendar)!');
            closeReviewModal();
        }
    </script>
'''

content = content.replace('    <!-- Application Script -->\n    <script src="app.js"></script>', modal_html + '\n    <!-- Application Script -->\n    <script src="app.js"></script>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Review Modal added successfully!")
