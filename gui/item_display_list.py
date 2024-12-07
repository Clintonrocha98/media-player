import tkinter as tk


class ItemDisplayList:
    def __init__(self):
        self.__listbox = None

    def set_frame(self, frame):
        self.__listbox = tk.Listbox(frame, width=40, height=15)
        self.set_position()

    def set_position(self, row=0, column=0):
        self.__listbox.grid(row=row, column=column)

    def add_to_list(self, path):
        if not self.is_music_in_list(path):
            self.__listbox.insert(tk.END, path)

    def clear_list(self):
        self.__listbox.delete(0, tk.END)

    def highlight_playing(self, music_name):
        """Destaque arquivo na caixa de listagem."""
        self.__listbox.selection_clear(0, tk.END)
        items = self.__listbox.get(0, tk.END)

        index = items.index(music_name)
        self.__listbox.selection_set(index)
        self.__listbox.activate(index)

    def is_music_in_list(self, path):
        items = self.__listbox.get(0, tk.END)
        return path in items

    def get_item_selected(self):
        selection = self.__listbox.curselection()

        if selection:
            index = selection[0]
            value = self.__listbox.get(index)
            return value

    def set_evento_on_select(self, event):
        value = self.get_item_selected()
        event(value)
