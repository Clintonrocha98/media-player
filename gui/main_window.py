import tkinter as tk
from tkinter.filedialog import askopenfilenames
from .progress_bar import ProgressBar
from .controls import Controls
from .music_list import MusicList
from core.player import Pygame
from core.playlist import PlayList
from utils.format_music_filename import format_music_filename


class Window:
    def __init__(self, title="Clinton Mp3"):
        self.__root = tk.Tk()
        self.__root.title(title)
        self.__controls = Controls()
        self.__playlist = PlayList()

        # TODO: falta colocar a barra de progresso na UI
        self.__progress_bar = ProgressBar(self.__root)

        self.__music_list = MusicList(self.__root)
        self.__pygame = Pygame()

        self.set_window_size()

        open_folter_button = tk.Button(
            self.__root, text="abrir pasta", 
            command=self.open_and_add_music_files
        )
        open_folter_button.grid(row=0, column=0, pady=5,padx=5)

        self.__controls.set_play_function(self.play)
        self.__controls.set_pause_function(self.pause)

        self.__controls.set_root(self.__root)
        self.__controls.set_prev_click_event(self.play_previous_song)
        self.__controls.set_next_click_event(self.play_next_song)

        self.__pygame.start_event()

        self.__root.mainloop()

    def play(self):
        self.__pygame.unPause()
        self.__controls.switch_to_pause_button()

    def pause(self):
        self.__pygame.pause()
        self.__controls.switch_to_play_button()

    def open_and_add_music_files(self):
        file_paths = self.__open_file_dialog()

        if file_paths:
            self.__add_music_files_to_playlist(file_paths)
            self.__start_playback_if_not_playing()

    def play_next_song(self):
        next_file = self.__playlist.next_music()

        if next_file:
            self.__pygame.play(next_file)
            self.__music_list.highlight_playing(format_music_filename(next_file))
        else:
            if self.__pygame.is_playing():
                self.__controls.switch_to_pause_button()
            else:
                self.__controls.switch_to_play_button()
            print("Fim da playlist ou nenhuma música carregada.")

    def play_previous_song(self):
        prev_file = self.__playlist.prev_music()

        if prev_file:
            self.__pygame.play(prev_file)
            self.__music_list.highlight_playing(format_music_filename(prev_file))
        else:
            print("Nenhuma música anterior ou playlist vazia.")

    def __open_file_dialog(self):
        return askopenfilenames(
            title="Selecione arquivos MP3", filetypes=[("Arquivos MP3", "*.mp3")]
        )

    def __add_music_files_to_playlist(self, file_paths):
        """Adiciona as músicas selecionadas à playlist e à UI."""
        for file in file_paths:
            formatted_name = format_music_filename(file)
            self.__music_list.add_music(formatted_name)
            self.__playlist.add_music(file)

    def __start_playback_if_not_playing(self):
        """Verifica se há uma música tocando, e começa a reprodução se necessário."""
        if not self.__pygame.is_playing():
            self.__controls.switch_to_pause_button()
            self.play_next_song()
            self.__check_and_handle_pygame_events()

    def __check_and_handle_pygame_events(self):
            """Verifica os eventos do pygame periodicamente."""
            for event in self.__pygame.get_event():
                if event.type == self.__pygame.get_user_event():
                    self.play_next_song()
            self.__root.after(100, self.__check_and_handle_pygame_events)

    def set_window_size(self, width=500, height=375):
        width_window = self.__root.winfo_screenwidth()
        height_window = self.__root.winfo_screenheight()

        pos_x = (width_window - width) // 2
        pos_y = (height_window - height) // 2

        self.__root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
