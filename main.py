import sys, pygame
pygame.init()
fpsClock = pygame.time.Clock()

size = width, height = 640-3, 640-3
white = (255, 255, 255)
blue = (0,0,255)
screen = pygame.display.set_mode(size)


# def read_pattern():
#     import pdb  
#     pdb.set_trace()
#     pattern_file = open("pattern.txt",'r')
#     lines = pattern_file.readlines()
#     pattern = []
#     for l in lines:
#         pattern.append(list(l)[0:-1])
#     return pattern

# p = read_pattern()


pattern = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]
           
num_cells = len(pattern)
square = width/num_cells 

class Cell:
    def __init__(self,location_x,location_y,size, is_alive=False):
        self.loc_x = location_x
        self.loc_y = location_y
        self.size = size
        self.alive = is_alive 
    
    def is_alive(self):
        return self.alive

    def die(self):
        self.alive = False

    def create(self):
        self.alive = True

    def draw(self):

        if self.is_alive():
            pygame.draw.rect(screen,blue,(self.loc_x,self.loc_y,self.size,self.size))
        else:
            pygame.draw.rect(screen,blue,(self.loc_x,self.loc_y,self.size,self.size),1)


class GameOfLife:

    def __init__(self,cells):
        self.cells = cells
        self.num_cells = num_cells
        self.temp = []
        for row in range(num_cells):
            single_row = []
            for col in range(num_cells):
                cell = Cell(row*square,col*square,square)
                single_row.append(cell)
            self.temp.append(single_row)

    def simulate(self):
        for i in range(1,self.num_cells-1):
            for j in range(1,self.num_cells-1):
                self.rules(i,j)

        for i in range(self.num_cells):
            for j in range(self.num_cells):
                if self.temp[i][j].is_alive():
                    self.cells[i][j].create()
                else:
                    self.cells[i][j].die()
        

    # def print(self,arr):
    #     for i in range(len(arr)):
    #         for j in range(len(arr)):
    #             print(int(arr[i][j].is_alive())," ",end="")
    #         print()
    def count_alive_neighbors(self,x,y):
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if (i+x == x and j+y == y):
                    continue
                count+=int(self.cells[i+x][j+y].is_alive())
        return count

    def rules(self,x,y):
        count = self.count_alive_neighbors(x,y)
        cell = Cell(x*square,y*square,square,self.cells[x][y].is_alive())
        if count < 2 or count >3:
            cell.die()
        elif count == 3:
            cell.create()
        self.temp[x][y] = cell

    def draw(self):
        for i in range(self.num_cells):
            for j in range(self.num_cells):
                self.cells[i][j].draw()


is_white = True
cells = []
for i in range(num_cells):
    row = []
    for j in range(num_cells):
        cell = Cell(j*square,i*square,square,bool(pattern[i][j]))
        row.append(cell)
    cells.append(row)
game_of_life = GameOfLife(cells)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(white)

    game_of_life.draw()
    game_of_life.simulate()
    pygame.display.flip()
    fpsClock.tick(1)



        


