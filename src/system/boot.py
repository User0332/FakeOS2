import os
import sys
import contextlib
import unittest.mock
from fs import manager as fsctl
from process import Process

os.chdir(os.path.dirname(sys.argv[0])) # set context in src/
os.chdir("..")

fakesys = Process(lambda x: None, {}, 0, 0, "", '/')

fsobj = fsctl.load()
fsctl.globalfsobj = fsobj

sys_path = fsctl.get_file_content(fakesys, "/cfg/env/syspath")

while 1:
	cmd = input().split()
