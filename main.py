
class Board:
    def __init__(self):
        self.size = 8
        self.grid = [[str(0) for i in range(self.size)] for j in range(self.size)]

    def get_grid(self):
        return self.grid

    def display_grid(self):
        print(["x","a","b","c","d","e","f","g","h"])
        count = 8
        for row in self.grid:
            disp_row = [str(count)]
            for square in row:
                if type(square) == str:
                    disp_row = disp_row + [square]
                else:
                    disp_row = disp_row +[square.icon]

            print(disp_row)
            count = count - 1




class Piece:

    def __init__(self, board_grid, location, colour):
        self.icon = "X"
        self.moves = []
        self.taking_moves = []
        self.can_jump = False
        self.location = location
        self.board_grid = board_grid
        self.colour = colour
        board_grid[self.location[0]][self.location[1]] = self

    def get_location(self, board_grid, location, colour):
        return self.location

    def move(self):
        pass


class Pawn(Piece):
    def __init__(self,board_grid, location, colour):
        super().__init__(board_grid, location, colour)
        self.moves = [[0,1]]
        self.taking_moves = [[-1,1],[1,1]]
        self.icon = "PWN"

class Bishop(Piece):
    def __init__(self,board_grid, location, colour):
        super().__init__(board_grid, location, colour)
        self.moves = [[num,num] for num in range(1,8)] + [[num,-num] for num in range(1,8)] + [[-num,num] for num in range(1,8)] + [[-num,-num] for num in range(1,8)]
        self.taking_moves = moves
        self.icon = "PWN"

c_board = Board()

test_piece = Pawn(c_board.get_grid(), [5,5], "Black")

c_board.display_grid()