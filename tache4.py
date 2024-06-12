import pygame
import sys

pygame.init()

# Initialisation de la fenêtre
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Jeu de serpent")

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Logique du jeu ici

    pygame.display.flip()