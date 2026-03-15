"""
Check OpenGL version using GLUT (no Pygame required).
This creates a hidden window just to obtain an OpenGL context.
"""
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glutSwapBuffers()
    # After drawing once, we can exit
    glutLeaveMainLoop()  # freeglut specific; for standard GLUT use glutDestroyWindow

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1, 1)          # tiny hidden window
    glutCreateWindow(b"Version Check")
    glutDisplayFunc(display)

    # Now we have an OpenGL context
    version = glGetString(GL_VERSION)
    if version is None:
        print("Failed to get OpenGL version. Context may not exist.")
        glutDestroyWindow(glutGetWindow())
        return

    print("OpenGL version:", version.decode())
    print("Vendor:", glGetString(GL_VENDOR).decode())
    print("Renderer:", glGetString(GL_RENDERER).decode())
    print("GLSL version:", glGetString(GL_SHADING_LANGUAGE_VERSION).decode())

    glutMainLoop()

if __name__ == "__main__":
    main()
