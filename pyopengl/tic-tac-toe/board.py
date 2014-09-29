from locals import *
from settings import *
import gl_misc

class Board(object):
    def __init__(self):
        self.reset()
        
        self.dl_x = glGenLists(1)
        glNewList(self.dl_x,GL_COMPILE)
        glColor4f(1,1,0,1)
        glBegin(GL_LINES)
        glVertex3f(0.1,0.0,0.1); glVertex3f(0.9,0.0,0.9)
        glVertex3f(0.1,0.0,0.9); glVertex3f(0.9,0.0,0.1)
        glEnd()
        glEndList()

        self.dl_o = glGenLists(1)
        glNewList(self.dl_o,GL_COMPILE)
        glColor4f(0,1,1,1)
        glBegin(GL_LINE_STRIP)
        for i in range(0,100+1,1):
            angle = radians(360.0*i/100.0)
            glVertex3f(0.5+0.4*cos(angle),0.0,0.5+0.4*sin(angle))
        glEnd()
        glEndList()
    def __del__(self):
        glDeleteLists(self.dl_x,1)
        glDeleteLists(self.dl_o,1)
        
    def reset(self):
        self.data = []
        for y in range(4):
            layer = []
            for z in range(4):
                row = []
                for x in range(4):
                    row.append(None)
                layer.append(row)
            self.data.append(layer)

    def get_at(self, x,y,z):
        return self.data[y][z][x]
    def set_at(self, x,y,z, piece):
        self.data[y][z][x] = piece

    def calc_projected(self, player):
        #-1 for player's piece here
        #-2 for other player's piece here
        #None for empty
        #<number> for my piece projected from that number's layer index
        proj_data = []
        for y in range(4):
            layer = []
            for z in range(4):
                row = []
                for x in range(4):
                    if   self.data[y][z][x] ==   None: row.append(None)
                    elif self.data[y][z][x] == player: row.append(  -1)
                    elif self.data[y][z][x] != player: row.append(  -2)
                layer.append(row)
            proj_data.append(layer)
        for z in range(4):
            for x in range(4):
                for y1 in range(4):
                    if proj_data[y1][z][x] != -1: continue #only projecting this player's pieces
                    y2 = y1
                    for i in range(3): #project to the three blocks "above"
                        if board_modular:
                            y2 = (y2 + 1) % 4
                        else:
                            y2 += 1
                            if y2 == 4: break
                        if   proj_data[y2][z][x] == None: proj_data[y2][z][x] = y1
                        else: break
                    y2 = y1
                    for i in range(3): #project to the three blocks "below"
                        if board_modular:
                            y2 = (y2 - 1) % 4
                        else:
                            y2 -= 1
                            if y2 < 0: break
                        if   proj_data[y2][z][x] == None: proj_data[y2][z][x] = y1
                        else: break
        return proj_data
    def check_for_solutions(self):
        for player in [1,2]:
            proj_data = self.calc_projected(player)

            solutions = []
            for y in range(4):
                for z in range(4):
                    for x in range(4):
                        #print("Checking (%d,%d,%d)"%(x,y,z))
                        if proj_data[y][z][x] == None: continue #empty
                        if proj_data[y][z][x] ==   -2: continue #other player

                        for dy in [0,-1,1]: #this order allows "more obvious" solutions to be
                            for dz in [0,-1,1]: #found first.  Also, we choose preferentially
                                for dx in [0,-1,1]: #non-projective solutions later.
                                    #print("Inner (%d,%d,%d)"%(dx,dy,dz))
                                    if dx == 0 and dz == 0: continue

                                    coord = [x,y,z]
                                    solution = []
                                    for i in range(4):
                                        block = proj_data[coord[1]][coord[2]][coord[0]]
                                        if block in [-2,None]: #empty or other player's piece
                                            break
                                        if block == -1: #my piece
                                            solution.append([ list(coord), list(coord), False ])
                                        else: #my piece projected; y height of original
                                            solution.append([ list(coord), [coord[0],block,coord[2]], True ])
                                        if board_modular:
                                            coord[0] = (coord[0]+dx)%4
                                            coord[1] = (coord[1]+dy)%4
                                            coord[2] = (coord[2]+dz)%4
                                        else:
                                            coord[0] += dx
                                            coord[1] += dy
                                            coord[2] += dz
                                            if coord[0] < 0 or coord[0] >= 4: break
                                            if coord[1] < 0 or coord[1] >= 4: break
                                            if coord[2] < 0 or coord[2] >= 4: break
                                    if len(solution) == 4:
                                        playing = False
##                                        Board.output(proj_data)
##                                        print((dx,dy,dz))
##                                        coord = [x,y,z]
##                                        print(coord)
##                                        for i in range(4):
##                                            block = proj_data[coord[1]][coord[2]][coord[0]]
##                                            print(str(coord)+" => "+str(block))
##                                            coord[0] = (coord[0]+dx)%4
##                                            coord[1] = (coord[1]+dy)%4
##                                            coord[2] = (coord[2]+dz)%4
                                        solutions.append(solution)
            if solutions != []:
                #Preferentially choose solutions that are the least projective, since they're more "intuitive"
                num_projections = {}
                for solution in solutions:
                    num_projections[int(solution[0][2]) + int(solution[1][2]) + int(solution[2][2]) + int(solution[3][2])] = solution
                for i in range(4):
                    if i in num_projections.keys():
                        return num_projections[i]
        return None

    @staticmethod
    def output(board_data):
        print("[")
        for y in range(4):
            print("  [")
            for z in range(4):
                s = ""
                for x in range(4):
                    v = str(board_data[4-y-1][z][x])
                    while len(v)<4: v=v+" "
                    s += v+"\t"
                print("    ["+s+"]")
            print("  ]")
        print("]")
            
    def draw_pieces(self):
        for y in range(4):
            for z in range(4):
                for x in range(4):
                    piece = self.data[y][z][x]
                    if piece == None: continue
                    
                    glPushMatrix()
                    glTranslatef(x,spacing*y,z)
                    if   piece == 1:
                        glCallList(self.dl_x)
    ##                    if piece != True and piece != False:
    ##                        print(board2)
    ##                        input(piece)
    ##                        glColor4f(1,1,0,1)
    ##                        glBegin(GL_LINES)
    ##                        glVertex3f(0,0,0)
    ##                        glVertex3f(0,-spacing*y + piece,0)
    ##                        glEnd()
                    elif piece == 2:
                        glCallList(self.dl_o)
                    glPopMatrix()
    def draw_grid(self):
        glBegin(GL_LINES)
        for layer in range(4):
            glColor4f(*board_colors[layer])
            for i in range(4+1):
                glVertex3f(i,spacing*layer,0); glVertex3f(i,spacing*layer,4)
                glVertex3f(0,spacing*layer,i); glVertex3f(4,spacing*layer,i)
        glEnd()
    def draw_fill(self):
        for layer in range(4):
            glBegin(GL_QUADS)
            glVertex3f(0,spacing*layer,0)
            glVertex3f(4,spacing*layer,0)
            glVertex3f(4,spacing*layer,4)
            glVertex3f(0,spacing*layer,4)
            glEnd()

    def draw_solution(self, solution):
        for projected, original, uses_projected in solution:
            #print((projected, original))
            if projected[1] != original[1]:
                glColor4f(1,0,1,1)
                #print("Drawing line")
                glPushMatrix()
                glTranslatef(0.5,0.0,0.5)
                glBegin(GL_LINES)
                star_size_x = 0.2
                star_size_y = 0.1
                star_size_z = 0.2
                glVertex3f( original[0], spacing*original[1], original[2]); glVertex3f(projected[0],spacing*projected[1],projected[2])
                glVertex3f(projected[0]-star_size_x,spacing*projected[1]+star_size_y,projected[2]); glVertex3f(projected[0]+star_size_x,spacing*projected[1]-star_size_y,projected[2])
                glVertex3f(projected[0]+star_size_x,spacing*projected[1]+star_size_y,projected[2]); glVertex3f(projected[0]-star_size_x,spacing*projected[1]-star_size_y,projected[2])
                glVertex3f(projected[0],spacing*projected[1]+star_size_y,projected[2]-star_size_z); glVertex3f(projected[0],spacing*projected[1]-star_size_y,projected[2]+star_size_z)
                glVertex3f(projected[0],spacing*projected[1]+star_size_y,projected[2]+star_size_z); glVertex3f(projected[0],spacing*projected[1]-star_size_y,projected[2]-star_size_z)
                glEnd()
                glPopMatrix()
        for projected, original, uses_projected in solution:
            glColor4f(1,1,0,0.5)
            gl_misc.draw_square(projected[0],projected[1],projected[2])
        #input()
        
