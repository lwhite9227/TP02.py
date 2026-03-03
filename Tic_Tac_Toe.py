# 1. Create 3x3 Board

board = ["1","2","3",
         "4","5","6",
         "7","8","9"]

# Function to display board
def display_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


# 2. Ask User to Play First

# Keep asking until valid answer
while True:
    first = input("Do you want to play first? (y/n): ")
   
    if first == "y" or first == "Y":
       user_turn = True
       break
   
    elif first == "n" or first == "N":
       user_turn = False
       break
       
    else:
        print("Invalid input")
       
       
# 3. Choose X or O

# Keep asking until valid symbol
while True:
    symbol = input("Choose X or O: ")
   
    if symbol == "X" or symbol == "x":
       
       user_symbol = "X"
       computer_symbol = "O"
       break
   
    elif symbol == "O" or symbol == "o":
       
        user_symbol = "O"
        computer_symbol = "X"
        break
   
    else:
        print("Invalid input")
       
       
# 4. Start Game Loop

game_over = False

while game_over == False:
   
    # Display board
    display_board()
   
   
# User Turn

if user_turn == True:
   
    # Ask for position 1-9
    position = input("Choose position (1-9): ")
   
    # Convert to index
    position = int(position) - 1
   
    # Place symbol on board
    board[position] = user_symbol
   
   
     # TODO:
     # Check for winner
     # Check for draw

    user_turn = False
   
   
# Computer Turn

else:
   
    # Temporary computer move
    # (always chooses first open spot)
   
    for i in range(9):
       
        if board[i] != "X" and board[i] != "O":
           
            board[i] = computer_symbol
            break
       
    # TODO:
    # Check for winner
    # Check for draw

    user_turn = True
   
   
 # Temporary Stop Condition
 
 # This is here only for testing
 # Will be replaced later
 
stop = input("Continue? (y/n): ")
 
if stop == "n":
   
    game_over = True
   
print("Game ended")