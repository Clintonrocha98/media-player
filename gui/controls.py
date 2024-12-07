import tkinter as tk


class Controls:
    def __init__(self):        
        self.__play_function = None
        self.__pause_function = None

    def set_frame(self, frame):
        self.__prev_button = tk.Button(frame, text="prev")
        self.__center_button = tk.Button(frame, text="play", width=15)
        self.__next_button = tk.Button(frame, text="next")
        self.__random_button = tk.Button(frame, text="random")
        self.__open_folder_button = tk.Button(frame, text="abrir pasta")

        self.__prev_button.grid(row=2,column=1,sticky="nsew")
        self.__center_button.grid(row=3,column=1,sticky="nsew")
        self.__next_button.grid(row=4,column=1,sticky="nsew")
        self.__random_button.grid(row=5,column=1,sticky="nsew")
        self.__open_folder_button.grid(row=6,column=1,sticky="nsew")

    def set_open_folder_fuction(self, event):
        self.__open_folder_button.config(command=event)

    def set_play_function(self, play_function):
        self.__play_function = play_function

    def set_pause_function(self, pause_function):
        self.__pause_function = pause_function

    def switch_to_pause_button(self):
        self.__center_button.config(text="pause", command=self.__pause_function)

    def switch_to_play_button(self):
        self.__center_button.config(text="play", command=self.__play_function)

    def set_prev_click_event(self, event):
        self.__prev_button.config(command=event)

    def set_next_click_event(self, event):
        self.__next_button.config(command=event)

    def set_random_click_event(self, event):
        self.__random_button.config(command=event)
