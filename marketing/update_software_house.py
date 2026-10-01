with open(r'd:\laragon\www\marketing_prototype\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    # Inbox
    '"Min, promo yang kemaren masih ada gak ya?"': '"Min, mau tanya kalau biaya bikin website company profile (React.js) berapa ya?"',
    '"Kerja sama endorsement kak, bisa cek ratecard?"': '"Kak, kalo bikin ERP custom untuk pabrik lebih bagus pakai Laravel atau Node.js?"',
    '"Barang udh sampai min, makasih ya!"': '"Wah makasih tutorial deploy servernya min, sangat membantu project aplikasi saya!"',
    
    # Inbox AI action labels
    'TERBALAS OTOMATIS': 'TERBALAS (PRICING AI)',
    'BUTUH MANUSIA': 'BUTUH TIM TEKNIS',
    
    # Social Listening
    '@KompetitorA': '@AgencyWebJkt',
    '"Kesalahan Fatal Pemula di Next.js"': '"Berapa Modal Bikin Website E-Commerce di 2026?"',
    '@TokoTech': '@TechStartupIndo',
    '"Review Macbook M3 2026"': '"Kenapa Perusahaan Mulai Meninggalkan React?"',
    
    # Content History tweaks
    'Promo Diskon Web': 'Promo Jasa Pembuatan Aplikasi',
    'Behind the Scene Kantor': 'A Day in the Life: Software Engineer',
    'Q&A: Bootcamp Worth it?': 'Bikin Web Custom vs Template WP',
    
    # Detail View Comments / UI
    'Data acuan AI: <strong>Katalog_Promo.pdf</strong>': 'Data acuan AI: <strong>Pricelist_Software_House.pdf</strong>',
    '"Halo Kak Budi! 👋 Promo bulan lalu sudah berakhir, tapi jangan khawatir, kita punya diskon spesial 20% khusus buat Kakak hari ini. Cek link di bio ya!"': '"Halo Kak Budi! 👋 Untuk biaya pembuatan website company profile berbasis React mulai dari Rp 15 Juta. Silakan klik link di bio untuk konsultasi gratis dengan tim developer kami ya!"'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(r'd:\laragon\www\marketing_prototype\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
