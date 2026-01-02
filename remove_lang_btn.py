"""
Remove language toggle button from route pages.
Keep it only on HOME page.
"""
import os
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

# The lang button to remove
OLD_WITH_LANG = '''        <button class="date-filter-btn" onclick="openDateModal()">📅</button>
        <button class="lang-btn" onclick="toggleLang()">
            <span class="ar-text">EN</span>
            <span class="en-text">عربي</span>
        </button>

        <div class="header-main">'''

NEW_WITHOUT_LANG = '''        <button class="date-filter-btn" onclick="openDateModal()">📅</button>

        <div class="header-main">'''

def fix_file(filepath):
    """Remove lang button from a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if OLD_WITH_LANG in content:
        content = content.replace(OLD_WITH_LANG, NEW_WITHOUT_LANG)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    fixed_count = 0

    for html_file in ROUTES_DIR.glob('*.html'):
        if fix_file(html_file):
            print(f"Fixed: {html_file.name}")
            fixed_count += 1

    print(f"\nTotal fixed: {fixed_count} files")

if __name__ == '__main__':
    main()
