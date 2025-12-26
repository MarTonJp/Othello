PLAYER1 = 1
PLAYER2 = -1

class OthelloBoard:
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.empty_list = [(x,y) for x in range(8) for y in range(8)]

        self.place_piece(3,3, PLAYER1)
        self.place_piece(4,4, PLAYER1)

        self.place_piece(3,4, PLAYER2)
        self.place_piece(4,3, PLAYER2)

        return

    def print_board(self):
        print()
        for y in range(8):
            for x in range(8):
                print(f"{self.board[y][x]:3d}", end="")
            print()
    
    def get_board_value(self, x, y):
        return self.board[y][x]

    def count_piece(self, player):
        count = 0
        for y in range(8):
            for x in range(8):
                count += 1 if self.board[y][x] == player else 0
    
        return count

    def place_piece(self, x, y, player):
        self.board[y][x] = player
        if (x,y) in self.empty_list:
            self.empty_list.remove((x,y))
           
        return

    def check_flip_piece(self, x, y, player):
        opponent = -player
        target_piece = []
        for dx, dy in self.directions:
            tx = x + dx
            ty = y + dy
            count = 0
            _piece = []
            while 0 <= tx < 8 and 0 <= ty < 8 and self.board[ty][tx] == opponent:
                _piece.append((tx,ty))
                tx += dx
                ty += dy
                count += 1
            if count > 0 and 0 <= tx < 8 and 0 <= ty < 8 and self.board[ty][tx] == player:
                for _p in _piece:
                    target_piece.append(_p)

        return target_piece
    
    def flip_piece(self, x, y, player):
        result = False
        target_piece = self.check_flip_piece(x, y, player)
        if len(target_piece):
            result = True
            self.place_piece(x, y, player)
            for tx, ty in target_piece:
                self.place_piece(tx, ty, player)

        return result
    
def main():
    return

if __name__ == "__main__":
    main()
