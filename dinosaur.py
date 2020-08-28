import pygame
import os

_image_library={}
def get_image(path):
    global _image_library
    image=_image_library.get(path)
    if image == None:
        chuanhoa_path=path.replace('/', os.sep).replace('\\', os.sep)
        image=pygame.image.load(chuanhoa_path)
        _image_library[path]=image
    return image

pygame.init()
screen = pygame.display.set_mode((600, 150))
FPS = 60
gravity =0.6 # Trong luc
clock = pygame.time.Clock()
pygame.display.set_caption("Dino_Chay")

#Hang doi man hinh
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                
        screen.fill((255,255,255))
        screen.blit(get_image('C:\\Users\\vinh\\Desktop\\Dino_runGame\\sprites\\ground.png'),(5,110))
        screen.blit(get_image('C:\\Users\\vinh\\Pictures\\Saved Pictures\\dinosaur.png'),(10,70))
        #screen.blit(get_image('C:\\Users\\vinh\\Pictures\\Saved Pictures\\could.png'),(90,10))
        #screen.blit(get_image('C:\\Users\\vinh\\Pictures\\Saved Pictures\\could.png'),(150,20))
        screen.blit(get_image('C:\\Users\\vinh\\Pictures\\Saved Pictures\\cactus.png'),(200,70))

        pygame.display.flip()#Trao doi bo dem
        
        clock.tick(60)

