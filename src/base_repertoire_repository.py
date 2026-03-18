from abc import ABC, abstractmethod
from typing import List, Tuple

keys = {
    "A"  :  0,
    "B"  :  1,
    "H"  :  2,
    "C"  :  3,
    "Db" :  4, "C#" :  4,
    "D"  :  5,
    "Eb" :  6, "D#" :  6,
    "E"  :  7,
    "F"  :  8,
    "F#" :  9, "Gb" :  9,
    "G"  : 10,
    "Ab" : 11, "G#" : 11, 
    "F#m": 12, "Gbm": 12,
    "Gm" : 13,
    "G#m": 14, "Abm": 14,
    "Am" : 15,
    "Bm" : 16,
    "Hm" : 17,
    "Cm" : 18,
    "C#m": 19, "Dbm": 19,
    "Dm" : 20,
    "D#m": 21, "Ebm": 21,
    "Em" : 22,
    "Fm" : 23,

    "None" : -1,
}

def format_song_name(name: str):
    return name.strip().replace("‘", "'").replace("’", "'")

class BaseRepertoireRepository(ABC):
    
    def get_songs(self, song_names_column: int, keys_column: int, notes_column: int) -> List[Tuple[str, int]]:
        """Template method that defines the algorithm structure."""
        self._validate_column_parameters(song_names_column, keys_column, notes_column)
        song_names, song_keys, notes = self._fetch_columns(song_names_column, keys_column, notes_column)
        return self._process_song_data(song_names, song_keys, notes)
    
    def _validate_column_parameters(self, song_names_column: int, keys_column: int, notes_column: int):
        """Validate that column parameters are valid."""
        if song_names_column <= 0:
            raise ValueError(f"Song names column value must be greater than 0 ({song_names_column}).")
        if keys_column <= 0:
            raise ValueError(f"Keys column value must be greater than 0 ({keys_column}).")
        if notes_column <= 0:
            raise ValueError(f"Notes column value must be greater than 0 ({notes_column}).")
        if song_names_column == keys_column:
            raise ValueError(f"Song names column value ({song_names_column}) and keys column value ({keys_column}) cannot be the same.")
        if song_names_column == notes_column:
            raise ValueError(f"Song names column value ({song_names_column}) and notes column value ({notes_column}) cannot be the same.")
        if keys_column == notes_column:
            raise ValueError(f"Keys column value ({keys_column}) and notes column value ({notes_column}) cannot be the same.")
    
    @abstractmethod
    def _fetch_columns(self, song_names_column: int, keys_column: int, notes_column: int) -> Tuple[List[str], List[str], List[str]]:
        """Fetch the song names, keys and notes columns from the data source."""
        pass
    
    def _process_song_data(self, song_names: List[str], song_keys: List[str], notes: List[str]) -> List[Tuple[str, int, str]]:
        enumerated_rows = {}
        for i, row in enumerate(zip(song_names, song_keys, notes)):
            if row[0]:
                enumerated_rows[i] = row

        row_ids_with_error = []
        for id, row in enumerated_rows.items():
            try:
                keys[row[1]]
            except KeyError:
                row_ids_with_error.append(id)
        
        if len(row_ids_with_error) > 0:
            raise ValueError(f"Key errors in rows: {[row + 1 for row in row_ids_with_error]}.")
        
        songs = []
        for _, row in enumerated_rows.items():
            song_name = format_song_name(row[0])
            key = row[1].strip()
            note = row[2]
            songs.append((song_name, keys[key], note))
        
        return songs