"""
Add filterFromHeader JavaScript function.
"""
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

OLD_MARKER = '''        // ==================== COLOR/THREAT LEVEL FILTER ====================
        let activeColorFilter = 'all';'''

NEW_CODE = '''        // ==================== HEADER STAT FILTERS ====================
        function filterFromHeader(level, el) {
            // Toggle: if already active, show all
            const isActive = el.classList.contains('active');

            // Remove active from all header stats
            document.querySelectorAll('.header-stat').forEach(s => s.classList.remove('active'));

            if (isActive) {
                // Was active, now show all
                filterByColor('all');
            } else {
                // Activate this one
                el.classList.add('active');
                filterByColor(level);
            }
        }

        // ==================== COLOR/THREAT LEVEL FILTER ====================
        let activeColorFilter = 'all';'''

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'function filterFromHeader' not in content and OLD_MARKER in content:
        content = content.replace(OLD_MARKER, NEW_CODE)
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
