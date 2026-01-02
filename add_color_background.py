"""
Add background color change when color filter is selected.
- HIGH (red) -> light red background
- MEDIUM (yellow) -> light yellow background
- LOW (green) -> light green background
- ALL -> default background
"""
import os
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

# Find the filterByColor function and add background change
OLD_FILTER_FUNCTION = '''        function filterByColor(level) {
            activeColorFilter = level;
            const dateSections = document.querySelectorAll('[data-date]');

            dateSections.forEach(section => {
                const cards = section.querySelectorAll('.threat-card');
                let hasVisibleCard = false;

                cards.forEach(card => {
                    if (level === 'all') {
                        card.classList.remove('hidden');
                        hasVisibleCard = true;
                    } else {
                        const isMatch = card.classList.contains(level);
                        card.classList.toggle('hidden', !isMatch);
                        if (isMatch) hasVisibleCard = true;
                    }
                });

                // Hide entire date section if no visible cards
                if (level !== 'all') {
                    section.classList.toggle('hidden', !hasVisibleCard);
                }
            });

            updateFilteredStats();
            highlightActiveColorBtn(level);
        }'''

NEW_FILTER_FUNCTION = '''        function filterByColor(level) {
            activeColorFilter = level;
            const dateSections = document.querySelectorAll('[data-date]');

            dateSections.forEach(section => {
                const cards = section.querySelectorAll('.threat-card');
                let hasVisibleCard = false;

                cards.forEach(card => {
                    if (level === 'all') {
                        card.classList.remove('hidden');
                        hasVisibleCard = true;
                    } else {
                        const isMatch = card.classList.contains(level);
                        card.classList.toggle('hidden', !isMatch);
                        if (isMatch) hasVisibleCard = true;
                    }
                });

                // Hide entire date section if no visible cards
                if (level !== 'all') {
                    section.classList.toggle('hidden', !hasVisibleCard);
                }
            });

            // Change page background color based on filter
            const bgColors = {
                'all': 'linear-gradient(135deg, #f5f3f9 0%, #ebe7f3 100%)',
                'high': 'linear-gradient(135deg, #fff5f5 0%, #ffe8e8 100%)',
                'medium': 'linear-gradient(135deg, #fffbf0 0%, #fff3e0 100%)',
                'low': 'linear-gradient(135deg, #f0fff4 0%, #e8f5e9 100%)'
            };
            document.body.style.background = bgColors[level] || bgColors['all'];

            updateFilteredStats();
            highlightActiveColorBtn(level);
        }'''

def fix_file(filepath):
    """Add background color change to filter function."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if OLD_FILTER_FUNCTION in content:
        content = content.replace(OLD_FILTER_FUNCTION, NEW_FILTER_FUNCTION)
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
