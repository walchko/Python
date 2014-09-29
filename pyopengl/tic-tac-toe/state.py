from locals import *
import board as board_module, gl_misc
from settings import *

STATE_MENU = 1
STATE_PLAY = 2
STATE_END = 3

def init():
    global state, font18,font36
    state = StateMenu()
    font18 = pygame.font.SysFont("Times New Roman",18)
    font36 = pygame.font.SysFont("Times New Roman",36)
    
class State(object):
    def __init__(self):
        #self.state = STATE_MENU
        pass
    def handle_input(self):
        global keys_pressed,mouse_buttons,mouse_position,mouse_rel

        keys_pressed = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_position = list(pygame.mouse.get_pos())
        mouse_position[1] = screen_size[1] - mouse_position[1]
        mouse_rel = pygame.mouse.get_rel()

        for event in pygame.event.get():
            if   event.type == QUIT: return False
            elif event.type == KEYDOWN:
                if not self._process_keydown(event): return False
            elif event.type == MOUSEBUTTONDOWN:
                if not self._process_mousebuttondown(event): return False
        self._process_misc()
        
        return True
    def draw_surf(self, surf, x,y):
        w,h = surf.get_size()
        data = pygame.image.tostring(surf,"RGBA",1)
        glRasterPos2f(x,y)
        glDrawPixels(w,h,GL_RGBA,GL_UNSIGNED_BYTE,data)
        glRasterPos2i(0,0)
class StateMenu(State):
    def __init__(self):
        State.__init__(self)

        self.hovering = None
    def _process_mousebuttondown(self, event):
        global state
        if event.button == 1:
            if   self.hovering == 0: #Two-Player
                state = StateGame()
            elif self.hovering == 1: #Tutorial
                state = StateTutorial()
            elif self.hovering == 2: #Exit
                return False
        return True
    def _process_keydown(self, event):
        if   event.key == K_ESCAPE: return False
        return True
    def _process_misc(self):
        pass
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        gl_misc.set_view_2D([0,0,screen_size[0],screen_size[1]])
        
        def get_drawloc(surf, index):
            return [
                screen_size[0]/2 - surf. get_width()/2,
                screen_size[1]/2 - surf.get_height()/2 - 50*index
            ]
        def draw_choice(text, index):
            surf = font36.render(text,True,(255,255,255))
            loc = get_drawloc(surf,index)

            c = [0.6,0.6,0.6, 1.0]
            if     mouse_position[0]>loc[0] and mouse_position[0]<loc[0]+surf. get_width():
                if mouse_position[1]>loc[1] and mouse_position[1]<loc[1]+surf.get_height():
                    self.hovering = index
                    c = [0.8,0.8,0.0, 1.0]
            c = list(map(lambda x:int(round(255.0*x)),c))
            
            surf = font36.render(text,True,c).convert_alpha()
            
            #glColor4f(c[0],c[1],c[2], 1.0)
            self.draw_surf(surf, loc[0],loc[1])
        self.hovering = None
        draw_choice("Two-Player",0)
        draw_choice(  "Tutorial",1)
        draw_choice(      "Exit",2)
class StateTutorial(State):
    def __init__(self):
        State.__init__(self)
        
        self.index = 0
        self.solution = None
        self.setup_example()
    def _process_mousebuttondown(self, event): return True
    def _process_keydown(self, event):
        global state
        if   event.key == K_ESCAPE: state = StateMenu()
        elif event.key == K_RETURN:
            self.index += 1
            self.setup_example()
        return True
    def _process_misc(self): pass
    def setup_example(self):
        global state
        if   self.index == 0:
            text = "The object of the game is\nto get four in a row."
            pieces = [[0,0,0, 1],[1,0,1, 1],[2,0,2, 1],[3,0,3, 1]]
        elif self.index == 1:
            text = "This can be accomplished by\nmoving through different\nlayers, as long as it is not\ncompletely vertical."
            pieces = [[1,0,0, 1],[1,1,1, 1],[1,2,2, 1],[1,3,3, 1]]
        elif self.index == 2:
            text = "Pieces project up and down\nthrough the four boards."
            pieces = [[0,0,1, 1],[1,0,1, 1],[2,2,1, 1],[3,0,1, 1]]
        elif self.index == 3:
            text = ". . . except when blocked\nfrom doing so by the\nother side's pieces."
            pieces = [[0,0,0, 1],[0,2,0, 2],[1,1,1, 2],[1,2,1, 1],[2,0,2, 1],[2,2,2, 2],[3,0,3, 1]]
        elif self.index == 4:
            text = "Right click or arrow keys to rotate\nLeft click to place\n\nHave fun!"
            pieces = []
        elif self.index == 5:
            state = StateMenu()
            return
        self.board = board_module.Board()
        for piece in pieces: self.board.set_at(*piece)
        self.solution = self.board.check_for_solutions()
        self.surfs = [font18.render(line,True,(255,255,255)) for line in text.split("\n")]
    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        gl_misc.set_view_2D([0,0,screen_size[0]/4,screen_size[1]])

        i = 0
        for surf in self.surfs:
            self.draw_surf(surf, 50,screen_size[1]/2-i*25)
            i += 1

        gl_misc.set_camera(
            [screen_size[0]/4,0,3*screen_size[0]/4,screen_size[1]],
            gl_misc.camera_center,
            camera_rot_def,
            camera_radius_def
        )

        self.board.draw_pieces()
        self.board.draw_grid()
        if self.solution != None:
            self.board.draw_solution(self.solution)
        
class StateGame(State):
    def __init__(self):
        State.__init__(self)

        self.playing = True
        self.turn = 1
        self.board = board_module.Board()

        self.cursor_pos = [0,0,0]
        self.cursor_valid = False
        self.solution = None

    def _process_mousebuttondown(self, event):
        if event.button == 1:
            if self.cursor_valid and self.playing:
                self.board.set_at(
                    self.cursor_pos[0],self.cursor_pos[1],self.cursor_pos[2],
                    self.turn
                )
                self.solution = self.board.check_for_solutions()
                if self.solution != None:
                    self.playing = False
                self.turn = 3 - self.turn
        elif event.button == 4: gl_misc.camera_radius -= 0.5
        elif event.button == 5: gl_misc.camera_radius += 0.5
        return True
    def _process_keydown(self, event):
        global state
        if event.key == K_ESCAPE: state = StateMenu()
        return True
    def _process_misc(self):
        if mouse_buttons[2]:
            if not self.cursor_valid:
                gl_misc.camera_rot[0] += mouse_rel[0]
                gl_misc.camera_rot[1] += mouse_rel[1]
        if keys_pressed[ K_LEFT]: gl_misc.camera_rot[0] += 2
        if keys_pressed[K_RIGHT]: gl_misc.camera_rot[0] -= 2
        if keys_pressed[   K_UP]: gl_misc.camera_rot[1] += 2
        if keys_pressed[ K_DOWN]: gl_misc.camera_rot[1] -= 2
    
    def draw(self):
        gl_misc.set_camera()
        
        glClear(GL_DEPTH_BUFFER_BIT)

        self.board.draw_fill()

        self.cursor_pos = gl_misc.get_pos_at(mouse_position,False)
        self.cursor_pos[0] = int(      self.cursor_pos[0]         )
        self.cursor_pos[1] = int(round(self.cursor_pos[1]/spacing))
        self.cursor_pos[2] = int(      self.cursor_pos[2]         )
        self.cursor_valid =\
            self.playing and\
            self.cursor_pos[0]>=0 and self.cursor_pos[0]<=3 and\
            self.cursor_pos[1]>=0 and self.cursor_pos[1]<=3 and\
            self.cursor_pos[2]>=0 and self.cursor_pos[2]<=3 and\
            self.board.get_at(*self.cursor_pos) == None
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        self.board.draw_pieces()
        self.board.draw_grid()
        
        if not self.playing:
            self.board.draw_solution(self.solution)
            
        if self.playing:
            if self.cursor_valid:
                c = board_colors[self.cursor_pos[1]]
                glColor4f(c[0],c[1],c[2],0.4)
                gl_misc.draw_square(*self.cursor_pos)

        glColor4f(1,1,1,1)






