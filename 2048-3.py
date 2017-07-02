import random
import copy
import os
import tkinter
from tkinter import messagebox


class MyMatrix:
    def __init__(self):
        # Initialization of MyMatrix. GameField as list. ScoreStep - as int. GameOver as bool

        # self.GameField = [[1, 2, 2, 3], [5, 40, 4, 3], [3, 3, 3, 0], [0, 0, 0, 0]]
        # self.GameField = [[2, 0, 0, 4],
        #                   [2, 0, 0, 0],
        #                   [0, 0, 0, 2],
        #                   [4, 0, 0, 2]]'''
        self.GameField = [[0 for _ in range(4)] for _ in range(4)]  # [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.ScoreStep = 0
        self.add_values(2)
        self.add_values(4)
        self.GameOver = False

    def print_field(self): # Only for console and debug
        # Print in console our GameField 4x4 with tab between them. And the current Score
        # os.system('cls' if os.name == 'nt' else 'clear') #not working =(
        print('\n' * 30)
        for row in self.GameField:
            print('\t'.join([str(elem) for elem in row]))
        print()
        print('Score = ', self.ScoreStep)

    def add_values(self, *a):
        # Add 2 or 4(rarely) or *a in the empty fields after every round. *a needs for initialization
        if a:
            a = int(a[0])
            self.ScoreStep -= 1 # -1 for initialization
        else:
            a = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4]) #(with chance of 1 in 10)
        coordinates = self.find_free_space  # find coordinates of 0 values via @property find_free_space
        if coordinates: # if there is at least one 0. Otherwise call is_it_end() to find out that the game is over
            random.shuffle(coordinates) # for more randomization
            one_coordinate = random.choice(coordinates)
            self.GameField[one_coordinate[0]][one_coordinate[1]] = a
            self.ScoreStep += 1
            if len(coordinates) == 1: # there is no 0 anymore,is it over?
                self.is_it_end()
        else:                         # another condition of game over. coordinates is None
            self.is_it_end()

    @property
    def find_free_space(self):
        # Make a list of coordinates of 0 values in matrix
        free_space = []
        for i in range(len(self.GameField)):
            for j in range(len(self.GameField[i])):
                if self.GameField[i][j] == 0:
                    free_space.append([i, j])
        if free_space:
            return free_space
        else:
            #self.stop_game()
            # bad idea
            pass

    #def stop_game(self):
        # Stop current game and exit()
     #   self.print_field()
     #   print('The end \nScore = ', self.ScoreStep)
        #exit() 

    def is_it_end(self):  # FIXME Have to understand how to find out the game is finished.
        print('is it end?')
        for i in range(4): # check columns
            for j in range(3):
                if self.GameField[i][j] == self.GameField[i][j+1]:
                    print("Это не конец!")
                    return 0

        for i in range(3): # check rows
            for j in range(4):
                if self.GameField[i][j] == self.GameField[i+1][j]:
                    print("Это не конец!")
                    return 0

        print('Это конец')
        self.GameOver = True


    # Moving/Actions below
    def move_up(self):
        print('move_up')
        old_game_field = copy.deepcopy(self.GameField)
        for t in range(3):  # Do it three times to be sure that all the values are moved and after that sum adjacent
            for i in range(3):  # 3 because we don't have to work with last string
                for j in range(4):
                    if self.GameField[i][j] == 0:  # If it's 0 - move all elements up and set 0 to the last one
                        for k in range(i, 3):
                            self.GameField[k][j] = self.GameField[k + 1][j]
                            self.GameField[k + 1][j] = 0
                        self.GameField[3][j] = 0
                    elif self.GameField[i][j] == self.GameField[i + 1][j] and t == 2:  # sum of adjacent and move others
                        self.GameField[i][j] = self.GameField[i][j] + self.GameField[i + 1][j]
                        for k in range(i + 1, 3):
                            self.GameField[k][j] = self.GameField[k + 1][j]
                            self.GameField[k + 1][j] = 0
        if self.GameField == old_game_field:
            print('Ничего не изменилось')
        else:
            print('что-то изменилось')
            self.add_values()

    def move_down(self):
        print('move_down')
        old_game_field = copy.deepcopy(self.GameField)
        for t in range(3):  # Do it three times to be sure that all the values are moved and after that sum adjacent
            for i in range(3, 0, -1):  # 3 because we don't have to work with last string
                for j in range(4):
                    if self.GameField[i][j] == 0:  # If it's 0 - move all elements up and set 0 to the last one
                        for k in range(i, 0, -1):  # FIXME
                            self.GameField[k][j] = self.GameField[k - 1][j]
                            self.GameField[k - 1][j] = 0
                        self.GameField[0][j] = 0
                    elif self.GameField[i][j] == self.GameField[i - 1][j] and t == 2:  # sum of adjacent and move others
                        self.GameField[i][j] = self.GameField[i][j] + self.GameField[i - 1][j]
                        for k in range(i - 1, 0, -1):  # FIXME
                            self.GameField[k][j] = self.GameField[k - 1][j]
                            self.GameField[k - 1][j] = 0
        if self.GameField == old_game_field:
            print('Ничего не изменилось')
        else:
            print('что-то изменилось')
            self.add_values()

    def move_left(self):
        print('move_left')
        old_game_field = copy.deepcopy(self.GameField)
        for t in range(3):
            for j in range(3):
                for i in range(4):
                    if self.GameField[i][j] == 0:
                        for k in range(j, 3):
                            self.GameField[i][k] = self.GameField[i][k + 1]
                            self.GameField[i][k + 1] = 0
                        self.GameField[i][3] = 0
                    elif (self.GameField[i][j] == self.GameField[i][j + 1] and t == 2):
                        self.GameField[i][j] = self.GameField[i][j] + self.GameField[i][j + 1]
                        for k in range(j + 1, 3):
                            self.GameField[i][k] = self.GameField[i][k + 1]
                            self.GameField[i][k + 1] = 0
        if self.GameField == old_game_field:
            print('Ничего не изменилось')
        else:
            print('что-то изменилось')
            self.add_values()

    def move_right(self):
        print('move_right')
        old_game_field = copy.deepcopy(self.GameField)
        for t in range(3):
            for j in range(3, 0, -1):
                for i in range(4):
                    if self.GameField[i][j] == 0:
                        for k in range(j, 0, -1):
                            self.GameField[i][k] = self.GameField[i][k - 1]
                            self.GameField[i][k - 1] = 0
                        self.GameField[i][0] = 0
                    elif (self.GameField[i][j] == self.GameField[i][j - 1] and t == 2):
                        self.GameField[i][j] = self.GameField[i][j] + self.GameField[i][j - 1]
                        for k in range(j - 1, 0, -1):
                            self.GameField[i][k] = self.GameField[i][k - 1]
                            self.GameField[i][k - 1] = 0
        if self.GameField == old_game_field:
            print('Ничего не изменилось')
        else:
            print('что-то изменилось')
            self.add_values()

class TestMatrix(MyMatrix):
    def __init__(self):
        # Initialization of MyMatrix. GameField as list. ScoreStep - as int. GameOver as bool
		
		
     #   self.GameField = [[0 for _ in range(4)] for _ in range(4)]  # [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        # self.GameField = [[1, 2, 2, 3], [5, 40, 4, 3], [3, 3, 3, 0], [0, 0, 0, 0]]
        self.GameField = [[2, 4, 8, 16], [32,64, 128, 256], [512, 1024, 2048, 2], [4, 0, 0, 2]]
        self.ScoreStep = 0
        self.add_values(2)
        self.add_values(4)
        self.GameOver = False

			
def Move_Up(event):
    Game.move_up()
    refreshconfig(Game.GameField)


def Move_Down(event):
    Game.move_down()
    refreshconfig(Game.GameField)


def Move_Left(event):
    Game.move_left()
    refreshconfig(Game.GameField)


def Move_Right(event):
    Game.move_right()
    refreshconfig(Game.GameField)


def refreshconfig(GameField): # reprint all the values using colour dictionary
    for i in range(4):
        for j in range(4):
            tbg = BG
            tfg = FG
            if GameField[i][j] in colour_dict:
                tbg = colour_dict[GameField[i][j]][0]
                tfg = colour_dict[GameField[i][j]][1]
            label[i][j].configure(text=GameField[i][j], bg=tbg, fg=tfg)
    LabelRight.configure(text='Score:  ' + str(Game.ScoreStep))
    if Game.GameOver == True:
        answer = messagebox.askyesno(title='Game Over', message='Игра закончена\n'+'Ваш счет: '+str(Game.ScoreStep)
                                     +'\n\nНачать заново?')
        print(answer)
        if answer:
            restart_game()
        else:
            rootwindow.destroy()


def restart_game():
    print('hi')
    Game.GameField = [[0 for _ in range(4)] for _ in range(4)]  # [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    Game.ScoreStep = 0
    Game.add_values(2)
    Game.add_values(4)
    Game.GameOver = 0
    refreshconfig(Game.GameField)


# Constants:
WIDTH = 7
HEIGHT = 4
BG = '#cea61a'
FG = 'white'
FONT = 'arial 25'

colour_dict = {0:   ['#cdc1b4', '#cdc1b4'],
               2:   ['#eee4da', '#776e65'],
               4:   ['#ede0c8', '#776e65'],
               8:   ['#f2b179', 'white'],
               16:  ['#f59563', 'white'],
               32:  ['#f67c5f', 'white'],
			   64:  ['#f65e3b', 'white'],
			   128: ['#edcf72', 'white'],
			   256: ['#edcc61', 'white'],
               512: ['#e9c13a', 'white'],
			   1024: ['#e4b81f', 'white'],
			   2048:['#cea61a','white']
			   }

Game = MyMatrix()
#Game = TestMatrix()

rootwindow = tkinter.Tk()
rootwindow.configure(bg='#bbada0')

frame1 = tkinter.Frame(rootwindow, bg='#bbada0') # Frame for GameField
frame2 = tkinter.Frame(rootwindow, bg='#bbada0', height=HEIGHT) # Frame for Score and Restart Button

frame1.grid(row=0, column=0, padx=5, pady=5)
frame2.grid(row=0, column=1, padx=5, pady=5, sticky='n')

label = [[0 for _ in range(4)] for _ in range(4)]
for i in range(4):
    for j in range(4):
        label[i][j] = tkinter.Label(frame1, text=Game.GameField[i][j], width=WIDTH, height=HEIGHT, bg=BG, fg=FG,
                                    font=FONT)

for i in range(4):
    for j in range(4):
        label[i][j].grid(row=i, column=j, padx=5, pady=5)

LabelRight = tkinter.Label(frame2, text='Score:  ' + str(Game.ScoreStep), width=WIDTH*2, height=HEIGHT,
                           bg='#eee4da', fg="black", font=FONT)
LabelRight.grid(row=0, column=0, padx=5, pady=5)

ButtonRestart = tkinter.Button(frame2, text='Новая игра', width=WIDTH*2, height=HEIGHT-2, bg='#f65e3b',
                               fg='black', font=FONT, command=restart_game)
ButtonRestart.grid(row=1, column=0, padx=5, pady=5, sticky='s')

refreshconfig(Game.GameField)

rootwindow.bind('<Up>', Move_Up)
rootwindow.bind('<Down>', Move_Down)
rootwindow.bind('<Right>', Move_Right)
rootwindow.bind('<Left>', Move_Left)

#rootwindow.rowconfigure(0, weight=0)
#rootwindow.rowconfigure(0, weight=0)

rootwindow.mainloop()

'''
TField = MyMatrix()
while True:
    print('-'*15)
    TField.print_field()
    input_choice = input()
    if input_choice == '8':
        TField.move_up()
    elif input_choice == '4':
        TField.move_left()
    elif input_choice == '5':
        TField.move_down()
    elif input_choice == '6':
        TField.move_right()
    else:
        TField.stop_game()
'''
