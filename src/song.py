class Song:
    def __init__(self, id: int, name: str, key: int, subtitle: str, key_shift: int):
        self.id = id
        self.name = name
        self.key = key
        self.subtitle = subtitle
        self.key_shift = key_shift

    def active_key(self):
        key = self.key + self.key_shift
        if self.key <= 11:
            key %= 12
        else:
            if key >= 24:
                key -= 12
        return key