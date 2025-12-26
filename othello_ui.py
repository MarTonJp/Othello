import pygame
from othello_board import OthelloBoard, PLAYER1, PLAYER2

CELL_SIZE = 50
CELL_GAP  = 3
CIRCLE_SIZE = CELL_SIZE / 2 - CELL_GAP

SCREEN_X = (CELL_SIZE+CELL_GAP)*8+CELL_GAP
SCREEN_Y = (CELL_SIZE+CELL_GAP)*8+CELL_GAP
INFOMATOIN_AREA = 120

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class CellUI:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((CELL_SIZE + CELL_GAP) * self.x + CELL_GAP, (CELL_SIZE + CELL_GAP) * self.y + CELL_GAP, CELL_SIZE, CELL_SIZE)


class OthelloUI:
    def __init__(self, screen, board: OthelloBoard):
        self.screen = screen
        self.board = board
        self.cells = [[CellUI(x, y) for x in range(8)] for y in range(8)]

        self.font = pygame.font.SysFont("msuiogothic", 36)

    def draw_board(self):
        pygame.draw.rect(self.screen, (0,128,0), pygame.Rect(SCREEN_X, CELL_GAP, INFOMATOIN_AREA - CELL_GAP, SCREEN_Y - CELL_GAP * 2))
        for y in range(8):
            for x in range(8):
                pygame.draw.rect(self.screen, (0,128,0), self.cells[y][x])
        
        _y = 1
        for _y in range(8):
            for _x in range(8):
                state = self.board.get_board_value(_x, _y)
                if  state != 0:
                    y = (CELL_SIZE + CELL_GAP) * _y + CELL_SIZE / 2 + CELL_GAP
                    x = (CELL_SIZE + CELL_GAP) * _x + CELL_SIZE / 2 + CELL_GAP
                    piece_color = BLACK if state == PLAYER1 else WHITE 
                    pygame.draw.circle(self.screen, piece_color, (x,y), CIRCLE_SIZE)
    
    def draw_infomation(self, player, black_count, white_count):
        turn_str = "Turn"
        turn_text = self.font.render(turn_str, True, (255, 255, 255))
        self.screen.blit(turn_text, (SCREEN_X + 30, 20))

        player_str = "Black's" if player == PLAYER1 else "White's"
        player_text = self.font.render(player_str, True, (255, 255, 255))
        self.screen.blit(player_text, (SCREEN_X + 20, 50))


        score_str = "Score"
        score_text = self.font.render(score_str, True, (255, 255, 255))
        self.screen.blit(score_text, (SCREEN_X + 25, 100))

        pygame.draw.circle(self.screen, BLACK, (SCREEN_X + 20, 150), 10)
        black_str = f"{black_count:2d}"
        black_text = self.font.render(black_str, True, (255, 255, 255))
        self.screen.blit(black_text, (SCREEN_X + 45, 140))

        pygame.draw.circle(self.screen, WHITE, (SCREEN_X + 20, 180), 10)
        white_str = f"{white_count:2d}"
        white_text = self.font.render(white_str, True, (255, 255, 255))
        self.screen.blit(white_text, (SCREEN_X + 45, 170))

        return
    
    def click_button(self, pos, player):
        result = False
        for empty in self.board.empty_list:
            cell = self.cells[empty[1]][empty[0]]
            rect = cell.rect
            if rect.collidepoint(pos):
                if self.board.flip_piece(cell.x, cell.y, player):
                    player *= -1

        return player

def main():
    return

if __name__ == "__main__":
    main()
