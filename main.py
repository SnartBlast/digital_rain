from rain import Rain
from board import Board
from fastRain import FastRain
import sys
import time

if __name__ == "__main__":
    # define command line parameters
    width = 0
    height = 0
    option = 0

    # update command line arguments
    if (len(sys.argv) == 2):
        if (sys.argv[1] == '1'):
            width = 40
            height = 40
            option = 1 

        if (sys.argv[1] == '2'):
            width = 51
            height = 55
            option = 2

        if (sys.argv[1] == '3'):
            width = 53
            height = 60
            option = 3

        if (sys.argv[1] == '4'):
            width = 53
            height = 60
            option = 4

        if (sys.argv[1] == '5'):
            width = 34
            height = 55
            option = 5
    else:
        width = 51
        height = 55
        option = 2


    # define necessary classes
    rain = Rain(width, height)
    fast_rain = FastRain(width, height)
    board = Board(width, height)

    # print lines
    if (option == 1):
        while (True):
            time.sleep(0.13)
            board.mutate()
            rain.update()

            for y in range(height):
                print()
                for x in range(width):
                    # find char and state at position
                    char = board.board[y][x]
                    state = rain.rain[y][x]

                    if (state < 13):
                        print(char, end="")
                    else:
                        print("  ", end="", )


    # print digital rain
    elif (option == 2):
        # colors
        ESC = '\x1b'
        CLEAR = '[2J'
        WHITE = '[38;5;15m'
        GREEN0 = '[38;5;46m'
        GREEN1 = '[38;5;40m'
        GREEN2 = '[38;5;34m'
        GREEN3 = '[38;5;28m'
        GREEN4 = '[38;5;22m'
        GREEN5 = '[38;5;237m'
        BLACK  = '[38;5;236m'

        # begin loop
        while (True):
            # mutate and update 
            board.mutate()
            rain.update()
            fast_rain.update()
            time.sleep(0.13)
            screen = ''

            for i in range(len(rain.rain)):
            #for line in rain.rain:
                screen += '\n'

                for j in range(len(rain.rain[i])):
                #for char in line:
                    char = board.board[i][j]
                    state = rain.rain[i][j]  
                    if (fast_rain.rain[i][j] < rain.rain[i][j]):
                        state = fast_rain.rain[i][j] 

                    # add elements to screen string 
                    if (state == 1):
                        screen += ESC + WHITE + str(char)

                    elif (2 <= state < 5):
                        screen += ESC + GREEN0 + str(char)

                    elif (5 <= state < 7):
                        screen += ESC + GREEN1 + str(char) 

                    elif (7 <= state < 10):
                        screen += ESC + GREEN2 + str(char)

                    elif (10 <= state < 12):
                        screen += ESC + GREEN3 + str(char)

                    elif (12 <= state < 14):
                        screen += ESC + GREEN4 + str(char)

                    elif (14 <= state < 16):
                        screen += ESC + GREEN5 + str(char)

                    else:    
                        screen += ESC + BLACK + str(char)

            screen += '\n'
            print(screen)
            print(ESC + CLEAR)



    # print digital rain, improved ansi
    elif (option == 3):
        rain.pulse()        


   # print character board
    elif (option == 4):
        while (True):
            time.sleep(0.3)
            board.printBoard()
            board.mutate()


    #print rain board
    elif (option == 5):

        while (True):
            time.sleep(0.15)
            screen = ''
            for line in rain.rain:
                screen += '\n'
                for char in line:
                    if (char < 10):
                        screen += str(char) + '  ' 
                    else:
                        screen += str(char) + ' '

            print(screen)
            rain.update()


