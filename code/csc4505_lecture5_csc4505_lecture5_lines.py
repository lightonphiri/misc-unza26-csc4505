"""
Demonstrates GL_POINTS – four white points at the corners.
"""
import pygame
from pygame.locals import *
from OpenGL.GL import *

def fxn_draw():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)        # Green
    glVertex3f(-0.5,  0.5, 0.0)      # Start line 1
    glVertex3f( 0.5, -0.5, 0.0)      # End line 1
    glVertex3f(-0.5, -0.5, 0.0)      # Start line 2
    glVertex3f( 0.5,  0.5, 0.0)      # End line 2
    glEnd()

def main():
    var_running = True
    var_display = (800, 600)

    pygame.init()
    pygame.display.set_mode(var_display, DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("GL_POINTS Example")
    var_clock = pygame.time.Clock()

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

        fxn_draw()

        pygame.display.flip()
        var_clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
