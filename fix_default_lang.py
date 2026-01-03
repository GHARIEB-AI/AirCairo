"""Change default language to English in all route pages."""
from pathlib import Path

ROUTES_DIR = Path(__file__).parent / "routes"

def fix_route_file(file_path):
    """Change default language to English in a single route file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Change body class from ar to en
    if '<body class="ar">' in content:
        content = content.replace('<body class="ar">', '<body class="en">')
        modified = True

    # Change lang-toggle button text from EN to AR
    if '>EN</button>' in content:
        content = content.replace('>EN</button>', '>AR</button>')
        modified = True

    if modified:
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
