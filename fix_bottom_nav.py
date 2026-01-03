"""Fix bottom-nav position: change from bottom: 60px to bottom: 0"""
import os

ROUTES_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes"
ARCHIVE_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\archive"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix bottom-nav position
    if 'bottom: 60px;' in content:
        content = content.replace('bottom: 60px;', 'bottom: 0;')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def fix_routes():
    count = 0
    for filename in os.listdir(ROUTES_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(ROUTES_DIR, filename)
            if fix_file(filepath):
                count += 1
                print(f"Fixed: {filename}")
    print(f"\nFixed {count} route files")

def fix_archive():
    count = 0
    for filename in os.listdir(ARCHIVE_DIR):
        if filename.endswith('.html') and filename != 'index.html':
            filepath = os.path.join(ARCHIVE_DIR, filename)
            if fix_file(filepath):
                count += 1
                print(f"Fixed: {filename}")
    print(f"\nFixed {count} archive files")

if __name__ == "__main__":
    print("=== Fixing Routes ===")
    fix_routes()
    print("\n=== Fixing Archive ===")
    fix_archive()
    print("\n=== Done ===")
