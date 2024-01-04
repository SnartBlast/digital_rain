
import random


class Board():

    def __init__(self, width=6, height=53):
        self.width = width
        self.height = height
        self.mutateRate = 5
        self.board = [[0] * self.width for i in range(self.height)]
        self.allChars = []
        self.populateBoard()

    def populateBoard(self):
        japaneseChars = ['よ', 'か', 'と', 'し', 'っ', 'ん', 'ら', 'ひ', 'の', 'て',
                         'ち', 'け', 'か', 'お', 'え', 'ら', 'さ', 'う', 'い', 'イ',
                         'ウ', 'エ', 'カ', 'ケ', 'コ', 'シ', 'セ', 'チ', 'テ', 'ト',
                         'ヒ', 'フ', 'ホ', 'リ', 'ル', 'ロ', 'ラ', 'ヤ', 'ケ', 'ス',
                         'ソ', 'ハ', 'ナ', 'ム', 'ヘ', 'ワ', 'ヨ', 'ミ', 'タ', 'ニ']

        latinChars = ['A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ', 'J ',
                      'K ', 'L ', 'M ', 'N ', 'O ', 'P ', 'Q ', 'R ', 'S ', 'T ',
                      'U ', 'V ', 'W ', 'X ', 'Y ', 'Z ', 'a ', 'b ', 'c ', 'd ', 
                      'e ', 'f ', 'g ', 'h ', 'i ', 'j ', 'k ', 'l ', 'm ', 'n ', 
                      'o ', 'p ', 'q ', 'r ', 's ', 't ', 'u ', 'v ', 'w ', 'x ', 
                      'y ', 'z ']

        cryillicChars = ['Я ', 'Б ', 'Ж ', 'Ь ', 'Ф ', 'Й ', 'Л ', 'Д ']

        numberChars = ['0 ', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ']

        symbolChars = ['| ', '< ', '> ', '^ ', '& ', '@ ', '# ', '% ', '- ', '* ',
                       '? ', '= ', ': ', '; ']

        allChars = []

        
#        for char in japaneseChars:
#            allChars.append(char)
 
        for char in latinChars:
            allChars.append(char)
 
#        for char in cryillicChars:
#            allChars.append(char)
        

        for char in numberChars:
            allChars.append(char)
 
        for char in symbolChars:
            allChars.append(char)

        # create board

        screen = []
        for i in range(self.height):
            line = []

            while (len(line) < self.width): 
                currChar = allChars[random.randint(0, len(allChars) - 1)]
 
                if (len(line) == 0):
                    line.append(currChar)
 
                elif (line[-1] != currChar):
                    line.append(currChar)

            screen.append(line)

        self.allChars = allChars
        self.board = screen


    def mutate(self):
        # alter portions of the board
        for y in range(self.height):
            for x in range(self.width):
                change = random.randint(1, self.mutateRate)

                if (change == 1):
                    index = random.randint(1, len(self.allChars) - 1)
                    char = self.allChars[index]    
                    self.board[y][x] = char



