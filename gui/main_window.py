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
        self.__controls = Controls(self.__root)
        self.__playlist = PlayList()

        #TODO: falta colocar a barra de progresso na UI
        self.__progress_bar = ProgressBar(self.__root)

        self.__music_list = MusicList(self.__root)
        self.__pygame = Pygame()

        self.set_window_size()

        # ligando as funções de play e pause na UI do botão de cada
        self.__controls.set_functions(self.play, self.pause)

        prev_music_button = self.__controls.get_prev_button()
        prev_music_button.config(command=self.play_previous)
        prev_music_button.pack(side=tk.LEFT, padx=5, pady=5)

        center_button = self.__controls.get_center_button()
        center_button.pack(side=tk.LEFT, padx=5, pady=5)

        next_music_button = self.__controls.get_next_button()
        next_music_button.config(command=self.play_next)
        next_music_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        music_button = tk.Button(self.__root,text="abrir pasta", command=self.ask_path)
        music_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.__root.mainloop()

    def play(self):
        self.__pygame.unPause()
        self.__controls.toggle_play_pause()
        self.__pygame.start_event()

    def pause(self):
        self.__pygame.pause()
        self.__controls.toggle_play_pause()

    def ask_path(self):
        file_paths = askopenfilenames(
            title="Selecione arquivos MP3", filetypes=[("Arquivos MP3", "*.mp3")]
        )

        if file_paths:
            for file in file_paths:
                formatted_name = format_music_filename(file)
                self.__music_list.add_music(formatted_name)  
                self.__playlist.add_music(file)

            if self.__playlist.head:
                self.__controls.toggle_play_pause() 
                self.play_next()
                self.__check_pygame_events()

    def play_next(self):
        """Reproduz a próxima música na playlist."""
        next_file = self.__playlist.next_music()

        if next_file:
            self.__pygame.stop() 
            self.__pygame.play(next_file)  
            self.__music_list.highlight_playing(format_music_filename(next_file))
        else:
            print("Fim da playlist ou nenhuma música carregada.")


    def play_previous(self):
        """Reproduz a música anterior na playlist."""
        prev_file = self.__playlist.prev_music() 
        
        if prev_file:
            self.__pygame.stop()
            self.__pygame.play(prev_file)
            self.__music_list.highlight_playing(format_music_filename(prev_file))
        else:
            print("Nenhuma música anterior ou playlist vazia.")
            
    def __check_pygame_events(self):
        """Verifica os eventos do pygame periodicamente."""
        for event in self.__pygame.get_event():
            if event.type == self.__pygame.get_user_event():
                self.play_next()  
        self.__root.after(100, self.__check_pygame_events)

    def set_window_size(self, width=450, height=500):
        width_window = self.__root.winfo_screenwidth()
        height_window = self.__root.winfo_screenheight()

        pos_x = (width_window - width) // 2
        pos_y = (height_window - height) // 2

        self.__root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
