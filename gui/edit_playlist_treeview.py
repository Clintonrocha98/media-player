import tkinter as tk
from tkinter import ttk
from utils import (
    rename_file,
    generate_playlist_filename,
    remove_song_by_name,
    read_paths_from_file,
    format_music_filename,
)


class EditPlaylistTreeview:
    def __init__(self):
        self.__root = None
        self.__playlist_name = None
        self.__entry = None
        self.__rename_button = None
        self.__update_playlist_ui_function = None

    def set_frame(self, root):
        self.__root = tk.Toplevel(root)
        self.__root.title("Editar playlist " + self.__playlist_name)
        self.__root.geometry("400x300")
        self.__frame = tk.Frame(self.__root)
        self.__frame.grid(row=0, column=0, sticky="NSEW")

        self.__entry = ttk.Entry(self.__frame)
        self.__entry.grid(row=0, column=0, sticky="nsew")
        self.__entry.insert(0, self.__playlist_name)

        self.__rename_button = ttk.Button(
            self.__frame, text="Renomear", command=self.__rename_playlist
        )
        self.__rename_button.grid(row=0, column=1,sticky="nsew")

        self.__render_musics()

    def set_playlist_name(self, playlist_name):
        self.__playlist_name = playlist_name

    def set_update_playlist_ui_function(self, function):
        self.__update_playlist_ui_function = function

    def __rename_playlist(self):
        new_name = self.__entry.get()
        if new_name:
            name = generate_playlist_filename(new_name)
            playlist_name = generate_playlist_filename(self.__playlist_name)
            rename_file(playlist_name, name)
            self.__playlist_name = new_name
            self.__root.title("Editar playlist " + self.__playlist_name)
            if self.__update_playlist_ui_function:
                self.__update_playlist_ui_function()

    def __render_musics(self):
        playlist = generate_playlist_filename(self.__playlist_name)
        paths = read_paths_from_file(playlist)
        if paths:
            for path in paths:
                music = format_music_filename(path)
                self.__add_item(music)

    def __add_item(self, music):
        frame = tk.Frame(self.__root)
        frame.grid(sticky="nsew", padx=5, pady=2, columnspan=2)
        frame.columnconfigure(0, weight=1)

        music_label = tk.Label(frame, text=music, anchor="w")
        music_label.grid(row=0, column=0, sticky="ew")

        delete_button = tk.Button(
            frame,
            text="remover",
            command=lambda f=frame, m=music: self.__delete_music(f, m),
        )
        delete_button.grid(row=0, column=1, sticky="nsew")

    def __delete_music(self, frame, name):
        playlist_name = generate_playlist_filename(self.__playlist_name)
        remove_song_by_name(playlist_name, name)

        frame.destroy()

        if self.__update_playlist_ui_function:
            self.__update_playlist_ui_function()
