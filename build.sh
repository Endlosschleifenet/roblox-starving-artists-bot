# Check if the 'executables' directory does not exist and create it
[ ! -d "executables" ] && mkdir executables

# Use PyInstaller to create standalone executables
pyinstaller --onefile --distpath executables bot.py
pyinstaller --onefile --distpath executables coordinates-finder.py

# Clean up build artifacts
rm -rf build dist *.spec
