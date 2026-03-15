"""
Base template for Pygame/OpenGL immediate mode drawing.
All variables prefixed with 'var_', functions with 'fxn_'.
"""
import pygame
from pygame.locals import *
from OpenGL.GL import *

def main():
    var_running = True
    var_display = (800, 600)

    pygame.init()
    pygame.display.set_mode(var_display, DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("Lecture 5 Template")
    var_clock = pygame.time.Clock()

    print("OpenGL version:", glGetString(GL_VERSION).decode())
    print("Vendor:", glGetString(GL_VENDOR).decode())
    print("Renderer:", glGetString(GL_RENDERER).decode())

    while var_running:
        for var_event in pygame.event.get():
            if var_event.type == QUIT:
                var_running = False
            elif var_event.type == KEYDOWN and var_event.key == K_ESCAPE:
                var_running = False
            elif var_event.type == VIDEORESIZE:
                var_display = var_event.size
                pygame.display.set_mode(var_display, DOUBLEBUF | OPENGL | RESIZABLE)
                glViewport(0, 0, var_display[0], var_display[1])

        glClearColor(0.2, 0.3, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glPointSize(50)
        glBegin(GL_POINTS)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.75, 0.75, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-0.75, -0.75, 0.0)
        glEnd()

        pygame.display.flip()
        var_clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
