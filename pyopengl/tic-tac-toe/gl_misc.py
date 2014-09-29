from locals import *
from settings import *

def setup():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)

    glEnable(GL_TEXTURE_2D)
    glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
    glTexEnvi(GL_POINT_SPRITE,GL_COORD_REPLACE,GL_TRUE)

    glHint(GL_PERSPECTIVE_CORRECTION_HINT,GL_NICEST)
    glEnable(GL_DEPTH_TEST)
    
def draw_square(x,y,z):
    glBegin(GL_QUADS)
    glVertex3f(x,  spacing*y,z  )
    glVertex3f(x+1,spacing*y,z  )
    glVertex3f(x+1,spacing*y,z+1)
    glVertex3f(x,  spacing*y,z+1)
    glEnd()

def get_pos_at(windowcoord,flip=True):
    viewport = glGetIntegerv(GL_VIEWPORT)
    winX = windowcoord[0]
    if flip: winY = viewport[3]-windowcoord[1]
    else: winY = windowcoord[1]
    winZ = glReadPixels(winX,winY,1,1,GL_DEPTH_COMPONENT,GL_FLOAT)[0][0]
    return list(gluUnProject(winX,winY,winZ))#,modelview,projection,viewport)

def _rndint(num): return int(round(num))

def set_view_2D(rect):
    glViewport(*list(map(_rndint,rect)))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(rect[0],rect[0]+rect[2], rect[1],rect[1]+rect[3], -1.0,1.0);
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
def set_view_3D(rect):
    glViewport(*list(map(_rndint,rect)))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if which_camera < 3:
        gluPerspective(camera_fov,float(screen_size[0])/float(screen_size[1]), 0.1, 100.0)
    else:
        glOrtho(-10.0,10.0, -10.0,10.0, -100.0,100.0);
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def set_camera(rect=[0,0,screen_size[0],screen_size[1]], cen=camera_center,rot=camera_rot,rad=camera_radius):
    set_view_3D(rect)
    
    camera_pos = [
        cen[0] + rad*cos(radians(rot[0]))*cos(radians(rot[1])),
        cen[1] + rad                     *sin(radians(rot[1])),
        cen[2] + rad*sin(radians(rot[0]))*cos(radians(rot[1]))
    ]
    gluLookAt(
        camera_pos[0],camera_pos[1],camera_pos[2],
        cen[0],cen[1],cen[2],
        0,1,0
    )
