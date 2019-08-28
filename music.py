import pygame



def gas():

    pygame.mixer.init()

    pygame.mixer.music.load('gas.mp3')

    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)