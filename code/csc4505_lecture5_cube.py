"""
csc4505_lecture5_cube.py

Draws a spinning 3D cube with each face in a different colour.
Demonstrates depth testing and basic transformation.
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
import math

var_angle = 0.0  # rotation angle (in degrees)

def fxn_draw_cube():
    """
    Draws a cube centered at the origin with side length 1.
    Each face is drawn as two triangles with a distinct colour.
    """
    # Front face (z = +0.5) – red
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, 0.5)   # V4
    glVertex3f( 0.5, -0.5, 0.5)   # V5
    glVertex3f( 0.5,  0.5, 0.5)   # V6
    glVertex3f(-0.5, -0.5, 0.5)   # V4
    glVertex3f( 0.5,  0.5, 0.5)   # V6
    glVertex3f(-0.5,  0.5, 0.5)   # V7
    glEnd()

    # Back face (z = -0.5) – green
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, -0.5)  # V0
    glVertex3f( 0.5,  0.5, -0.5)  # V2
    glVertex3f( 0.5, -0.5, -0.5)  # V1
    glVertex3f(-0.5, -0.5, -0.5)  # V0
    glVertex3f(-0.5,  0.5, -0.5)  # V3
    glVertex3f( 0.5,  0.5, -0.5)  # V2
    glEnd()

    # Left face (x = -0.5) – blue
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, -0.5)  # V0
    glVertex3f(-0.5,  0.5, -0.5)  # V3
    glVertex3f(-0.5,  0.5,  0.5)  # V7
    glVertex3f(-0.5, -0.5, -0.5)  # V0
    glVertex3f(-0.5,  0.5,  0.5)  # V7
    glVertex3f(-0.5, -0.5,  0.5)  # V4
    glEnd()

    # Right face (x = +0.5) – yellow
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f( 0.5, -0.5, -0.5)  # V1
    glVertex3f( 0.5, -0.5,  0.5)  # V5
    glVertex3f( 0.5,  0.5,  0.5)  # V6
    glVertex3f( 0.5, -0.5, -0.5)  # V1
    glVertex3f( 0.5,  0.5,  0.5)  # V6
    glVertex3f( 0.5,  0.5, -0.5)  # V2
    glEnd()

    # Top face (y = +0.5) – cyan
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5,  0.5, -0.5)  # V3
    glVertex3f( 0.5,  0.5, -0.5)  # V2
    glVertex3f( 0.5,  0.5,  0.5)  # V6
    glVertex3f(-0.5,  0.5, -0.5)  # V3
    glVertex3f( 0.5,  0.5,  0.5)  # V6
    glVertex3f(-0.5,  0.5,  0.5)  # V7
    glEnd()

    # Bottom face (y = -0.5) – magenta
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.5, -0.5, -0.5)  # V0
    glVertex3f( 0.5, -0.5, -0.5)  # V1
    glVertex3f( 0.5, -0.5,  0.5)  # V5
    glVertex3f(-0.5, -0.5, -0.5)  # V0
    glVertex3f( 0.5, -0.5,  0.5)  # V5
    glVertex3f(-0.5, -0.5,  0.5)  # V4
    glEnd()


def main():
    global var_angle
    var_running = True
    var_display = (800, 600)

    pygame.init()
    pygame.display.set_mode(var_display, DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("3D Cube with Depth Test")
    var_clock = pygame.time.Clock()

    # Enable depth testing so that faces occlude each other correctly
    glEnable(GL_DEPTH_TEST)
    # Also set the clear mask to clear both colour and depth buffers
    glClearDepth(1.0)

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

        # Clear colour and depth buffers
        glClearColor(0.2, 0.3, 0.4, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply a simple rotation to show the cube's 3D nature
        # (preview of transformations, to be covered in next lecture)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(var_angle, 1, 1, 0)  # rotate around diagonal axis
        var_angle += 1.0
        if var_angle > 360:
            var_angle -= 360

        # Draw the cube
        fxn_draw_cube()

        pygame.display.flip()
        var_clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
