"""
csc4505_lecture5_cube_numpy.py

A complete example of drawing a 3D cube using immediate mode with NumPy.
The cube is centered at the origin, side length 1, with each face a different colour.
Includes depth testing and a simple rotation to show 3D structure.
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
import numpy as np

# ----------------------------------------------------------------------
# Cube vertex data: each row = [x, y, z, r, g, b]
# We store position and colour together for clarity, but colour is not used
# directly because we set per‑face colours. The colours here are only for reference.
# ----------------------------------------------------------------------
var_cube_vertices = np.array([
    #   x     y     z     r    g    b
    [-0.5, -0.5, -0.5,  0.0, 1.0, 0.0],   # V0: back, bottom, left   (green)
    [ 0.5, -0.5, -0.5,  0.0, 1.0, 0.0],   # V1: back, bottom, right  (green)
    [ 0.5,  0.5, -0.5,  0.0, 1.0, 0.0],   # V2: back, top, right     (green)
    [-0.5,  0.5, -0.5,  0.0, 1.0, 0.0],   # V3: back, top, left      (green)
    [-0.5, -0.5,  0.5,  1.0, 0.0, 0.0],   # V4: front, bottom, left  (red)
    [ 0.5, -0.5,  0.5,  1.0, 0.0, 0.0],   # V5: front, bottom, right (red)
    [ 0.5,  0.5,  0.5,  1.0, 0.0, 0.0],   # V6: front, top, right    (red)
    [-0.5,  0.5,  0.5,  1.0, 0.0, 0.0]    # V7: front, top, left     (red)
], dtype=np.float32)

# ----------------------------------------------------------------------
# Triangle indices: 12 triangles (2 per face), each defined by three vertex indices.
# Order: front, back, left, right, top, bottom.
# ----------------------------------------------------------------------
var_cube_indices = np.array([
    # Front face (red) – two triangles (V4,V5,V6) and (V4,V6,V7)
    [4,5,6], [4,6,7],
    # Back face (green) – two triangles (V0,V2,V1) and (V0,V3,V2)
    [0,2,1], [0,3,2],
    # Left face (blue) – (V0,V3,V7) and (V0,V7,V4)
    [0,3,7], [0,7,4],
    # Right face (yellow) – (V1,V5,V6) and (V1,V6,V2)
    [1,5,6], [1,6,2],
    # Top face (cyan) – (V3,V2,V6) and (V3,V6,V7)
    [3,2,6], [3,6,7],
    # Bottom face (magenta) – (V0,V1,V5) and (V0,V5,V4)
    [0,1,5], [0,5,4]
], dtype=np.int32)

# ----------------------------------------------------------------------
# Per‑face colours (r,g,b) in the same order as the faces above.
# ----------------------------------------------------------------------
var_face_colours = [
    [1.0, 0.0, 0.0],   # red    – front
    [0.0, 1.0, 0.0],   # green  – back
    [0.0, 0.0, 1.0],   # blue   – left
    [1.0, 1.0, 0.0],   # yellow – right
    [0.0, 1.0, 1.0],   # cyan   – top
    [1.0, 0.0, 1.0]    # magenta – bottom
]

# ----------------------------------------------------------------------
# Drawing function: uses immediate mode with loops over the arrays.
# ----------------------------------------------------------------------
def fxn_draw_cube():
    """Draw the cube using GL_TRIANGLES and the defined vertex/index data."""
    glBegin(GL_TRIANGLES)
    for var_face in range(6):                       # six faces
        glColor3f(*var_face_colours[var_face])      # set colour for this face
        for var_i in range(2):                      # two triangles per face
            var_tri = var_cube_indices[var_face*2 + var_i]   # indices of this triangle
            for var_j in range(3):                   # three vertices per triangle
                var_v = var_cube_vertices[var_tri[var_j]]    # fetch vertex data
                glVertex3f(var_v[0], var_v[1], var_v[2])    # pass position
    glEnd()

# ----------------------------------------------------------------------
# Main function: sets up Pygame, enables depth testing, and runs the loop.
# ----------------------------------------------------------------------
def main():
    var_running = True
    var_display = (800, 600)
    var_angle = 0.0

    pygame.init()
    pygame.display.set_mode(var_display, DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("3D Cube with NumPy")
    var_clock = pygame.time.Clock()

    # Enable depth testing so that faces occlude each other correctly
    glEnable(GL_DEPTH_TEST)

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

        # Apply a rotation to make the 3D structure visible
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glRotatef(var_angle, 1, 1, 0)   # rotate around diagonal axis
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
