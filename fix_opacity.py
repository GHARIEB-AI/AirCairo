"""Fix scroll buttons: 20% opacity, 80% on hover/press, gap 30px"""
import os

ROUTES_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes"
ARCHIVE_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\archive"

def fix_scroll_buttons(content):
    """Update scroll button CSS for 20% opacity and 30px gap"""

    # Fix gap in scroll-nav
    content = content.replace('gap: 20px;', 'gap: 30px;')
    content = content.replace('gap: 8px;', 'gap: 30px;')

    # Fix background opacity: 0.4 -> 0.2
    content = content.replace('background: rgba(70, 43, 115, 0.4);', 'background: rgba(70, 43, 115, 0.2);')
    content = content.replace('background: rgba(70, 43, 115, 0.1);', 'background: rgba(70, 43, 115, 0.2);')

    # Fix border opacity: 0.4 -> 0.2
    content = content.replace('border: 2px solid rgba(247, 148, 29, 0.4);', 'border: 2px solid rgba(247, 148, 29, 0.2);')
    content = content.replace('border: 2px solid rgba(247, 148, 29, 0.3);', 'border: 2px solid rgba(247, 148, 29, 0.2);')

    # Fix hover background: keep 0.8
    # Already correct in most files

    # Fix active/pressed background
    content = content.replace('background: rgba(247, 148, 29, 0.3);', 'background: rgba(247, 148, 29, 0.8);')

    return content

def fix_routes():
    count = 0
    for filename in os.listdir(ROUTES_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(ROUTES_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = fix_scroll_buttons(content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
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

            new_content = fix_scroll_buttons(content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Fixed: {filename}")

    print(f"\nFixed {count} archive files")

if __name__ == "__main__":
    print("=== Fixing Routes ===")
    fix_routes()

    print("\n=== Fixing Archive ===")
    fix_archive()

    print("\n=== Done ===")
