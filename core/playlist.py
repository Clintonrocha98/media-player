from .node import Node

class PlayList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.current = None

    def add_music(self, data):
        """Adiciona uma música no final da playlist, se ela ainda não existir."""
        if self.find_music(data):
            print(f"A música '{data}' já está na playlist.")
            return 
        
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_music(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def next_music(self): 
        if not self.current:
            self.current = self.head
            return self.current.data if self.current else None

        if self.current.next:
            self.current = self.current.next
            return self.current.data
        else:
            return None
  
    def prev_music(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        elif self.current:
            self.current = self.tail
            return self.current.data
        return None 

    def reset(self):
        self.current = self.head
