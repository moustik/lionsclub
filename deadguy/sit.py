import time

import pygame
from pygame.locals import*


img = pygame.image.load('C:\\Users\\museomix\\lionsclub\\deadguy\\museomix_mapping_gisant_fuschia-01-01.jpg')
img = pygame.transform.scale(img,(1280, 1024))
secret = 'C:\\Users\\museomix\\lionsclub\\deadguy\\LeSecretDuLion-Eglise-16Bit.mp3'

def start_mapping():
    screen.fill((white))
    screen.blit(img,(0,0))
    pygame.display.flip()


def stop_mapping():
    screen.fill((0, 0, 0))
    pygame.display.flip()

def play_secret():
    pygame.mixer.init()
    pygame.mixer.music.load(secret)
    pygame.mixer.music.play()
    #pygame.mixer.Sound(secret).play()
#    time.sleep(10)

#pygame.mixer.init(44100, -16, 2, 2048)
#pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.

white = (255, 64, 64)
w = 1280
h = 1024
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


screen.fill((0, 0, 255))


toggle = False

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
                break # break out of the for loop
            if event.key == pygame.K_SPACE:
                toggle = not toggle
                if toggle:
                    start_mapping()
                else:
                    stop_mapping()
            if event.key == pygame.K_a:
                play_secret()
        elif event.type == pygame.QUIT:
            done = True
            break # break out of the for loop
    if done:
        break # to break out of the while loop

pygame.quit() 
