import sys
import os

print(sys.argv)

print(sys.version)

print(sys.path)

sys.path.append('/Users/handsomehan/Python/flask')

print(sys.path)

print(sys.platform)

if sys.platform == "win32":
    os.system('dir')
else:
    os.system('ls')
