from typing import Protocol

class OSRequest(Protocol):
	def write(fd: int, data: bytes): pass
	def get_procinfo(): pass