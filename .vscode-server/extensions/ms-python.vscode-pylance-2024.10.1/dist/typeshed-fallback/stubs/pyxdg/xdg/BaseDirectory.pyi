from _typeshed import StrPath
from collections.abc import Iterator

xdg_data_home: str
xdg_data_dirs: list[str]
xdg_config_home: str
xdg_config_dirs: list[str]
xdg_cache_home: str
xdg_state_home: str

def save_config_path(*resource: StrPath) -> str: ...
def save_data_path(*resource: StrPath) -> str: ...
def save_cache_path(*resource: StrPath) -> str: ...
def save_state_path(*resource: StrPath) -> str: ...
def load_config_paths(*resource: StrPath) -> Iterator[str]: ...
def load_first_config(*resource: StrPath) -> str: ...
def load_data_paths(*resource: StrPath) -> Iterator[str]: ...
def get_runtime_dir(strict: bool = True) -> str: ...
