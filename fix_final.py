"""Final fix: scroll buttons 20% opacity, 80% on press, gap 40px"""
import os
import re

ROUTES_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes"
ARCHIVE_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\archive"
PC_REPORT = r"D:\CODERED\LAB\market_insights\AirCairo-Report\online_pc_report.html"

# New CSS for mobile scroll buttons
NEW_MOBILE_CSS = '''.scroll-nav {
            position: fixed;
            right: 15px;
            bottom: 140px;
            display: flex;
            flex-direction: column;
            gap: 40px;
            z-index: 99;
        }

        .scroll-btn {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            border: 2px solid rgba(247, 148, 29, 0.15);
            background: rgba(70, 43, 115, 0.15);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
            color: rgba(255, 255, 255, 0.5);
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.2s ease;
        }

        .scroll-btn:active, .scroll-btn.pressed {
            background: rgba(70, 43, 115, 0.8);
            border-color: rgba(247, 148, 29, 0.8);
            color: rgba(255, 255, 255, 1);
            transform: scale(0.95);
        }

        .scroll-btn svg {
            width: 22px;
            height: 22px;
        }'''

def fix_routes():
    """Fix all route files"""
    count = 0
    for filename in os.listdir(ROUTES_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(ROUTES_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find and replace the scroll CSS block
            pattern = r'\.scroll-nav \{[^}]+\}\s*\.scroll-btn \{[^}]+\}\s*\.scroll-btn:active[^}]+\}'

            if re.search(pattern, content):
                new_content = re.sub(pattern, NEW_MOBILE_CSS.replace('.scroll-btn svg {', '').strip().rstrip('}').rstrip(), content)

                # Also add svg style if not present
                if '.scroll-btn svg {' not in new_content:
                    new_content = new_content.replace(
                        '.scroll-btn:active, .scroll-btn.pressed {',
                        '''.scroll-btn svg {
            width: 22px;
            height: 22px;
        }

        .scroll-btn:active, .scroll-btn.pressed {'''
                    )

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
                print(f"Fixed: {filename}")
            else:
                # Try simpler replacements
                modified = False

                # Fix gap
                if 'gap: 30px;' in content:
                    content = content.replace('gap: 30px;', 'gap: 40px;')
                    modified = True
                if 'gap: 20px;' in content:
                    content = content.replace('gap: 20px;', 'gap: 40px;')
                    modified = True

                # Fix background to 15%
                content = content.replace('background: rgba(70, 43, 115, 0.2);', 'background: rgba(70, 43, 115, 0.15);')
                content = content.replace('background: rgba(70, 43, 115, 0.4);', 'background: rgba(70, 43, 115, 0.15);')

                # Fix border to 15%
                content = content.replace('border: 2px solid rgba(247, 148, 29, 0.2);', 'border: 2px solid rgba(247, 148, 29, 0.15);')
                content = content.replace('border: 2px solid rgba(247, 148, 29, 0.4);', 'border: 2px solid rgba(247, 148, 29, 0.15);')

                # Fix color
                content = content.replace('color: rgba(255, 255, 255, 0.8);', 'color: rgba(255, 255, 255, 0.5);')
                content = content.replace('color: rgba(255, 255, 255, 0.6);', 'color: rgba(255, 255, 255, 0.5);')

                # Fix active state - add full styling
                old_active = '.scroll-btn:active, .scroll-btn.pressed {\n            transform: scale(0.92);\n        }'
                new_active = '''.scroll-btn:active, .scroll-btn.pressed {
            background: rgba(70, 43, 115, 0.8);
            border-color: rgba(247, 148, 29, 0.8);
            color: rgba(255, 255, 255, 1);
            transform: scale(0.95);
        }'''
                if old_active in content:
                    content = content.replace(old_active, new_active)
                    modified = True

                # Also try without newline variations
                if 'transform: scale(0.92);' in content and 'background: rgba(70, 43, 115, 0.8);' not in content:
                    content = content.replace(
                        'transform: scale(0.92);',
                        '''background: rgba(70, 43, 115, 0.8);
            border-color: rgba(247, 148, 29, 0.8);
            color: rgba(255, 255, 255, 1);
            transform: scale(0.95);'''
                    )
                    modified = True

                if modified:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count += 1
                    print(f"Fixed (simple): {filename}")

    print(f"\nFixed {count} route files")

def fix_archive():
    """Fix all archive files"""
    count = 0
    for filename in os.listdir(ARCHIVE_DIR):
        if filename.endswith('.html') and filename != 'index.html':
            filepath = os.path.join(ARCHIVE_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            modified = False

            # Fix gap
            if 'gap: 30px;' in content:
                content = content.replace('gap: 30px;', 'gap: 40px;')
                modified = True
            if 'gap: 8px;' in content:
                content = content.replace('gap: 8px;', 'gap: 40px;')
                modified = True

            # Fix background to 15%
            if 'background: rgba(70, 43, 115, 0.2);' in content:
                content = content.replace('background: rgba(70, 43, 115, 0.2);', 'background: rgba(70, 43, 115, 0.15);')
                modified = True
            if 'background: rgba(70, 43, 115, 0.4);' in content:
                content = content.replace('background: rgba(70, 43, 115, 0.4);', 'background: rgba(70, 43, 115, 0.15);')
                modified = True

            # Fix border to 15%
            if 'border: 2px solid rgba(247, 148, 29, 0.2);' in content:
                content = content.replace('border: 2px solid rgba(247, 148, 29, 0.2);', 'border: 2px solid rgba(247, 148, 29, 0.15);')
                modified = True
            if 'border: 2px solid rgba(247, 148, 29, 0.4);' in content:
                content = content.replace('border: 2px solid rgba(247, 148, 29, 0.4);', 'border: 2px solid rgba(247, 148, 29, 0.15);')
                modified = True

            # Fix active state
            if 'transform: scale(0.92);' in content and 'background: rgba(70, 43, 115, 0.8);' not in content:
                content = content.replace(
                    'transform: scale(0.92);',
                    '''background: rgba(70, 43, 115, 0.8);
            border-color: rgba(247, 148, 29, 0.8);
            color: rgba(255, 255, 255, 1);
            transform: scale(0.95);'''
                )
                modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Fixed: {filename}")

    print(f"\nFixed {count} archive files")

def fix_pc_report():
    """Fix PC report"""
    with open(PC_REPORT, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Fix gap
    if 'gap: 30px;' in content:
        content = content.replace('gap: 30px;', 'gap: 40px;')
        modified = True

    # Fix background to 15%
    if 'background: rgba(70, 43, 115, 0.2);' in content:
        content = content.replace('background: rgba(70, 43, 115, 0.2);', 'background: rgba(70, 43, 115, 0.15);')
        modified = True

    # Fix border to 15%
    if 'border: 2px solid rgba(247, 148, 29, 0.2);' in content:
        content = content.replace('border: 2px solid rgba(247, 148, 29, 0.2);', 'border: 2px solid rgba(247, 148, 29, 0.15);')
        modified = True

    if modified:
        with open(PC_REPORT, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed: online_pc_report.html")

if __name__ == "__main__":
    print("=== Fixing PC Report ===")
    fix_pc_report()

    print("\n=== Fixing Routes ===")
    fix_routes()

    print("\n=== Fixing Archive ===")
    fix_archive()

    print("\n=== Done ===")
