class Track:
    def __init__(self, name, time):
        self.name = str(name)
        self.time = int(time)

    def __str__(self):
        return f'{self.name} - {self.time} min'


class Album:
    def __init__(self, name, group):
        self.name = str(name)
        self.group = str(group)
        self.list_song = []

    def get_tracks(self):
        return '\n'.join([song.__str__() for song in self.list_song])

    def add_track(self, track):
        if isinstance(track, Track):
            self.list_song.append(track)
        else:
            print('Введите данные о треке в верном формате')

    def get_duration(self):
        list_time = [song.time for song in self.list_song]
        return f'{sum(list_time)} min'

    def __str__(self):
        return f'''
Name group: {self.group}
Name album: '{self.name}'
Tracks:
{self.get_tracks()}
'''


steal_is_album = Album('Steal This Album!', 'System of A Down')
boom = Track('Boom!', 5)
add = Track('A.D.D.', 3)
mr_jack = Track('Mr.Jack', 4)

steal_is_album.add_track(boom)
steal_is_album.add_track(add)
steal_is_album.add_track(mr_jack)

print(steal_is_album.get_tracks())

print(steal_is_album.get_duration())

print(boom)

print(steal_is_album)