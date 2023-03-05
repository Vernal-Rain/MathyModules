print("Welcome to Tic-Tac-Toe!\n")
board = [["-"] *3 for i in range(3)]
def print_board():
    print("  A B C")
    for i in range(3):
        print(i+1, " ".join(board[i]))
def won():
    return 


win = False
while not win:
    print_board()
    print("Select a spot...")
    row = int(input("Enter row number: ")) - 1
    col = ord(input("Enter column letter: ")) - 65
    
    
    
    
