from .music import Music
import random

class PlayList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.current = None

    def add_music(self, name):
        """Adiciona uma música no final da playlist, se ela ainda não existir."""
        if self.find_music(name):
            print(f"A música '{name}' já está na playlist.")
            return 
        
        new_music = Music(name)

        if not self.head:
            self.head = self.tail = new_music
        else:
            self.tail.next = new_music
            new_music.prev = self.tail
            self.tail = new_music

    def find_music(self, name):
        current = self.head
    
        while current:
            if current.name == name:
                return current
            current = current.next
        return None

    def next_music(self): 
        if not self.current:
            self.current = self.head
            return self.current.name if self.current else None

        if self.current.next:
            self.current = self.current.next
            return self.current.name
        else:
            return None
  
    def prev_music(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.name
        elif self.current:
            self.current = self.tail
            return self.current.name
        return None 

    def shuffle_playlist(self):
        songs = []
        current = self.head
        current_song_name = self.current.name if self.current else None 

        while current:
            songs.append(current.name)
            current = current.next

        random.shuffle(songs)

        self.head = self.tail = None
        for song in songs:
            self.add_music(song)

        if current_song_name:
            self.current = self.find_music(current_song_name)