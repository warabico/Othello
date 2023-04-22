import constant as C

E = C.STONE_EMPTY
B = C.STONE_BLACK
W = C.STONE_WHITE

INIT_BOARD = [
    [ E, E, E, E, E, E, E, E ],
    [ E, E, E, E, E, E, E, E ],
    [ E, E, E, E, E, E, E, E ],
    [ E, E, E, W, B, E, E, E ],
    [ E, E, E, B, W, E, E, E ],
    [ E, E, E, E, E, E, E, E ],
    [ E, E, E, E, E, E, E, E ],
    [ E, E, E, E, E, E, E, E ]
]

class Board(object):
    def __init__(self):
        self.board = INIT_BOARD

    @property
    def board_str(self):
        str = ''

        str += '\t   '
        for char_col in C.CHAR_COLS:
            str += ' ' + char_col
        str += '\n'
        str += '\t  +-----------------+'
        str += '\n'

        for row_idx in range(C.ROWS):
            str += '\t' + C.CHAR_ROWS[row_idx] + ' |'
            for col_idx in range(C.COLS):
                str += ' ' + C.CHAR_STONES[self.board[row_idx][col_idx]]
            str += ' |'
            str += '\n'
        str += '\t  +-----------------+'
        str += '\n'

        return str

    def put_cmd(self, stone, cmd):
        row, col = self.cmd2xy(cmd)
        self.__put(stone, row, col)
    
    def put_xy(self, stone, row, col):
        self.__put(stone, row, col)
        
    def __put(self, stone, row, col):
        reversibles = self.get_reversibles(stone, row, col)
        if len(reversibles) > 0:
            self.board[row][col] = stone
            for (x, y) in reversibles:
                self.board[y][x] = stone
            return True
        else:
            return False

    def get_reversibles(self, stone, row, col):
        reversibles = []

        if stone == C.STONE_BLACK:
            enemy = C.STONE_WHITE
        elif stone == C.STONE_WHITE:
            enemy = C.STONE_BLACK
        else:
            return reversibles
        
        if self.board[row][col] != C.STONE_EMPTY:
            return reversibles

        for (dx, dy) in C.DIRECTIONS:
            temp_reversibles = []
            scan_flag = True
            x = col + dx
            y = row + dy

            while scan_flag:
                if self.is_valid_xy(x, y):
                    temp_stone = self.board[y][x]
                    if temp_stone == stone:
                        reversibles.extend(temp_reversibles)
                        scan_flag = False
                    elif temp_stone == enemy:
                        temp_reversibles.append((x, y))
                        x = x + dx
                        y = y + dy
                    else:
                        temp_reversibles = []
                        scan_flag = False
                else:
                    scan_flag = False

        return reversibles

    @staticmethod
    def is_valid_xy(x, y):
        return x >= C.IDX_MIN and x <= C.IDX_MAX and y >= C.IDX_MIN and y <= C.IDX_MAX
    
    @staticmethod
    def cmd2xy(cmd):
        x = C.CHAR_COLS.index(cmd[0])
        y = C.CHAR_ROWS.index(cmd[1])
        return y, x

if __name__ == '__main__':
    board = Board()
    print(board.board_str)
    board.put_cmd(C.STONE_BLACK, 'C4')
    board.put_cmd(C.STONE_WHITE, 'C3')
    board.put_cmd(C.STONE_BLACK, 'D3')
    board.put_cmd(C.STONE_WHITE, 'E3')
    board.put_cmd(C.STONE_BLACK, 'F2')
    board.put_cmd(C.STONE_WHITE, 'E2')
    board.put_cmd(C.STONE_BLACK, 'D2')
    board.put_cmd(C.STONE_WHITE, 'C1')
    board.put_cmd(C.STONE_BLACK, 'B2')
    board.put_cmd(C.STONE_WHITE, 'A1')
    board.put_cmd(C.STONE_BLACK, 'F4')
    board.put_cmd(C.STONE_WHITE, 'C5')
    print(board.board_str)