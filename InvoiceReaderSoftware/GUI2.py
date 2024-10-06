import pygame
import sys
import cv2
from pygame.locals import *

global    new_width 
global    new_height



def display_image(image_path):
   

    # Load the image
    
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (new_width, new_height))
    
    output_path = 'resized_image.jpg'  # Change this to your desired output path
    cv2.imwrite(output_path, resized_image)
    
    
    image = pygame.image.load('resized_image.jpg')

    # Scale the image to fit the screen
    image = pygame.transform.scale(image, (screen_width, screen_height))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == MOUSEBUTTONDOWN:
                running = False

        # Draw the image on the screen
        screen.blit(image, (0, 0))
        
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
     # Initialize Pygame
    pygame.init()

    # Set up the display
    new_width = 1600 
    new_height = 900  
    
    
    screen_width = 1920
    screen_height = 861
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Display Image")
    display_image('welcome.png')
    
    
