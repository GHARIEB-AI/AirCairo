"""
Remove LOW (green) threat cards from all route pages.
Also update the header stats to not show LOW count.
"""
import re
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

def remove_low_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_len = len(content)

    # Remove LOW threat cards (they have class="threat-card low")
    # Pattern: <div class="threat-card low">...entire card...</div>
    content = re.sub(
        r'<div class="threat-card low">.*?</div>\s*</div>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove LOW from header stats
    content = re.sub(
        r'<span class="header-stat low"[^>]*>.*?</span>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove LOW from stats bar if exists
    content = re.sub(
        r'<div class="stat-item low"[^>]*>.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    if len(content) != original_len:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    fixed_count = 0
    for html_file in ROUTES_DIR.glob('*.html'):
        if remove_low_from_file(html_file):
            print(f"Fixed: {html_file.name}")
            fixed_count += 1
    print(f"\nTotal fixed: {fixed_count} files")

if __name__ == '__main__':
    main()
