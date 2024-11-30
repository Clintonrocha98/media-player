from node import Node

class PlayList:
  def __init__(self):
    self.head = None
  
    def add_music(self, value):
        """Adiciona uma musica no final da playlist"""
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def all_musics(self):
        """retorna todas as musicas"""
        musics = []
        current = self.head
        while current: 
            musics.append(current.value)  
            current = current.next
        return musics

    def remove_music(self, value):
        """TODOLIST: acredito que dessa forma não deva funcionar, verifique posteriormente se com a estrutura da musica vá funcionar"""
        """remove uma musica da playlist"""
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next
