"""
Pygame event handling with OpenGL.
Prints key and mouse events.
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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                print(f"Key down: {event.key} (scancode: {event.scancode})")
            elif event.type == KEYUP:
                print(f"Key up: {event.key}")
            elif event.type == MOUSEMOTION:
                print(f"Mouse move: ({event.pos[0]}, {event.pos[1]})")
            elif event.type == MOUSEBUTTONDOWN:
                print(f"Mouse button {event.button} down at {event.pos}")
            elif event.type == MOUSEBUTTONUP:
                print(f"Mouse button {event.button} up at {event.pos}")

        glClearColor(0.2, 0.3, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
