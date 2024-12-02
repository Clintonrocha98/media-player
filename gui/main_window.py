import os
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilenames
from .progress_bar import ProgressBar
from .controls import Controls
from .menu import MediaPlayerMenu

def criar_playlist():
    print("vc esta criando uma playlist")

def ouvir_musica():
    print("musica selecionada")

class Window:
    def __init__(self, title="Clinton Mp3"):
        self.__root = tk.Tk()
        self.__root.title(title)
        self.__controls = Controls(self.__root)
        self.__menu = MediaPlayerMenu(self.__root)
        self.__progress_bar = ProgressBar(self.__root)

        self.__menu.add_option("criar playlist",criar_playlist)
        self.__menu.add_option("selecione uma musica",ouvir_musica)

        self.set_window_size()

        center_button = self.__controls.get_center_button()
        self.__controls.set_functions(self.play, self.pause)
        center_button.pack()

        #TODO: precisa fazer algo depois de ler os arquivos na pasta...
        music_button = tk.Button(self.__root,text="abrir pasta", command=self.ask_path)
        music_button.pack()

        self.__root.mainloop()

    def play(self):
        """metodo provisorio"""
        self.__controls.toggle_play_pause()
        print("dei play")

    def pause(self):
        """metodo provisorio"""
        self.__controls.toggle_play_pause()
        print("pausei ")

    def readPath(self):
        """provisorio"""
        pasta = askdirectory(title="Selecione uma pasta")

        if pasta:
            print(f"Pasta selecionada: {pasta}")

            for root_dir, dirs, files in os.walk(pasta):
                for file in files:
                    caminho_completo = os.path.join(root_dir, file)
                    print(caminho_completo)
        else:
            print("Nenhuma pasta foi selecionada.")

    def ask_path(self):
        file_paths = askopenfilenames(
            title="Selecione arquivos MP3", filetypes=[("Arquivos MP3", "*.mp3")]
        )

        paths = []

        if file_paths:
            for file in file_paths:
                paths.append(file)

        return paths

    def set_window_size(self, width=800, height=400):
        width_window = self.__root.winfo_screenwidth()
        height_window = self.__root.winfo_screenheight()

        pos_x = (width_window - width) // 2
        pos_y = (height_window - height) // 2

        self.__root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
