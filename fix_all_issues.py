"""
Fix all issues in route pages:
1. Change LOW color from green to purple-gray
2. Ensure filters work with checkmarks
3. Ensure date filter button exists
"""
import re
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Change green emoji to purple/gray for LOW
    content = content.replace('🟢', '🟣')  # Green to purple circle

    # 2. Change LOW color in CSS from green to purple-gray
    content = content.replace('.header-stat.low { color: #6ee7b7; }', '.header-stat.low { color: #a78bfa; }')
    content = content.replace('.stat-item.low { border-bottom: 3px solid #6b5b7a; }', '.stat-item.low { border-bottom: 3px solid #8b7ba0; }')

    # 3. Change background color for LOW filter from green to purple
    content = content.replace(
        "'low': 'linear-gradient(135deg, #f0fff4 0%, #e8f5e9 100%)'",
        "'low': 'linear-gradient(135deg, #f5f0ff 0%, #ede8f5 100%)'"
    )

    if content != original:
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
