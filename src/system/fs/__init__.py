from dataclasses import dataclass
from typing import TypedDict

class FSType(TypedDict):
	dirs: dict[str, 'FSType']
	files: dict[str, bytes]

MODE_READ = 0
MODE_WRITE = 1
MODE_READWRITE = 2
MODE_UNKNOWN = 3

TYPE_FILE = 0
TYPE_PIPE = 1

@dataclass
class FDEntry:
	type: int
	path: str | None
	pipe_buf: bytes
	mode: int
	offset: int
	
EMPTY_DIR: FSType = {
	"dirs": {},
	"files": {}
}

default_fs: FSType = {
	"dirs": {
		"proc": { **EMPTY_DIR },
		"cfg": {
			"dirs": {
				"security": {
					"dirs": {},
					"files": {
						"passwd": b''
					}
				},
				"env": {
					"dirs": {},
					"files": {
						"syspath": b"/bin"
					}
				}
			},
			"files": {
			}
		},
		"home": { **EMPTY_DIR }
	},
	"files": {}
}