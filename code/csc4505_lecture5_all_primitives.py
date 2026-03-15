import pygame
from pygame.locals import *
from OpenGL.GL import *

def fxn_draw_points():
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    glVertex3f(-0.8, 0.8, 0); glVertex3f(0.8, 0.8, 0)
    glVertex3f(0.8,-0.8, 0); glVertex3f(-0.8,-0.8, 0)
    glEnd()

def fxn_draw_lines():
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex3f(-0.5, 0.5, 0); glVertex3f(0.5,-0.5, 0)
    glVertex3f(-0.5,-0.5, 0); glVertex3f(0.5, 0.5, 0)
    glEnd()

def fxn_draw_line_strip():
    glBegin(GL_LINE_STRIP)
    glColor3f(1,1,0)
    glVertex3f(-0.9,0.2,0); glVertex3f(-0.6,0.5,0); glVertex3f(-0.3,0.2,0)
    glVertex3f(0.0,0.5,0); glVertex3f(0.3,0.2,0); glVertex3f(0.6,0.5,0); glVertex3f(0.9,0.2,0)
    glEnd()

def fxn_draw_line_loop():
    glBegin(GL_LINE_LOOP)
    glColor3f(0,1,1)
    glVertex3f(-0.7,-0.2,0); glVertex3f(0.7,-0.2,0); glVertex3f(0.0,-0.7,0)
    glEnd()

def fxn_draw_triangles():
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0); glVertex3f(-0.8,-0.8,0)
    glColor3f(0,1,0); glVertex3f(-0.2,-0.8,0)
    glColor3f(0,0,1); glVertex3f(-0.5,-0.3,0)
    glEnd()

def fxn_draw_triangle_fan():
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,1)
    glVertex3f(0.5,-0.5,0); glVertex3f(0.8,-0.5,0); glVertex3f(0.8,-0.2,0); glVertex3f(0.5,-0.2,0)
    glEnd()

def fxn_draw_triangle_strip():
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1,0,1)
    glVertex3f(0.2,0.2,0); glVertex3f(0.5,0.5,0); glVertex3f(0.5,0.2,0)
    glVertex3f(0.8,0.5,0); glVertex3f(0.8,0.2,0)
    glEnd()

def fxn_draw_all():
    fxn_draw_points()
    fxn_draw_lines()
    fxn_draw_line_strip()
    fxn_draw_line_loop()
    fxn_draw_triangles()
    fxn_draw_triangle_fan()
    fxn_draw_triangle_strip()

def main():
    var_running = True
    var_display = (800, 600)

    pygame.init()
    pygame.display.set_mode(var_display, DOUBLEBUF | OPENGL | RESIZABLE)
    pygame.display.set_caption("3D Cube")
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

        fxn_draw_all()

        pygame.display.flip()
        var_clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
