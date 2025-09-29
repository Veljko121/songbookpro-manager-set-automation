class Service:

    def __init__(self, song_repository, set_repository):
        self.song_repository = song_repository
        self.set_repository = set_repository

    # 1. load song names from the repertoire
    # 2. find songs from the database by those names (check if each one exists)

    def create_set(self, sheet: str, set_name: str):
        database_songs = self.song_repository.find_songs_by_names()