"""
Fix header stats to be clickable filters with checkmark.
"""
import os
import re
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

# Old header-stat CSS
OLD_HEADER_STAT_CSS = '''        .header-stat {
            font-size: 0.75em;
        }
        .header-stat.high { color: #fca5a5; }
        .header-stat.medium { color: #fcd34d; }
        .header-stat.low { color: #6ee7b7; }'''

# New header-stat CSS with clickable and checkmark
NEW_HEADER_STAT_CSS = '''        .header-stat {
            font-size: 0.75em;
            cursor: pointer;
            padding: 4px 8px;
            border-radius: 15px;
            transition: all 0.2s;
        }
        .header-stat:active { transform: scale(0.95); }
        .header-stat.active { background: rgba(255,255,255,0.3); }
        .header-stat.active::after { content: " ✓"; }
        .header-stat.high { color: #fca5a5; }
        .header-stat.medium { color: #fcd34d; }
        .header-stat.low { color: #6ee7b7; }'''

# Old header-stats HTML pattern
def fix_header_stats_html(content):
    """Add onclick to header-stat spans."""
    # Pattern for header-stat spans
    old_pattern = r'<span class="header-stat high">([^<]+)</span>'
    new_pattern = r'<span class="header-stat high" onclick="filterFromHeader(\'high\', this)">\1</span>'
    content = re.sub(old_pattern, new_pattern, content)

    old_pattern = r'<span class="header-stat medium">([^<]+)</span>'
    new_pattern = r'<span class="header-stat medium" onclick="filterFromHeader(\'medium\', this)">\1</span>'
    content = re.sub(old_pattern, new_pattern, content)

    old_pattern = r'<span class="header-stat low">([^<]+)</span>'
    new_pattern = r'<span class="header-stat low" onclick="filterFromHeader(\'low\', this)">\1</span>'
    content = re.sub(old_pattern, new_pattern, content)

    return content

# JavaScript function to add
JS_FILTER_FUNCTION = '''
        // ==================== HEADER STAT FILTERS ====================
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

        // ==================== COLOR/THREAT LEVEL FILTER ===================='''

OLD_JS_MARKER = '''        // ==================== COLOR/THREAT LEVEL FILTER ===================='''

def fix_file(filepath):
    """Fix header stats in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    # Fix CSS
    if OLD_HEADER_STAT_CSS in content:
        content = content.replace(OLD_HEADER_STAT_CSS, NEW_HEADER_STAT_CSS)
        changed = True

    # Fix HTML - add onclick if not already there
    if 'onclick="filterFromHeader' not in content:
        content = fix_header_stats_html(content)
        changed = True

    # Add JS function if not already there
    if 'filterFromHeader' not in content and OLD_JS_MARKER in content:
        content = content.replace(OLD_JS_MARKER, JS_FILTER_FUNCTION)
        changed = True

    if changed:
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
