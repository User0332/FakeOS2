from process import Process
from . import MODE_READ, MODE_READWRITE, TYPE_FILE, FDEntry, FSType
import dill

def load() -> FSType:
	return dill.load(open("disk/serialized", "rb"))

def store(fs: FSType) -> None:
	dill.dump(fs, open("disk/serialized", "wb"))

globalfsobj: FSType

def get_dir(path: str) -> FSType:
	parts = path.split('/')

	if parts[0] != '': raise ValueError("invalid call to get_dir")

	parts = parts[1:]

	working_dir: FSType = globalfsobj

	for part in parts:
		working_dir = working_dir["dirs"][part]

	return working_dir

def dir_exists(path: str) -> bool:
	try: get_dir(path)
	except KeyError: return False

	return True	

def get_file_content(caller: Process, path: str) -> bytes:
	parts = path.split('/')

	if parts[0] == '':
		return get_dir('/'.join(parts[:-1]))["files"][parts[-1]]
	else:
		return get_dir(caller.cwd + '/' + '/'.join(parts[:-1]))["files"][parts[-1]]


def read(caller: Process, fd: FDEntry) -> tuple[int, bytes]:
	if fd.mode not in (MODE_READ, MODE_READWRITE): return (-1, b'')

	if fd.type == TYPE_FILE: return (0, get_file_content(globalfsobj, fd.path))

	# it is a pipe
	return (0, fd.pipe_buf)