import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from utils import (
    rename_file,
    generate_playlist_filename,
    remove_song_by_name,
    read_paths_from_file,
    format_music_filename,
    create_and_append_file,
)


class EditPlaylistTreeview:
    def __init__(self):
        self.__root = None
        self.__playlist_name = None
        self.__entry = None
        self.__rename_button = None
        self.__update_playlist_ui_function = None
        self.__frame = None
        self.__add_button = None

    def set_playlist_name(self, playlist_name):
        self.__playlist_name = playlist_name

    def set_update_playlist_ui_function(self, function):
        self.__update_playlist_ui_function = function

    def set_frame(self, root):
        self.__create_window(root)
        self.__create_canvas_with_scrollbar()
        self.__create_buttons()
        self.__render_musics()

    def __create_window(self, root):
        self.__root = tk.Toplevel(root)
        self.__root.title(f"Editar playlist {self.__playlist_name}")
        self.__root.geometry("330x350")
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

    def __create_canvas_with_scrollbar(self):
        canvas = tk.Canvas(self.__root)
        canvas.grid(row=0, column=0, sticky="NSEW")

        scrollbar = ttk.Scrollbar(self.__root, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        canvas.configure(yscrollcommand=scrollbar.set)

        self.__frame = tk.Frame(canvas)
        self.__frame.grid(sticky="NSEW")

        self.__frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=self.__frame, anchor="nw")

    def __create_buttons(self):
        self.__entry = ttk.Entry(self.__frame)
        self.__entry.grid(row=0, column=0, sticky="nsew")
        self.__entry.insert(0, self.__playlist_name)

        self.__rename_button = ttk.Button(
            self.__frame, text="Renomear", command=self.__rename_playlist
        )
        self.__rename_button.grid(row=0, column=1, sticky="nsew", padx=5)
        self.__add_button = tk.Button(self.__root,text="adicionar musica", command=self.__open_and_add_music)
        self.__add_button.grid()

    def __rename_playlist(self):
        new_name = self.__entry.get()
        if new_name:
            old_playlist_file = generate_playlist_filename(self.__playlist_name)
            new_playlist_file = generate_playlist_filename(new_name)
            rename_file(old_playlist_file, new_playlist_file)
            self.__playlist_name = new_name
            self.__root.title(f"Editar playlist {self.__playlist_name}")
            if self.__update_playlist_ui_function:
                self.__update_playlist_ui_function()

    def __render_musics(self):
        playlist_file = generate_playlist_filename(self.__playlist_name)
        paths = read_paths_from_file(playlist_file)
        if paths:
            for index, path in enumerate(paths):
                music_name = format_music_filename(path)
                self.__add_music_item(music_name, index)

    def __add_music_item(self, music_name, row):
        music_label = tk.Label(self.__frame, text=music_name, anchor="w")
        music_label.grid(row=row + 1, column=0, sticky="ew")

        delete_button = tk.Button(
            self.__frame,
            text="Remover",
            command=lambda: self.__delete_music(music_name),
        )
        delete_button.grid(row=row + 1, column=1, sticky="nsew", padx=5)

    def __delete_music(self, music_name):
        playlist_file = generate_playlist_filename(self.__playlist_name)
        remove_song_by_name(playlist_file, music_name)
        if self.__update_playlist_ui_function:
            self.__update_playlist_ui_function()

        self.__render_musics()

    def __open_and_add_music(self):
        file_paths = askopenfilenames(
            title="Selecione arquivos MP3", filetypes=[("Arquivos MP3", "*.mp3")]
        )
        if file_paths:
            for idx, file in enumerate(file_paths):
                music_name = format_music_filename(file)
                self.__add_music_item(music_name, idx)
                playlist = generate_playlist_filename(self.__playlist_name)
                create_and_append_file(playlist, file)
