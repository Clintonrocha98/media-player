import tkinter as tk
from tkinter.filedialog import askopenfilenames
from tkinter import simpledialog
from gui import Controls, ItemDisplayList, EditPlaylistTreeview
from core import AudioPlayer, PlayList
from utils import (
    format_music_filename,
    list_files,
    read_paths_from_file,
    create_and_append_file,
    generate_playlist_filename,
    restore_string,
    delete_playlist_file,
)

root = tk.Tk()
root.title("Radinho de pilha")
music_list_ui = ItemDisplayList()
playlist_ui = ItemDisplayList()
controls = Controls()
pygame_instance = AudioPlayer()
playlist = PlayList()
treeview = EditPlaylistTreeview()


def play():
    pygame_instance.unPause()
    controls.switch_to_pause_button()


def pause():
    pygame_instance.pause()
    controls.switch_to_play_button()


def open_and_add_music_files():
    file_paths = askopenfilenames(
        title="Selecione arquivos MP3", filetypes=[("Arquivos MP3", "*.mp3")]
    )

    if file_paths:
        pygame_instance.stop()
        for file in file_paths:
            formatted_name = format_music_filename(file)
            music_list_ui.add_to_list(formatted_name)
            playlist.add_music(file)
        start_playback_if_not_playing()


def play_next_song():

    next_file = playlist.next_music()

    if next_file:
        pygame_instance.play(next_file)
        music_list_ui.highlight_playing(format_music_filename(next_file))
    else:
        if pygame_instance.is_playing():
            controls.switch_to_pause_button()
        else:
            controls.switch_to_play_button()
        print("Fim da playlist ou nenhuma música carregada.")


def play_previous_song():
    """Toca a música anterior na playlist."""
    prev_file = playlist.prev_music()

    if prev_file:
        pygame_instance.play(prev_file)
        music_list_ui.highlight_playing(format_music_filename(prev_file))
    else:
        print("Nenhuma música anterior ou playlist vazia.")


def start_playback_if_not_playing():
    """Inicia a reprodução se nenhuma música estiver tocando."""
    if not pygame_instance.is_playing():
        controls.switch_to_pause_button()
        play_next_song()
        check_and_handle_pygame_events()


def check_and_handle_pygame_events():
    """Verifica os eventos do pygame periodicamente."""
    for event in pygame_instance.get_event():
        if event.type == pygame_instance.get_user_event():
            play_next_song()
    root.after(500, check_and_handle_pygame_events)


def add_songs_from_playlist_to_ui():
    playlist_selected = playlist_ui.get_item_selected()
    playlist_selected = generate_playlist_filename(playlist_selected)
    if not playlist_selected:
        return

    file_paths = read_paths_from_file(playlist_selected)

    if file_paths:
        pygame_instance.stop()
        music_list_ui.clear_list()

        for file in file_paths:
            formatted_name = format_music_filename(file)
            music_list_ui.add_to_list(formatted_name)
            playlist.add_music(file)

        start_playback_if_not_playing()


def create_playlist():
    playlist_name = simpledialog.askstring("Criar playlist", "Nome da playlist")
    if playlist_name:
        file_name = generate_playlist_filename(playlist_name)
        create_and_append_file(file_name)

        ui_name = restore_string(file_name)
        playlist_ui.add_to_list(ui_name)


def update_playlist_ui():
    """Atualiza a ui com as playlists criadas"""
    for file in list_files():
        formatted_name = format_music_filename(file)
        formatted_name = restore_string(formatted_name)
        playlist_ui.add_to_list(formatted_name)


def delete_playlist():
    playlist_selected = playlist_ui.get_item_selected()
    playlist_selected = generate_playlist_filename(playlist_selected)
    if not playlist_selected:
        return
    delete_playlist_file(playlist_selected)
    playlist_ui.clear_list()
    update_playlist_ui()


def window_edit_playlist():
    playlist = playlist_ui.get_item_selected()
    if playlist:
        treeview.set_playlist_name(playlist)
        treeview.set_frame(main_frame)
        treeview.set_update_playlist_ui_function(update_playlist_ui)


width = 650
height = 500

width_window = root.winfo_screenwidth()
height_window = root.winfo_screenheight()

pos_x = (width_window - width) // 2
pos_y = (height_window - height) // 2

root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0)

tk.Label(main_frame, text="playlists").grid(row=0, column=0)
playlist_ui.set_frame(main_frame)
playlist_ui.set_position(1, 0)


tk.Label(main_frame, text="musicas").grid(row=0, column=1)
music_list_ui.set_frame(main_frame)
music_list_ui.set_position(1, 1)

controls.set_frame(main_frame)


tk.Button(
    main_frame, text="Tocar Playlist", command=add_songs_from_playlist_to_ui
).grid(row=2, column=0, sticky="nsew")

tk.Button(main_frame, text="Criar playlist", command=create_playlist).grid(
    row=3, column=0, sticky="nsew"
)

tk.Button(main_frame, text="Editar Playlist", command=window_edit_playlist).grid(
    row=4, column=0, sticky="nsew"
)

tk.Button(main_frame, text="Apagar Playlist", command=delete_playlist).grid(
    row=5, column=0, sticky="nsew"
)

update_playlist_ui()

controls.set_play_function(play)
controls.set_pause_function(pause)
controls.set_prev_click_event(play_previous_song)
controls.set_next_click_event(play_next_song)
controls.set_random_click_event(playlist.shuffle_playlist)
controls.set_open_folder_fuction(open_and_add_music_files)

pygame_instance.start_event()

root.mainloop()
