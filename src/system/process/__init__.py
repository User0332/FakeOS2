from dataclasses import dataclass
from system.osrequest import OSRequest
from typing import Callable
from fs import FDEntry

@dataclass
class Process:
	entry: Callable[[OSRequest], int]
	fd_table: dict[int, FDEntry]
	pid: int
	ppid: int
	cmd: str
	cwd: str