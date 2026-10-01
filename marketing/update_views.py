with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Asset Library
old_asset_lib = '''                <!-- 8. BRAND ASSET LIBRARY -->
                <section id="view-asset-library" class="view-section">
                    <div style="margin-bottom: 24px;">
                        <h2 style="font-size:20px;">Brand Asset Library</h2>
                        <p style="font-size:13px; color:var(--text-tertiary);">Pusat media dan identitas brand. AI akan menggunakan aset ini agar desain selalu konsisten.</p>
                    </div>
                    <div class="grid-3">'''

new_asset_lib = '''                <!-- 8. BRAND ASSET LIBRARY -->
                <section id="view-asset-library" class="view-section">
                    <div style="margin-bottom: 24px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <h2 style="font-size:20px;">Brand Asset Library</h2>
                            <p style="font-size:13px; color:var(--text-tertiary);">Pusat media dan identitas brand. AI akan menggunakan aset ini agar desain selalu konsisten.</p>
                        </div>
                        <button class="btn btn-primary"><i class="fa-solid fa-cloud-arrow-up"></i> Unggah Aset</button>
                    </div>
                    
                    <div style="background:var(--bg-card); border:2px dashed var(--border-dark); border-radius:var(--radius-md); padding:40px; text-align:center; margin-bottom:24px; cursor:pointer; transition:0.2s;" onmouseover="this.style.borderColor='var(--brand-primary)';" onmouseout="this.style.borderColor='var(--border-dark)';">
                        <i class="fa-solid fa-images" style="font-size:40px; color:var(--text-tertiary); margin-bottom:16px;"></i>
                        <h3 style="font-size:15px; margin-bottom:8px;">Tarik & Lepas file ke sini</h3>
                        <p style="font-size:13px; color:var(--text-tertiary);">Unggah Foto Produk, Aset Campaign, Logo (.png, .svg), atau PDF Panduan Brand.</p>
                    </div>

                    <div class="grid-3">'''

content = content.replace(old_asset_lib, new_asset_lib)

# Update Inbox
old_inbox = '''                <!-- 10. OMNICHANNEL INBOX -->
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
                </section>'''

new_inbox = '''                <!-- 10. OMNICHANNEL INBOX -->
                <section id="view-inbox" class="view-section">
                    <div style="margin-bottom: 24px; display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <h2 style="font-size:20px;">Omnichannel Inbox (Auto-Reply AI)</h2>
                            <p style="font-size:13px; color:var(--text-tertiary);">AI otomatis membalas DM & komentar berdasarkan Knowledge Base (Data Produk).</p>
                        </div>
                        <div style="display:flex; align-items:center; gap:10px;">
                            <span style="font-size:12px; font-weight:600; color:var(--text-secondary);">AI Auto-Reply:</span>
                            <label class="switch">
                                <input type="checkbox" checked>
                                <span class="slider"></span>
                            </label>
                        </div>
                    </div>
                    <div class="grid-2">
                        <div class="card">
                            <div class="card-header"><div class="card-title">Live Chat Feed</div></div>
                            <div class="card-body p-0">
                                <div style="padding:16px; border-bottom:1px solid var(--border-light); background:var(--bg-hover);">
                                    <strong style="font-size:13px;"><i class="fa-brands fa-instagram" style="color:#e11d48;"></i> Budi Santoso</strong> <span class="status-badge badge-done" style="float:right;">TERBALAS OTOMATIS</span>
                                    <p style="font-size:12px; margin-top:4px;">"Min, promo yang kemaren masih ada gak ya?"</p>
                                </div>
                            </div>
                        </div>
                        <div class="card">
                            <div class="card-body">
                                <div style="background:var(--bg-input); padding:16px; border-radius:var(--radius-md); margin-bottom:16px;">
                                    <strong style="font-size:11px; color:var(--status-success);"><i class="fa-solid fa-bolt"></i> Dibalas otomatis oleh AI dalam 2 detik</strong>
                                    <p style="font-size:13px; margin-top:8px;">"Halo Kak Budi! 👋 Promo bulan lalu sudah berakhir, tapi jangan khawatir, kita punya diskon spesial 20% khusus buat Kakak hari ini. Cek link di bio ya!"</p>
                                </div>
                                <div style="font-size:11px; color:var(--text-tertiary); display:flex; align-items:center; gap:6px;">
                                    <i class="fa-solid fa-database"></i> <span>Data acuan AI: <strong>Katalog_Promo.pdf</strong> (Akurasi 98%)</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>'''

content = content.replace(old_inbox, new_inbox)

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
