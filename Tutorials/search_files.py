from pathlib import Path

path = Path()
for file in path.glob('*.py'): # glob method searches for files or directories in current path. Here it is searching for .py files. * represents all files with .py extension.
    print(file)