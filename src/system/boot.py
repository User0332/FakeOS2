import os
import sys
from fs import manager as fsctl
from process import Process

# TODO: change all cwds to default root-starting since they are, change all os funcs to do this too (this will allow massive refactor for cd and others)

os.chdir(os.path.dirname(sys.argv[0])) # set context in src/
os.chdir("..")

fakesys = Process(lambda x: None, {}, 0, 0, "", '/')

fsobj = fsctl.load()
fsctl.globalfsobj = fsobj

sys_path = fsctl.get_file_content(fakesys, "/cfg/env/syspath").decode().split(';')

print(sys_path)

# TODO: file permissions, login as actual user first

while 1:
	cmd = input(f"root@fakeos2:{fakesys.cwd}> ").split()

	if len(cmd) < 1:
		continue

	if cmd[0] == "cd":
		if len(cmd) < 2:
			print("Need a second arg for 'cd'")
			continue

		target_dir = cmd[1].removesuffix('/')

		if target_dir == '': # actually '/' but removesuffix'd
			fakesys.cwd = '/'
			continue

		if target_dir == '.': continue
		if target_dir == "..":
			if fakesys.cwd == '/': continue

			fakesys.cwd = '/'.join(fakesys.cwd.split('/')[:-1])

			if not fakesys.cwd: fakesys.cwd = '/'

			continue

		if target_dir.startswith('/'):
			if fsctl.dir_exists(target_dir):
				fakesys.cwd = target_dir
				continue

			print("Invalid Directory!")
			continue
		
		if fakesys.cwd == '/':
			if fsctl.dir_exists(fakesys.cwd+target_dir):
				fakesys.cwd+=target_dir
				continue
			
			print("Invalid Directory!")
			continue

		if fsctl.dir_exists(f"{fakesys.cwd}/{target_dir}"):
			fakesys.cwd+=f"/{target_dir}"
			continue

		print("Invalid Directory!")
		continue

	# for path in sys_path:
	# 	if (path+cmd[0]) [exists]:
