board={'7':' ','8':' ','9':' ','4':' ','5':' ','6':' ','1':' ','2':' ','3':' '}
board_keys = []

for key in board:
    board_keys.append(key)


def printboard(board):
    print( board[7] + '|' + board[8] +'|' + board[9])
    print('----------')
    print( board[4] + '|' + board[5] +'|' + board[6])
    print('----------')
    print( board[1] + '|' + board[2] +'|' + board[3])


def game():
    turn='X'
    count=0

    for i in range(10):
        printboard(board)
        print("It's your turn",turn)
        move=input()
        if board[move]==" ":
            board[move]=turn
            count+=1
        else:
            print("It's already filled enter another position.")
            continue


        if count>=5:

             if board['7'] == board['8'] == board['9'] != ' ': 
                    printBoard(board)
                    print("\nGame Over.\n")                
                    print(" ** " +turn + " won. **")                
                    break
             elif board['4'] == board['5'] == board['6'] != ' ': 
                    printBoard(board)
                    print("\nGame Over.\n")                
                    print(" ** " +turn + " won. **")                
                    break
             elif board['1'] == board['2'] == board['3'] != ' ': 
                    printBoard(board)
                    print("\nGame Over.\n")                
                    print(" ** " +turn + " won. **")                
                    break
             elif board['7'] == board['4'] == board['1'] != ' ': 
                    printBoard(board)
                    print("\nGame Over.\n")                
                    print(" ** " +turn + " won. **")                
                    break
             elif board['8'] == board['5'] == board['2'] != ' ': 
                    printBoard(board)
                    print("\nGame Over.\n")                
                    print(" ** " +turn + " won. **")                
                    break
             elif board['9'] == board['6'] == board['3'] != ' ': 
                    printBoard(board)
                    print("\nGame Over.\n")                
                    print(" ** " +turn + " won. **")                
                    break
             elif board['7'] == board['5'] == board['3'] != ' ': 
                    printBoard(board)
                    print("\nGame Over.\n")                
                    print(" ** " +turn + " won. **")                
                    break
             elif board['1'] == board['5'] == board['9'] != ' ': 
                    printBoard(board)
                    print("\nGame Over.\n")                
                    print(" ** " +turn + " won. **")                
                    break
        if count=='9':
            print("Game Over.It's a tie.")

        if turn=='X':
            turn='O'
        else:
            turn='X'

    restart=input("Do you want to restart?")
    if restart=='y':
        for key in board:
            Board_keys[move]=" "
        game()


if __name__ == "__main__":
    print("TIC TAC TOE GAME")
    game()
