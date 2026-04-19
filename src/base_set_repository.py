from abc import ABC, abstractmethod
from set import Set
from set_item import SetItem
from typing import List

class BaseSetRepository(ABC):

    @abstractmethod
    def save(self, set: Set):
        pass