import pygame

class AudioPlayer:
    def __init__(self):
        pygame.init() 
        pygame.mixer.init()
        self.__pygame = pygame
        self.current_song = None

    def play(self, file_path):
        self.__pygame.mixer.music.load(file_path)
        self.__pygame.mixer.music.play()
        
    def pause(self):
        self.__pygame.mixer.music.pause()

    def stop(self):
        self.__pygame.mixer.music.stop()

    def unPause(self):
        self.__pygame.mixer.music.unpause()

    def is_playing(self):
        return self.__pygame.mixer.music.get_busy()

    def start_event(self):
        self.__pygame.mixer.music.set_endevent(self.__pygame.USEREVENT)

    def get_event(self):
        return self.__pygame.event.get() 
    
    def get_user_event(self):
        return self.__pygame.USEREVENT
    
