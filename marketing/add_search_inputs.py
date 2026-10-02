import re

file_path = 'd:/laragon/www/marketing_prototype/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add search to Brand Asset Library
# Search for:
# <div style="display:flex; gap:16px; align-items:center;">
#     <select class="form-control" style="height:32px; font-size:12px; border:none; background:transparent; font-weight:500;"><option>Sort by: type</option><option>Sort by: date</option></select>
# Inside the Asset Library section (around line 868)
search_input_html = '''<div style="position:relative;">
                                <i class="fa-solid fa-magnifying-glass" style="position:absolute; left:10px; top:50%; transform:translateY(-50%); color:var(--text-tertiary); font-size:12px;"></i>
                                <input type="text" placeholder="Cari..." style="height:32px; padding:0 12px 0 32px; font-size:12px; border:1px solid var(--border-light); border-radius:6px; outline:none; width:180px;">
                            </div>
                            '''

brand_asset_target = '''<div style="display:flex; gap:16px; align-items:center;">
                            <select class="form-control" style="height:32px; font-size:12px; border:none; background:transparent; font-weight:500;"><option>Sort by: type</option><option>Sort by: date</option></select>'''

if brand_asset_target in content:
    content = content.replace(brand_asset_target, '''<div style="display:flex; gap:16px; align-items:center;">
                            ''' + search_input_html + '''<select class="form-control" style="height:32px; font-size:12px; border:none; background:transparent; font-weight:500;"><option>Sort by: type</option><option>Sort by: date</option></select>''', 1)

# 2. Add search to Filter Bars
# We will inject the search input inside <div style="display:flex; gap:12px;"> right after <!-- Filter Bar --> and the following <div class...>
# Let's use regex to find Filter Bars and their child div.
filter_bar_pattern = r'(<!-- Filter Bar -->\s*<div[^>]*>\s*<div style="display:flex; gap:12px;">)'

def insert_search(match):
    return match.group(1) + '\n                                ' + search_input_html.strip() + '\n                                '

content = re.sub(filter_bar_pattern, insert_search, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Search inputs added.")
