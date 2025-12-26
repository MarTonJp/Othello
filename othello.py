import pygame
from othello_board import OthelloBoard, PLAYER1, PLAYER2
from othello_ui import OthelloUI
from othello_ui import SCREEN_X, SCREEN_Y, INFOMATOIN_AREA

def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((SCREEN_X + INFOMATOIN_AREA, SCREEN_Y))
    pygame.display.set_caption("Othello")
    clock = pygame.time.Clock()

    board = OthelloBoard()
    ui = OthelloUI(screen, board)

    black_count = board.count_piece(PLAYER1)
    white_count = board.count_piece(PLAYER2)

    player = PLAYER1
    running = True
    while running:
        for event in pygame.event.get():
            # 閉じるを押したとき終了する
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                player = ui.click_button(event.pos, player)
                black_count = board.count_piece(PLAYER1)
                white_count = board.count_piece(PLAYER2)

        # 盤面の表示
        ui.draw_board()
        ui.draw_infomation(player, black_count, white_count)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

    return

if __name__ == "__main__":
    main()
