#!/usr/bin/env python
#
# Kevin J. Walchko
# 22 Sept 2014
#
"""OpenGL rendering simulation"""
import sys
import ctypes

from OpenGL import GL, GLU
import sdl2


def draw_square(x,y,z):
	spacing = 10.0
	GL.glBegin(GL.GL_QUADS)
	GL.glColor3f(1.0, 0.0, 0.0)
	GL.glVertex3f(x,  spacing*y,z  )
	GL.glVertex3f(x+1,spacing*y,z  )
	GL.glVertex3f(x+1,spacing*y,z+1)
	GL.glVertex3f(x,  spacing*y,z+1)
	GL.glEnd()

def draw_triangle(x,y):	
	GL.glBegin(GL.GL_TRIANGLES)
	GL.glColor3f(1.0, 0.0, 0.0)
	GL.glVertex2f(x, y + 90.0)
	GL.glColor3f(0.0, 1.0, 0.0)
	GL.glVertex2f(x + 90.0, y - 90.0)
	GL.glColor3f(0.0, 0.0, 1.0)
	GL.glVertex2f(x - 90.0, y - 90.0)
	GL.glEnd()

def run():
    if sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO) != 0:
        print(sdl2.SDL_GetError())
        return -1

    window = sdl2.SDL_CreateWindow("OpenGL demo",
                                   sdl2.SDL_WINDOWPOS_UNDEFINED,
                                   sdl2.SDL_WINDOWPOS_UNDEFINED, 800, 600,
                                   sdl2.SDL_WINDOW_OPENGL)
    if not window:
        print(sdl2.SDL_GetError())
        return -1

    context = sdl2.SDL_GL_CreateContext(window)

    GL.glMatrixMode(GL.GL_PROJECTION | GL.GL_MODELVIEW)
    GL.glLoadIdentity()
    GL.glOrtho(-400, 400, 300, -300, 0, 1)
    #GL.glOrtho(-40, 40, 30, -30, 0, 1)

    x = 0.0
    y = 30.0

    event = sdl2.SDL_Event()
    running = True
    while running:
        while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == sdl2.SDL_QUIT:
                running = False

        GL.glClearColor(0, 0, 0, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glRotatef(10.0, 0.0, 0.0, 1.0)
        
        draw_square(x,y,0)
        #draw_triangle(x,y)
        

        sdl2.SDL_GL_SwapWindow(window)
        sdl2.SDL_Delay(10)
    sdl2.SDL_GL_DeleteContext(context)
    sdl2.SDL_DestroyWindow(window)
    sdl2.SDL_Quit()
    return 0

if __name__ == "__main__":
    sys.exit(run())