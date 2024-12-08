"""
1) Display the grid
2) Ask an index from the user
3)Check if the input is valid
    WHILE the input is invalid, ask again
4) Update the grid
5) Check if the game is won
    If game is won, break
  """
import check_py as XO


def isEmpty(matrix, index):
    if matrix[index // 3][index % 3] == '-':
        return True
    else:
        return False
    
def display_game(matrix):
    for list in matrix:
        print(list)

def determine_turn(sign):
    if sign == 'X':
        return 'O'
    else:
        return 'X'

turn = "X"
matrix = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
draw = True

for index in range(9):
    display_game(matrix)
    choice = int(input("Choose the index Of where you want to put your sign"))
    while not isEmpty(matrix, choice) :
        print(str(choice)+" is already taken, choose another :")
        choice = int(input("Choose the index of where you want to put your sign"))
    matrix[choice // 3][choice % 3] = turn
    if XO.check_game(matrix, turn) != 'N':
        print("Game won by "+turn)
        display_game(matrix)
        draw = False
        break
    turn = determine_turn(turn)
    print("\n")
    
if draw:
    display_game(matrix)
    print("It's a draw!")


