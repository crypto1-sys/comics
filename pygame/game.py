import pygame

pygame.init()

size = (600,400)

flags = pygame.FULLSCREEN | pygame.RESIZABLE

FENETRE = pygame.display.set_mode(size, flags)

pygame.display.set_caption("Funny Jungle")