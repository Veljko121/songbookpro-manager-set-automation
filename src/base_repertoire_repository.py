from abc import ABC, abstractmethod
from typing import List, Tuple

KEY_MAP = {
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
    
    def get_songs(self, spreadsheet_id: str, sheet_id: str, song_names_column: int, keys_column: int, notes_column: int) -> List[Tuple[str, int]]:
        """Template method that defines the algorithm structure."""
        self._validate_column_parameters(song_names_column, keys_column, notes_column)
        song_names, song_keys, song_notes = self._fetch_song_data(spreadsheet_id, sheet_id, song_names_column, keys_column, notes_column)
        songs = self._combine_song_data(song_names, song_keys, song_notes)
        return self._process_song_data(songs)
    
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
    def get_sheets(self, spreadsheet_id: str):
        """Fetch the sheet names for a given spreadsheet."""
        pass
    
    @abstractmethod
    def _fetch_song_data(self, spreadsheet_id: str, sheet_id: str, song_names_column: int, keys_column: int, notes_column: int) -> Tuple[List[str], List[str], List[str]]:
        """Fetch the song names, keys and notes columns from the data source."""
        pass
    
    def _combine_song_data(self, song_names: List[str], song_keys: List[str], song_notes: List[str]) -> List[Tuple[str, str, str]]:
        songs = []
        for i in range(len(song_names)):
            name = song_names[i]
            key = song_keys[i]
            note = None
            if i < len(song_notes):
                if song_notes[i]:
                    note = song_notes[i]
            song = (name, key, note)
            songs.append(song)
        return songs
    
    def _process_song_data(self, songs: List[Tuple[str, str, str]]) -> List[Tuple[str, int, str]]:
        enumerated_songs = {}
        for i, song in enumerate(songs):
            if song[0]:
                enumerated_songs[i] = song

        row_ids_with_error = []
        for id, song in enumerated_songs.items():
            try:
                KEY_MAP[song[1]]
            except KeyError:
                row_ids_with_error.append(id)
        
        if len(row_ids_with_error) > 0:
            raise ValueError(f"Key errors in rows: {[row + 1 for row in row_ids_with_error]}.")
        
        processed = []
        for song in enumerated_songs.values():
            name = format_song_name(song[0])
            key = song[1].strip()
            note = song[2]
            processed.append((name, KEY_MAP[key], note))

        return processed
