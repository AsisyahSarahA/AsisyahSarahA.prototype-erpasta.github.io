import sys
try:
    from bs4 import BeautifulSoup
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

table_cards = soup.find_all('div', class_='table-card glass')

for card in table_cards:
    header = card.find('div', class_='card-header')
    title_text = "Data Tabel"
    button_html = '<button class="primary-btn"><i class="fa-solid fa-plus"></i> Tambah Data Baru</button>'
    
    if header:
        h3 = header.find('h3')
        if h3:
            title_text = h3.text
        btn = header.find('button', class_='primary-btn')
        if btn:
            button_html = str(btn)
        
        # Don't add to "Aktivitas Transaksi Terbaru" on dashboard since it has view-all
        if "Aktivitas Transaksi" in title_text:
            continue
            
        header.decompose()
    else:
        # try to guess title from view-section
        parent_view = card.find_parent('div', class_='view-section')
        if parent_view and parent_view.find('h1'):
            title_text = parent_view.find('h1').text

    # Make specific counts
    rows = card.find_all('tbody')
    total_count = 0
    if rows:
        total_count = len(rows[0].find_all('tr'))
    if total_count == 0:
        total_count = 3 # fallback dummy

    new_header_html = f"""
    <div class="card-header-complex">
        <div class="header-title-row">
            <h3>{title_text}</h3>
            <span class="badge-total">Total: {total_count} Data</span>
        </div>
        <div class="header-actions-row">
            <div class="search-box">
                <i class="fa-solid fa-search"></i>
                <input type="text" placeholder="Cari {title_text.lower()}...">
            </div>
            <button class="icon-btn-outline"><i class="fa-solid fa-filter"></i> Filter</button>
            {button_html}
        </div>
    </div>
    """
    new_header_soup = BeautifulSoup(new_header_html, 'html.parser')
    card.insert(0, new_header_soup)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
