"""Fix navigation buttons in all route pages."""
import os
import re
from pathlib import Path

ROUTES_DIR = Path(__file__).parent / "routes"

# Old pages-nav pattern to replace
OLD_NAV_PATTERN = r'''<div class="pages-nav">
        <a href="\.\./dashboard_mobile\.html">
            <span class="nav-icon">🌐</span>
            <span>Dashboard</span>
        </a>
        <a href="\.\./mobile\.html" class="active">
            <span class="nav-icon">📊</span>
            <span>Report</span>
        </a>
        <a href="\.\./archive/">
            <span class="nav-icon">📁</span>
            <span>Archive</span>
        </a>
    </div>'''

# New pages-nav with correct links
NEW_NAV = '''<div class="pages-nav">
        <a href="../">
            <span class="nav-icon">🌐</span>
            <span>Dashboard</span>
        </a>
        <a href="https://flyaircairo-my.sharepoint.com/:f:/g/personal/dammam_to_aircairo_com/IgDvjscVb3zPQ63E6oVxGyViAencC8ryBmR137Me_icPPRs?e=oNiSIH" target="_blank" style="background: #0078D4;">
            <span class="nav-icon">☁️</span>
            <span>OneDrive</span>
        </a>
        <a href="../archive/">
            <span class="nav-icon">📁</span>
            <span>Archive</span>
        </a>
    </div>'''

def fix_route_file(file_path):
    """Fix navigation in a single route file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try exact match first
    if '../dashboard_mobile.html' in content and '../mobile.html' in content:
        # Replace the old nav section
        content = re.sub(OLD_NAV_PATTERN, NEW_NAV, content)

        # If regex didn't work, try string replacement
        if '../dashboard_mobile.html' in content:
            content = content.replace('../dashboard_mobile.html', '../')
        if '../mobile.html' in content:
            # Replace the Report link with OneDrive
            content = content.replace(
                '<a href="../mobile.html" class="active">',
                '<a href="https://flyaircairo-my.sharepoint.com/:f:/g/personal/dammam_to_aircairo_com/IgDvjscVb3zPQ63E6oVxGyViAencC8ryBmR137Me_icPPRs?e=oNiSIH" target="_blank" style="background: #0078D4;">'
            )
            content = content.replace(
                '<span class="nav-icon">📊</span>\n            <span>Report</span>',
                '<span class="nav-icon">☁️</span>\n            <span>OneDrive</span>'
            )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Fix all route files."""
    route_files = list(ROUTES_DIR.glob("*.html"))
    fixed = 0

    for route_file in route_files:
        if fix_route_file(route_file):
            print(f"Fixed: {route_file.name}")
            fixed += 1
        else:
            print(f"Skipped (already fixed or different format): {route_file.name}")

    print(f"\nTotal: {fixed}/{len(route_files)} files fixed")

if __name__ == "__main__":
    main()
