import os
import tkinter as tk
from tkinter.filedialog import askdirectory

class InterfaceTk:
    def __init__(self) -> None:
        self.__root = tk.Tk()
        self.__root.title("Clinton mp3")
        self.__altura = 400
        self.__largura = 800

        largura_tela = self.__root.winfo_screenwidth() 
        altura_tela = self.__root.winfo_screenheight()  

        pos_x = (largura_tela - self.__largura) // 2
        pos_y = (altura_tela - self.__altura) // 2

        self.__root.geometry(f'{self.__largura}x{self.__altura}+{pos_x}+{pos_y}')

        button = tk.Button(self.__root, text="Ler arquivos", command=self.readPath)

        button.pack(pady=20)

        self.__root.mainloop()
    
    def readPath(self):

        pasta = askdirectory(title="Selecione uma pasta")

        if pasta:
            print(f"Pasta selecionada: {pasta}")

            for root_dir, dirs, files in os.walk(pasta):
                for file in files:
                    caminho_completo = os.path.join(root_dir, file)
                    print(caminho_completo)
        else:
            print("Nenhuma pasta foi selecionada.")