"""
Add date filter button to all route pages.
The button will be placed next to the HOME button.
"""
import os
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

# Find the HOME button line and add date filter button after it
OLD_HOME_BTN = '''    <div class="sticky-header">
        <a href="https://gharieb-ai.github.io/AirCairo/mobile.html" class="home-btn">HOME</a>
        <button class="lang-btn" onclick="toggleLang()">'''

NEW_HOME_BTN = '''    <div class="sticky-header">
        <a href="https://gharieb-ai.github.io/AirCairo/mobile.html" class="home-btn">HOME</a>
        <button class="date-filter-btn" onclick="openDateModal()">📅</button>
        <button class="lang-btn" onclick="toggleLang()">'''

def fix_file(filepath):
    """Add date filter button to a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if OLD_HOME_BTN in content and 'date-filter-btn' not in content[:5000]:
        content = content.replace(OLD_HOME_BTN, NEW_HOME_BTN)
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
