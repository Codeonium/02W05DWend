class Room:
    def __init__(self, name, room_number, songs, space):
        self.name = name
        self.room_number = room_number
        self.songs = songs
        self.space = space

    def add_song_to_room(self, rooms, song):    
        self.songs.append(song)


    def number_of_songs_in_room(self, room):
        return len(self.songs)