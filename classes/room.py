class Room:
    def __init__(self, name, room_number, songs, space):
        self.name = name
        self.room_number = room_number
        self.songs = songs
        self.space = space

    # def add_song_to_room(self, room, song):
    #     for room in self.room_number:
    #         if self.room_number == room:
    #             self.room.songs.append(song)


    def number_of_songs_in_room(self, room):
        return len(self.songs)