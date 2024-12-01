from _typeshed import ReadableBuffer
from typing import Any

from serial.serialutil import *

sab: Any  # IronPython object

def as_byte_array(string: bytes) -> Any: ...  # IronPython object

class Serial(SerialBase):
    def open(self) -> None: ...
    @property
    def in_waiting(self) -> int: ...
    def read(self, size: int = 1) -> bytes: ...
    def write(self, b: ReadableBuffer, /) -> int | None: ...
    def reset_input_buffer(self) -> None: ...
    def reset_output_buffer(self) -> None: ...
    @property
    def cts(self) -> bool: ...
    @property
    def dsr(self) -> bool: ...
    @property
    def ri(self) -> bool: ...
    @property
    def cd(self) -> bool: ...
