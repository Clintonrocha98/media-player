import tkinter as tk

class MusicList:
    def __init__(self, root):
        self.__listbox = tk.Listbox(root, width=40, height=15)
        self.__listbox.grid(row=0,column=1,pady=10)
        
    def add_music(self, path):
        if not self.is_music_in_list(path):
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

    def is_music_in_list(self, path):
        items = self.__listbox.get(0, tk.END)
        return path in items