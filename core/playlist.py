from .node import Node

class PlayList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.current = None

    def add_music(self, data):
        """Adiciona uma musica no final da playlist"""
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def all_musics(self):
        """retorna todas as musicas"""
        musics = []
        current = self.head
        while current:
            musics.append(current.data)
            current = current.next
        return musics

    def remove_music(self, data):
        """Remove uma música específica da playlist."""
        current = self.head

        while current:
            if current.data == data:
                if current == self.head and current == self.tail:
                    self.head = self.tail = None
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return 
            current = current.next

    def next_music(self):
        if not self.current:
            self.current = self.head
            return self.current.data if self.current else None

        if self.current.next:
            self.current = self.current.next
            return self.current.data
        else:
            self.current = None
            return None

    def prev_music(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        elif self.current:
            return None
        else:
            self.current = self.tail
            return self.current.data if self.current else None

    def reset(self):
        self.current = self.head
