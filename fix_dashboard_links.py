"""Fix Dashboard links in route pages to point to mobile dashboard."""
from pathlib import Path

ROUTES_DIR = Path(__file__).parent / "routes"

def fix_route_file(file_path):
    """Fix Dashboard link in a single route file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if this file has the pages-nav with href="../"
    if 'href="../">' in content and 'pages-nav' in content:
        # Replace Dashboard link to point to mobile dashboard
        content = content.replace(
            '<a href="../">',
            '<a href="../online_mobile_dashboard.html">'
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
            print(f"Skipped: {route_file.name}")

    print(f"\nTotal: {fixed}/{len(route_files)} files fixed")

if __name__ == "__main__":
    main()
