class Playlist:
    def __init__(self, name : str):
        self.name = name
        self.lst = []

    def add_song(self, song : str):
        self.lst.append(song)

f = Playlist("В потоке")
s = Playlist("My playlist")

f.add_song("Крид Сердцеедка")
s.add_song("Drake Nonstop")

print(f.name)
print(f.lst)
print(s.lst)