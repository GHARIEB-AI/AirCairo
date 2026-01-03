"""Make scroll buttons transparent in all PC archive reports"""
import os
import re

ARCHIVE_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\archive"

OLD_SCROLL_STYLE = '''.scroll-btn {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: none;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: rgba(255, 255, 255, 0.8);
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
            transition: transform 0.15s, box-shadow 0.15s, background 0.15s, opacity 0.15s;
            opacity: 0.4;
        }

        .scroll-btn:hover {
            opacity: 1;
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.5);
        }

        .scroll-btn:active,
        .scroll-btn.pressed {
            opacity: 1;
            transform: scale(0.92);
            box-shadow: 0 4px 15px rgba(247, 148, 29, 0.5);
            background: linear-gradient(135deg, #F7941D 0%, #e8850a 100%);
        }

        .scroll-btn.end {
            background: linear-gradient(135deg, #F7941D 0%, #e8850a 100%);
        }

        .scroll-btn.end:hover {
            opacity: 1;
            box-shadow: 0 4px 15px rgba(247, 148, 29, 0.5);
        }'''

NEW_SCROLL_STYLE = '''.scroll-btn {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: 2px solid rgba(247, 148, 29, 0.3);
            background: rgba(70, 43, 115, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            color: rgba(70, 43, 115, 0.7);
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.15s, box-shadow 0.15s, background 0.15s, opacity 0.15s;
        }

        .scroll-btn:hover {
            background: rgba(70, 43, 115, 0.2);
            border-color: rgba(247, 148, 29, 0.6);
            transform: scale(1.1);
            box-shadow: 0 4px 15px rgba(70, 43, 115, 0.2);
        }

        .scroll-btn:active,
        .scroll-btn.pressed {
            transform: scale(0.92);
            background: rgba(247, 148, 29, 0.3);
            border-color: rgba(247, 148, 29, 0.8);
        }

        .scroll-btn.end {
            background: rgba(70, 43, 115, 0.1);
            border: 2px solid rgba(247, 148, 29, 0.3);
        }

        .scroll-btn.end:hover {
            background: rgba(70, 43, 115, 0.2);
            border-color: rgba(247, 148, 29, 0.6);
            box-shadow: 0 4px 15px rgba(70, 43, 115, 0.2);
        }'''


def fix_archive_scroll():
    count = 0
    for filename in os.listdir(ARCHIVE_DIR):
        if filename.endswith('.html') and not filename.endswith('_mobile.html') and filename != 'index.html':
            filepath = os.path.join(ARCHIVE_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if OLD_SCROLL_STYLE in content:
                content = content.replace(OLD_SCROLL_STYLE, NEW_SCROLL_STYLE)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Fixed: {filename}")

    print(f"\nFixed {count} PC archive files")


if __name__ == "__main__":
    fix_archive_scroll()
