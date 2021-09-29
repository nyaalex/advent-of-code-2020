import gameOfLife


class GameCube(gameOfLife.GameHandler):
    def load_board(self, filename):

        board_file = open(filename)
        self.main_board = gameOfLife.CellSpace(3)
        cell_val = {
            '.': 0,
            '#': 1,
        }

        for x, line in enumerate(board_file):
            for y, cell in enumerate(line.strip()):
                self.main_board[x, y, 0] = cell_val[cell]

        self.t = 0
        board_file.close()
        

if __name__ == '__main__':
    conway_cube = GameCube()
    conway_cube.load_board("input")

    for i in range(6):
        conway_cube.update()

    print(conway_cube.count_occupied())