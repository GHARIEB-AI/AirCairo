"""
Fix scroll buttons in all route pages.
Issue: btn.replaceWith() loses the reference, getElementById returns null.
Solution: Simpler approach without replacing nodes.
"""
import os
from pathlib import Path

ROUTES_DIR = Path(r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes")

# The broken scroll button code pattern
OLD_SCROLL_CODE = '''    <script>
        // ==================== SCROLL BUTTONS ====================
        // Tap = jump to top/bottom, Hold = slow scroll
        let holdTimer = null;
        let scrollInterval = null;
        let isScrolling = false;

        function setupScrollButton(btn, direction) {
            if (!btn) return;

            const jumpTo = direction === 'up' ? 0 : document.documentElement.scrollHeight;
            const scrollAmount = direction === 'up' ? -150 : 150;

            const startHandler = (e) => {
                e.preventDefault();
                isScrolling = false;

                // After 300ms of holding, start slow scroll
                holdTimer = setTimeout(() => {
                    isScrolling = true;
                    scrollInterval = setInterval(() => {
                        window.scrollBy({ top: scrollAmount, behavior: 'auto' });
                    }, 80);
                }, 300);
            };

            const endHandler = (e) => {
                e.preventDefault();
                clearTimeout(holdTimer);

                // If NOT scrolling (released before 300ms), it's a TAP - jump
                if (!isScrolling) {
                    window.scrollTo({ top: jumpTo, behavior: 'smooth' });
                }

                if (scrollInterval) {
                    clearInterval(scrollInterval);
                    scrollInterval = null;
                }
                isScrolling = false;
                holdTimer = null;
            };

            // Remove old listeners first
            btn.replaceWith(btn.cloneNode(true));
            btn = document.getElementById(btn.id);

            btn.addEventListener('touchstart', startHandler, { passive: false });
            btn.addEventListener('touchend', endHandler);
            btn.addEventListener('touchcancel', endHandler);
            btn.addEventListener('mousedown', startHandler);
            btn.addEventListener('mouseup', endHandler);
            btn.addEventListener('mouseleave', endHandler);
        }

        // Initialize scroll buttons
        const scrollUpBtn = document.getElementById('scrollUp');
        const scrollDownBtn = document.getElementById('scrollDown');
        if (scrollUpBtn) setupScrollButton(scrollUpBtn, 'up');
        if (scrollDownBtn) setupScrollButton(scrollDownBtn, 'down');'''

# Fixed scroll button code - simpler, no replaceWith
NEW_SCROLL_CODE = '''    <script>
        // ==================== SCROLL BUTTONS ====================
        // Tap = jump to top/bottom, Hold = slow scroll
        (function() {
            let holdTimer = null;
            let scrollInterval = null;
            let isHolding = false;

            function setupScrollButton(btnId, direction) {
                const btn = document.getElementById(btnId);
                if (!btn) return;

                const jumpTo = direction === 'up' ? 0 : document.documentElement.scrollHeight;
                const scrollAmount = direction === 'up' ? -150 : 150;

                function startPress(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    isHolding = false;

                    holdTimer = setTimeout(function() {
                        isHolding = true;
                        scrollInterval = setInterval(function() {
                            window.scrollBy(0, scrollAmount);
                        }, 80);
                    }, 300);
                }

                function endPress(e) {
                    e.preventDefault();
                    e.stopPropagation();

                    if (holdTimer) {
                        clearTimeout(holdTimer);
                        holdTimer = null;
                    }

                    if (scrollInterval) {
                        clearInterval(scrollInterval);
                        scrollInterval = null;
                    }

                    // If NOT holding (quick tap), jump to top/bottom
                    if (!isHolding) {
                        window.scrollTo({ top: jumpTo, behavior: 'smooth' });
                    }
                    isHolding = false;
                }

                // Touch events
                btn.addEventListener('touchstart', startPress, { passive: false });
                btn.addEventListener('touchend', endPress, { passive: false });
                btn.addEventListener('touchcancel', endPress, { passive: false });

                // Mouse events (for desktop testing)
                btn.addEventListener('mousedown', startPress);
                btn.addEventListener('mouseup', endPress);
                btn.addEventListener('mouseleave', function() {
                    if (holdTimer) clearTimeout(holdTimer);
                    if (scrollInterval) clearInterval(scrollInterval);
                    holdTimer = null;
                    scrollInterval = null;
                    isHolding = false;
                });
            }

            // Initialize when DOM is ready
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', function() {
                    setupScrollButton('scrollUp', 'up');
                    setupScrollButton('scrollDown', 'down');
                });
            } else {
                setupScrollButton('scrollUp', 'up');
                setupScrollButton('scrollDown', 'down');
            }
        })();'''

def fix_file(filepath):
    """Fix scroll buttons in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if OLD_SCROLL_CODE in content:
        content = content.replace(OLD_SCROLL_CODE, NEW_SCROLL_CODE)
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
