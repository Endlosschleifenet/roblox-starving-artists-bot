# Use PyInstaller to create a standalone executable for bot.py

mkdir -p executables

pyinstaller --onefile --distpath executables bot.py
pyinstaller --onefile --distpath executables coordinates-finder.py
rm -rf build dist *.spec
