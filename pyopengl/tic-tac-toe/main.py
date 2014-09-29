#!/usr/bin/env python
from locals import *

if sys.platform in ["win32","win64"]: os.environ["SDL_VIDEO_CENTERED"]="1"
pygame.display.init()
pygame.font.init()

import gl_misc
import state as state_module
from settings import *

icon = pygame.Surface((1,1)); icon.set_alpha(0); pygame.display.set_icon(icon)
pygame.display.set_caption("3D Projective Tic Tac Toe - Ian Mallett - v.1.0.0 - 2013")
if multisample:
    pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS,1)
    pygame.display.gl_set_attribute(GL_MULTISAMPLESAMPLES,multisample)
pygame.display.set_mode(screen_size,OPENGL|DOUBLEBUF)

gl_misc.setup()

def main():
    state_module.init()
    
    clock = pygame.time.Clock()
    while True:
        if not state_module.state.handle_input(): break
        state_module.state.draw()
        pygame.display.flip()
        
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()
        pygame.quit()
        input()
