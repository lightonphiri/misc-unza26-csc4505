"""
Resizable Pygame window with OpenGL.
Updates the viewport when the window is resized.
"""
import pygame
from pygame.locals import *
from OpenGL.GL import *

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)
    clock = pygame.time.Clock()

    print("OpenGL version:", glGetString(GL_VERSION).decode())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == VIDEORESIZE:
                # Update window size and OpenGL viewport
                display = event.size
                pygame.display.set_mode(display, DOUBLEBUF | OPENGL | RESIZABLE)
                glViewport(0, 0, display[0], display[1])
                print(f"Window resized to {display[0]}x{display[1]}")

        glClearColor(0.2, 0.3, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
