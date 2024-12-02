import tkinter as tk


class Controls:
    def __init__(self, root: tk.Tk):
        self.__root = root
        self.__center_button = tk.Button(self.__root, text="play")
        self.__state_button = False  # False: Play, True: Pause
        self.__prev = tk.Button(self.__root, text="prev")
        self.__next = tk.Button(self.__root, text="next")
        self.__favorite = tk.Button(self.__root, text="favorite")

        self.__play_function = None
        self.__pause_function = None

    def get_center_button(self):
        return self.__center_button

    def set_functions(self, play_function, pause_function):
        """Configura as funções de play e pause."""
        if not callable(play_function) or not callable(pause_function):
            raise ValueError(
                "As funções play_function e pause_function devem ser chamáveis."
            )
        self.__play_function = play_function
        self.__pause_function = pause_function
        self.__update_center_button()

    def toggle_play_pause(self):
        """Alterna entre play e pause."""
        self.__state_button = not self.__state_button
        self.__update_center_button()

    def get_prev_button(self):
        return self.__prev

    def get_next_button(self):
        return self.__next

    def get_favorite_button(self):
        return self.__favorite
    
    def __update_center_button(self):
        """Atualiza o texto e comando do botão central baseado no estado."""
        if self.__state_button:
            self.__center_button.config(text="pause", command=self.__pause_function)
        else:
            self.__center_button.config(text="play", command=self.__play_function)
