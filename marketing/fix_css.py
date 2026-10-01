import sys

replacements = {
    'var(--primary)': 'var(--brand-primary)',
    'var(--border)': 'var(--border-light)',
    'var(--text-muted)': 'var(--text-tertiary)',
    'var(--shadow-sm)': 'var(--shadow-soft)'
}

with open(r"d:\laragon\www\marketing_prototype\index.html", "r", encoding="utf-8") as f:
    content = f.read()

for k, v in replacements.items():
    content = content.replace(k, v)

with open(r"d:\laragon\www\marketing_prototype\index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Variables fixed successfully!")
