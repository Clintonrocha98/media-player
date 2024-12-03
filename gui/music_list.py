import tkinter as tk

class MusicList:
    def __init__(self, root):
        self.root = root
        self._create_widgets()

    def _create_widgets(self):
        self.__listbox = tk.Listbox(self.root, width=50, height=15)
        self.__listbox.pack(pady=10)


    def add_music(self, path):
      self.__listbox.insert(tk.END, path)

    def clear_list(self):
        self.__listbox.delete(0, tk.END)

    def highlight_playing(self, music_name):
        """Destaque a música atualmente sendo reproduzida na caixa de listagem."""
       
        self.__listbox.selection_clear(0, tk.END)
        items = self.__listbox.get(0, tk.END)

        index = items.index(music_name)
        self.__listbox.selection_set(index)
        self.__listbox.activate(index)
