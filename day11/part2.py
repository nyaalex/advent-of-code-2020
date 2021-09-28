import part1


class SightBoard(part1.GameBoard):

    def rule(self, x, y):
        floor = '.'
        occupied = '#'
        empty = 'L'

        current_cell = self.arr[x][y]
        if current_cell == floor:
            return floor

        occupied_count = 0
        for dx, dy in self.directions:
            sub_x, sub_y = x + dx, y + dy

            while sub_y not in (-1, self.max_y) and \
                    sub_x not in (-1, self.max_x):
                cell = self.arr[sub_x][sub_y]
                if cell == floor:
                    sub_x += dx
                    sub_y += dy
                elif cell == occupied:
                    occupied_count += 1
                    break
                else:
                    break

        if occupied_count >= 5:
            return empty
        elif current_cell == empty and occupied_count == 0:
            return occupied
        else:
            return current_cell


if __name__ == '__main__':
    board = SightBoard()
    board.load_board("input")

    has_changed = True
    while has_changed:
        has_changed = board.update()

    print(board.count_occupied())
