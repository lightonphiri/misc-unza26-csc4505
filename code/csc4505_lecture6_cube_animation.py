import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def fxn_draw_cube():
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )
    edges = (
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,7), (7,6), (6,4),
        (0,4), (1,5), (2,7), (3,6)
    )
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    var_display = (800, 600)
    pygame.display.set_mode(var_display, DOUBLEBUF | OPENGL)

    # Set up perspective projection (will be covered in viewing lecture)
    gluPerspective(45, (var_display[0]/var_display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)   # move camera back

    var_angle = 0.0
    var_tx = 0.0
    var_direction = 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply transformations: first rotate, then translate
        glPushMatrix()                # save camera matrix
        glTranslatef(var_tx, 0, 0)    # move left/right
        glRotatef(var_angle, 1, 1, 0) # rotate around diagonal axis
        fxn_draw_cube()
        glPopMatrix()                 # restore camera matrix

        pygame.display.flip()
        var_angle += 1.0
        var_tx += 0.01 * var_direction
        if abs(var_tx) > 2:
            var_direction *= -1
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
