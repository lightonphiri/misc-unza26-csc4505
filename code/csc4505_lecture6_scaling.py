import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def fxn_draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(0.0, 1.0)
    glEnd()

def main():
    pygame.init()
    var_display = (800, 600)
    pygame.display.set_mode(var_display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-3, 3, -3, 3)
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)

        # Draw original triangle (white)
        glLoadIdentity()
        glColor3f(1, 1, 1)
        fxn_draw_triangle()

        # Draw scaled triangle (red) – non‑uniform scaling
        glLoadIdentity()
        glScalef(2.0, 0.5, 1.0)   # scale x2, y0.5
        glColor3f(1, 0, 0)
        fxn_draw_triangle()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
