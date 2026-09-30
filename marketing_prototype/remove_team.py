with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

sidebar_to_remove = '''                    <a href="#" class="nav-item" data-target="view-team">
                        <i class="fa-solid fa-users-gear"></i> <span>Manajemen Tim</span>
                    </a>\n'''
content = content.replace(sidebar_to_remove, '')

section_to_remove = '''                <!-- 12. TEAM MANAGEMENT -->
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
                </section>\n\n'''
content = content.replace(section_to_remove, '')

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)


with open(r'd:\laragon\www\marketing_prototype\penjelasan_full_power.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

md_to_remove = '''## 5. Team Roles & Collaboration (Manajemen Tim Multi-User)
**Lokasi di Aplikasi:** Sidebar -> Manajemen Tim
**Fungsi Utama:** Sistem pendelegasian wewenang bertingkat yang wajib ada di setiap *software* ERP kantor.
*   **Mengapa Ini Penting?** Data analitik dan akses penerbitan (*publishing*) tidak boleh disentuh sembarangan oleh anak magang atau pekerja lepas (*freelancer*).
*   **Cara Kerja AI & Sistem:** Anda dapat membagi akses:
    *   **Manager (Full Akses):** Bisa melihat analitik, mengatur budget, dan klik tombol *Approve*.
    *   **Copywriter (Draft Only):** Hanya bisa masuk ke *AI Content Engine* untuk membuat draf, tapi tidak punya tombol *Approve* atau akses untuk mengubah *budget* Ads. Semuanya harus masuk ke tahap *Review* di Kanban.

---
'''
md_content = md_content.replace(md_to_remove, '')
md_content = md_content.replace('menjelaskan 5 fitur', 'menjelaskan 4 fitur')
md_content = md_content.replace('kelima modul', 'keempat modul')

with open(r'd:\laragon\www\marketing_prototype\penjelasan_full_power.md', 'w', encoding='utf-8') as f:
    f.write(md_content)
