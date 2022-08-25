from abc import ABC
from typing import Dict


class Component(ABC):

    def __init__(self):
        pass

    def eval(self, instance: Dict[str, bool]) -> Dict[str, bool]:
        pass
