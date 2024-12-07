import tkinter as tk
from tkinter.filedialog import askopenfilenames
from gui.progress_bar import ProgressBar
from gui.controls import Controls
from gui.item_display_list import ItemDisplayList
from gui.treeview import PlaylistWindow
from core.pygame_audio_player import AudioPlayer
from core.playlist import PlayList
from utils.format_music_filename import format_music_filename
from utils.list_files import list_files
from utils.read_paths_from_file import read_paths_from_file

root = tk.Tk()
root.title("Clinton Mp3")
music_list_ui = ItemDisplayList()
playlist_ui = ItemDisplayList()
controls = Controls()
progress_bar = ProgressBar(root)
pygame_instance = AudioPlayer()
playlist = PlayList()


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


def add_songs_from_playlist_to_ui():
    playlist_selected = playlist_ui.get_item_selected()
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

for file in list_files():
    formatted_name = format_music_filename(file)
    playlist_ui.add_to_list(formatted_name)

play_playlist_button = tk.Button(
    main_frame, text="play playlist", command=add_songs_from_playlist_to_ui
)
play_playlist_button.grid(row=2, column=0)

controls.set_play_function(play)
controls.set_pause_function(pause)
controls.set_prev_click_event(play_previous_song)
controls.set_next_click_event(play_next_song)
controls.set_random_click_event(playlist.shuffle_playlist)
controls.set_open_folder_fuction(open_and_add_music_files)

pygame_instance.start_event()

root.mainloop()
