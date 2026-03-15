"""
Draws a triangle using legacy immediate mode (glBegin/glEnd).
This is for demonstration only; modern OpenGL uses VBOs and shaders.
"""
import pygame
from pygame.locals import *
from OpenGL.GL import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)   # red
    glVertex2f(0.0, 0.5)
    glColor3f(0.0, 1.0, 0.0)   # green
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)   # blue
    glVertex2f(0.5, -0.5)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        draw_triangle()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
