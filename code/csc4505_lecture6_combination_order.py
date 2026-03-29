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
    gluOrtho2D(-4, 4, -4, 4)
    glMatrixMode(GL_MODELVIEW)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)

        # Original triangle (white)
        glLoadIdentity()
        glColor3f(1, 1, 1)
        fxn_draw_triangle()

        # Order 1: scale, then rotate, then translate (red)
        glLoadIdentity()
        glTranslatef(2, 1, 0)
        glRotatef(45, 0, 0, 1)
        glScalef(2, 1, 1)
        glColor3f(1, 0, 0)
        fxn_draw_triangle()

        # Order 2: translate, then rotate, then scale (blue) – different result
        glLoadIdentity()
        glScalef(2, 1, 1)
        glRotatef(45, 0, 0, 1)
        glTranslatef(2, 1, 0)
        # Shift down so we can see it
        glTranslatef(0, -2, 0)
        glColor3f(0, 0, 1)
        fxn_draw_triangle()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
