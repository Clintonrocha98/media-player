import tkinter as tk
from tkinter import ttk
from utils import rename_file,generate_playlist_filename


class EditPlaylistTreeview:
    def __init__(self):
        self.__root = None
        self.__playlist_name = None
        self.__entry = None
        self.__rename_button = None
        self.__tree = None

    def set_frame(self, root):
        self.__root = tk.Toplevel(root)
        self.__root.title("Editar playlist " + self.__playlist_name)
        self.__root.geometry("400x300")

        self.__entry = ttk.__Entry(self.__root)
        self.__entry.grid(row=0, column=0, sticky="nsew")
        self.__entry.insert(0, self.__playlist_name)

        self.__rename_button = ttk.Button(
            self.__root, text="Renomear", command=self.add_item
        )
        self.__rename_button.grid(row=0, column=1)

        self.__tree = ttk.Treeview(
            self.__root, columns=("Item", "Action"), show="headings"
        )
        self.__tree.heading("Item", text="Musica")
        self.__tree.heading("Action", text="Ação")
        self.__tree.grid(row=1, column=0, sticky="nsew")

        self.__tree.column("Item", stretch=tk.YES, anchor=tk.W)
        self.__tree.column("Action", width=100, anchor=tk.CENTER)

    def set_playlist_name(self, playlist_name):
        self.playlist_name = playlist_name

    def rename_playlist(self):
        new_name = self.__entry.get()
        if new_name:
            new_name = generate_playlist_filename(new_name)
            rename_file(self.__playlist_name, new_name)
            self.__playlist_name = new_name
        pass

    def add_item(self):
        item_text = self.__entry.get()
        if item_text:
            item_id = self.tree.insert("", tk.END, values=(item_text, "Apagar"))
            self.tree.set(item_id, column="Action", value="Apagar")
            self.tree.item(item_id, tags=item_id)
            self.tree.tag_bind(
                item_id, "<Button-1>", lambda event, id=item_id: self.delete_item(id)
            )
            self.__entry.delete(0, tk.END)

    def delete_item(self, item_id):
        self.tree.delete(item_id)
