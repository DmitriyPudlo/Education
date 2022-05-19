class Track:
    def __init__(self, name, time):
        self.name = str(name)
        self.time = int(time)

    def show(self):
        return f'{self.name} - {self.time}'


class Album:
    def __init__(self, name, group):
        self.name = str(name)
        self.group = str(group)
        self.list_song = []

    def get_tracks(self):
        for song in self.list_song:
            print(song.show())

    def add_track(self, track):
        if isinstance(track, Track):
            self.list_song.append(track)
        else:
            print('Введите данные о треке в верном формате')

    def get_duration(self):
        list_time = [song.time for song in self.list_song]
        return sum(list_time)


steal_is_album = Album('Steal This Album!', 'System of a Down')
boom = Track('Boom!', 5)
add = Track('A.D.D.', 3)
mr_jack = Track('Mr.Jack', 4)

steal_is_album.add_track(boom)
steal_is_album.add_track(mr_jack)

steal_is_album.get_tracks()
print(steal_is_album.get_duration())