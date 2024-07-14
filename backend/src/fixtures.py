from injector import Injector

# noinspection PyProtectedMember
from config.containers import _init_container


def init_dummy_container() -> Injector:
    return _init_container()
