import pygame

class MidiaPlayer:
    def __init__(self):
        self.__pygame = pygame
        self.__pygame.mixer.init()

    def play(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def unPause(self):
        pygame.mixer.music.unpause()

    def get_music_duration(self):
        return self.__pygame.mixer.Sound.get_length()    
