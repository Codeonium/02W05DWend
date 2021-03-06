class Room:
    def __init__(self, name, room_number, songs, guests_in, space):
        self.name = name
        self.room_number = room_number
        self.songs = songs
        self.guests_in = guests_in
        self.space = space

    def add_song_to_room(self, rooms, song):    
        self.songs.append(song)

    def add_guest_to_room(self,rooms, guest):
        self.guests_in.append(guest)
        
    def guests_in_room(self, room):
        return len(self.guests_in)

    def number_of_songs_in_room(self, room):
        return len(self.songs)