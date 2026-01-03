"""Fix threat overlay toggle for mobile routes and add to PC report"""
import os
import re

ROUTES_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\routes"
PC_REPORT = r"D:\CODERED\LAB\market_insights\AirCairo-Report\online_pc_report.html"
MOB_REPORT = r"D:\CODERED\LAB\market_insights\AirCairo-Report\online_mob_report.html"
ARCHIVE_DIR = r"D:\CODERED\LAB\market_insights\AirCairo-Report\archive"

# Fix 1: Update showAll() in mobile routes to remove overlay
def fix_mobile_routes():
    count = 0
    for filename in os.listdir(ROUTES_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(ROUTES_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Fix showAll to clear the threat overlay
            old_show_all = '''function showAll() {
            activeLevel = null;'''
            new_show_all = '''function showAll() {
            activeLevel = null;
            setThreatOverlay(null);'''

            if old_show_all in content and 'setThreatOverlay(null);' not in content:
                content = content.replace(old_show_all, new_show_all)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Fixed: {filename}")

    print(f"\nFixed {count} route files")

# Fix 2: Add threat overlay to PC report
def fix_pc_report():
    with open(PC_REPORT, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if setThreatOverlay is called in filterByThreatLevel
    if 'filterByThreatLevel(level)' in content and 'setThreatOverlay(level)' not in content.split('filterByThreatLevel')[1][:500]:
        # Add setThreatOverlay call at start of filterByThreatLevel function
        old_filter = '''function filterByThreatLevel(level) {
            const statCards = document.querySelectorAll('.stat-card');'''
        new_filter = '''function filterByThreatLevel(level) {
            // Update visual overlay
            if (currentThreatFilter === level) {
                setThreatOverlay(null);
            } else {
                setThreatOverlay(level);
            }
            const statCards = document.querySelectorAll('.stat-card');'''

        content = content.replace(old_filter, new_filter)

        with open(PC_REPORT, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed: online_pc_report.html - added setThreatOverlay call")
    else:
        print("PC report already has setThreatOverlay or structure different")

# Fix 3: Fix mobile report if needed
def fix_mob_report():
    with open(MOB_REPORT, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Check if setThreatOverlay function exists
    if 'function setThreatOverlay' not in content:
        print("Mobile report missing setThreatOverlay function")
        return

    # Check filterByLevel function for overlay toggle
    if 'function filterByLevel(level)' in content:
        # Add overlay removal in showAll
        old_show_all = '''function showAll() {
            activeLevel = null;'''
        new_show_all = '''function showAll() {
            activeLevel = null;
            setThreatOverlay(null);'''

        if old_show_all in content and 'setThreatOverlay(null)' not in content:
            content = content.replace(old_show_all, new_show_all)
            modified = True

    if modified:
        with open(MOB_REPORT, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed: online_mob_report.html")
    else:
        print("Mobile report already fixed or structure different")

# Fix 4: Fix archive reports
def fix_archive_reports():
    count = 0
    for filename in os.listdir(ARCHIVE_DIR):
        if filename.endswith('.html') and filename != 'index.html':
            filepath = os.path.join(ARCHIVE_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            modified = False

            # For PC archive reports - add setThreatOverlay to filterByThreatLevel
            if 'filterByThreatLevel(level)' in content:
                old_filter = '''function filterByThreatLevel(level) {
            const statCards = document.querySelectorAll('.stat-card');'''
                new_filter = '''function filterByThreatLevel(level) {
            // Update visual overlay
            if (currentThreatFilter === level) {
                setThreatOverlay(null);
            } else {
                setThreatOverlay(level);
            }
            const statCards = document.querySelectorAll('.stat-card');'''

                if old_filter in content and 'setThreatOverlay(level)' not in content.split('filterByThreatLevel')[1][:500]:
                    content = content.replace(old_filter, new_filter)
                    modified = True

            # For mobile archive reports - add showAll fix
            if 'function filterByLevel(level)' in content:
                old_show_all = '''function showAll() {
            activeLevel = null;'''
                new_show_all = '''function showAll() {
            activeLevel = null;
            setThreatOverlay(null);'''

                if old_show_all in content and 'setThreatOverlay(null)' not in content:
                    content = content.replace(old_show_all, new_show_all)
                    modified = True

            if modified:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Fixed: {filename}")

    print(f"\nFixed {count} archive files")

if __name__ == "__main__":
    print("=== Fixing Mobile Routes ===")
    fix_mobile_routes()

    print("\n=== Fixing PC Report ===")
    fix_pc_report()

    print("\n=== Fixing Mobile Report ===")
    fix_mob_report()

    print("\n=== Fixing Archive Reports ===")
    fix_archive_reports()

    print("\n=== Done ===")
