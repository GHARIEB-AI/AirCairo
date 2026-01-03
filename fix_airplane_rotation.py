"""Fix airplane rotation: change from horizontal to vertical"""
import os

ROUTES_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes"
ARCHIVE_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\archive"

def fix_rotation(content):
    """Change rotation from -90/90 to 0/180 for vertical airplane"""
    # For scroll up button: -90 -> 0
    content = content.replace('transform="rotate(-90 12 12)"', 'transform="rotate(0 12 12)"')
    # For scroll down button: 90 -> 180
    content = content.replace('transform="rotate(90 12 12)"', 'transform="rotate(180 12 12)"')
    return content

def fix_routes():
    count = 0
    for filename in os.listdir(ROUTES_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(ROUTES_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'rotate(-90 12 12)' in content or 'rotate(90 12 12)' in content:
                content = fix_rotation(content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Fixed: {filename}")

    print(f"\nFixed {count} route files")

def fix_archive():
    count = 0
    for filename in os.listdir(ARCHIVE_DIR):
        if filename.endswith('.html') and filename != 'index.html':
            filepath = os.path.join(ARCHIVE_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'rotate(-90 12 12)' in content or 'rotate(90 12 12)' in content:
                content = fix_rotation(content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Fixed: {filename}")

    print(f"\nFixed {count} archive files")

if __name__ == "__main__":
    print("=== Fixing Routes ===")
    fix_routes()

    print("\n=== Fixing Archive ===")
    fix_archive()

    print("\n=== Done ===")
