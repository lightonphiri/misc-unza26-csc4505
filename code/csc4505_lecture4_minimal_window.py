"""
Minimal Pygame window with OpenGL context.
Clears the screen with a color each frame.
"""
import pygame
from pygame.locals import *
from OpenGL.GL import *

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()

    print("OpenGL version:", glGetString(GL_VERSION).decode())
    print("Vendor:", glGetString(GL_VENDOR).decode())
    print("Renderer:", glGetString(GL_RENDERER).decode())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClearColor(0.2, 0.3, 0.4, 1.0)   # dark blue-gray
        glClear(GL_COLOR_BUFFER_BIT)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
