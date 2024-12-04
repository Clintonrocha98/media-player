import tkinter as tk
from tkinter.filedialog import askopenfilenames
from gui.progress_bar import ProgressBar
from gui.controls import Controls
from gui.music_list import MusicList
from core.pygame_audio_player import AudioPlayer
from core.playlist import PlayList
from utils.format_music_filename import format_music_filename

root = tk.Tk()
root.title("Clinton Mp3")
controls = Controls()
playlist = PlayList()
progress_bar = ProgressBar(root)
music_list = MusicList(root)
pygame_instance = AudioPlayer()

def play():
    """Inicia a reprodução."""
    pygame_instance.unPause()
    controls.switch_to_pause_button()

def pause():
    """Pausa a reprodução."""
    pygame_instance.pause()
    controls.switch_to_play_button()

def open_and_add_music_files():
    """Abre o seletor de arquivos e adiciona músicas à playlist."""
    file_paths = askopenfilenames(
        title="Selecione arquivos MP3", filetypes=[("Arquivos MP3", "*.mp3")]
    )

    if file_paths:
        add_music_files_to_playlist(file_paths)
        start_playback_if_not_playing()

def play_next_song():
    """Toca a próxima música na playlist."""
    next_file = playlist.next_music()

    if next_file:
        pygame_instance.play(next_file)
        music_list.highlight_playing(format_music_filename(next_file))
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
        music_list.highlight_playing(format_music_filename(prev_file))
    else:
        print("Nenhuma música anterior ou playlist vazia.")

def add_music_files_to_playlist(file_paths):
    """Adiciona músicas à playlist e à UI."""
    for file in file_paths:
        formatted_name = format_music_filename(file)
        music_list.add_music(formatted_name)
        playlist.add_music(file)

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
    root.after(100, check_and_handle_pygame_events)

"""Define o tamanho da janela."""
width_window = root.winfo_screenwidth()
height_window = root.winfo_screenheight()

pos_x = (width_window - 500) // 2
pos_y = (height_window - 375) // 2

root.geometry(f"{500}x{375}+{pos_x}+{pos_y}")

open_folder_button = tk.Button(
    root, text="abrir pasta", command=open_and_add_music_files
)
open_folder_button.grid(row=0, column=0, pady=5, padx=5)

controls.set_play_function(play)
controls.set_pause_function(pause)
controls.set_root(root)
controls.set_prev_click_event(play_previous_song)
controls.set_next_click_event(play_next_song)

pygame_instance.start_event()

root.mainloop()
