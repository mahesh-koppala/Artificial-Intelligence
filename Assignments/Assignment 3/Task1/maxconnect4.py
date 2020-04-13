import sys
from MaxConnect4Game import MaxConnect4game
import time

def play_human(gameboard):
    while gameboard.getPieceCount() != 42:
        print("It is Human's turn.")
        userTurn = int(input("Enter a column number between 1 - 7 for your play : "))
        if not 0 < userTurn < 8:
            print("Invalid Column, please Enter Again.")
            continue
        if not gameboard.playPiece(userTurn - 1):
            print("Column number: %d is full. Try other column." % userTurn)
            continue
        print("You made a move in column : " + str(userTurn))
        gameboard.display_gameboard()
        gameboard.gameFile = open("human.txt", 'w')
        gameboard.printGameBoardToFile()
        gameboard.gameFile.close()
        if gameboard.getPieceCount() == 42:
            print("further moves are not possible, the game is over.")
            gameboard.count_score()
            print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))
            break
        else:
            print("AI is computing based on next " + str(gameboard.depth) + " steps!")
            gameboard.change_move()
            gameboard.aiPlay()
            gameboard.display_gameboard()
            gameboard.gameFile = open('computer.txt', 'w')
            gameboard.printGameBoardToFile()
            gameboard.gameFile.close()
            gameboard.count_score()
            print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))

def interactive_mode(gameboard, next_player):
    print('Current Board state')
    gameboard.display_gameboard()
    gameboard.count_score()
    print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))
    if next_player == 'human-next':
        play_human(gameboard)
    else:
        gameboard.aiPlay()
        gameboard.gameFile = open('computer.txt', 'w')
        gameboard.printGameBoardToFile()
        gameboard.gameFile.close()
        gameboard.display_gameboard()
        gameboard.count_score()
        print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))
        play_human(gameboard)

    if gameboard.getPieceCount() == 42:
        if gameboard.player1Score > gameboard.player2Score:
            print("Player 1 wins !")
        if gameboard.player1Score == gameboard.player2Score:
            print("The game is a Tie !")
        if gameboard.player1Score < gameboard.player2Score:
            print("Player 2 wins !")
        print("Game Over")


def one_move_mode(gameboard):
    start_time = time.time()
    if gameboard.piece_count >= 42:
        print('Game board is full !\n Game Over !')
        sys.exit(0)
    print ('Gameboard state before move:')
    gameboard.display_gameboard()
    gameboard.aiPlay()
    print ('Gameboard state after move:')
    gameboard.display_gameboard()
    gameboard.count_score()
    print('Score: Player-1 = %d, Player-2 = %d\n' % (gameboard.player1Score, gameboard.player2Score))
    gameboard.printGameBoardToFile()
    gameboard.gameFile.close()
    print("Total Execution Time:")
    print (time.time() - start_time)


def main(argv):
    gameboard = MaxConnect4game()
    try:
        gameboard.gameFile = open(argv[2], 'r')
        file_lines = gameboard.gameFile.readlines()
        gameboard.gameboard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
        gameboard.current_move = int(file_lines[-1][0])
        gameboard.gameFile.close()
    except:
        print('File not found, begin new game.')
        gameboard.current_move = 1
    gameboard.checkPieceCount()
    gameboard.depth = argv[4]
    if argv[1] == 'one-move':
        try:
            gameboard.gameFile = open(argv[3], 'w')
        except:
            sys.exit('Error while opening output file.')
        one_move_mode(gameboard)
    else:
        interactive_mode(gameboard, argv[3])


main(sys.argv)
