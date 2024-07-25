import os
from sys import argv
from fs import default_fs
from fs.manager import store

os.chdir(os.path.dirname(argv[0])) # set context in src/
os.chdir("..")

store(default_fs)

print("FakeOS 2 is installed! (remove install.py and run boot.py to launch)")