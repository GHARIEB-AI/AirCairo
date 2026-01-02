"""
Fix escaped quotes in onclick handlers.
"""
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix escaped quotes
    if "\\'" in content:
        content = content.replace("\\'", "'")
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
