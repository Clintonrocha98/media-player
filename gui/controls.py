import tkinter as tk


class Controls:
    def __init__(self):
        self.__root = None
        self.__prev = tk.Button(self.__root, text="prev")
        self.__center_button = tk.Button(self.__root, text="play", width=15)
        self.__next = tk.Button(self.__root, text="next")

        self.__prev.grid(row=3, column=0, padx=5)
        self.__center_button.grid(row=3, column=1)
        self.__next.grid(row=3, column=2)

        self.__play_function = None
        self.__pause_function = None

    def set_root(self, root):
        self.__root = root

    def set_play_function(self, play_function):
        self.__play_function = play_function

    def set_pause_function(self, pause_function):
        self.__pause_function = pause_function

    def switch_to_pause_button(self):
        self.__center_button.config(text="pause", command=self.__pause_function)

    def switch_to_play_button(self):
        self.__center_button.config(text="play", command=self.__play_function)

    def set_prev_click_event(self, event):
        self.__prev.config(command=event)

    def set_next_click_event(self, event):
        self.__next.config(command=event)
