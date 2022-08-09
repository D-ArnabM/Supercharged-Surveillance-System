import pygame
class Alert:
    def play_audio(self):
        pygame.init()
        file="Sounds\Alert.mp3"
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()