from typing import List
from set_item import SetItem

class Set:

    def __init__(self, name, items: List[SetItem]):
        self.name = name
        self.items = items