#Taking Stones Game - MN404 Christian Milicevic

#Libaries/Vars
import random
 
#Game Intro Sequence Function
def GameIntro():
    global r_total_stones
    r_total_stones = random.randint(30, 50)

    print("\nWelcome to the game of taking of stones!")
    print("#############################################################################")
    print("The game goal is to take the last stone to be the winner")
    print("You can take between 1-3 stones per turn")
    print("The game will go in the rotational order of Player1, then Player2 then the computer AI")
    print("Player1 will pick the amount of stones in the game which is in the range of [30-50]")

    print("The game is a 3 players game consitiing of 2 human players and 1 computer AI")
    print("#############################################################################\n")
    print("Are you ready to play?")
    
    #User1, User2 and ComputerAI string input and captalization condtions
    user1 = input("Please enter in your username Player 1!: ");
    global user1_Id 
    user1_Id = input("Please enter in Player1 MIT Id: ");
    print("\n------------------------------------------")
    print("Welcome Player1:", user1.lower().capitalize(), "with the MIT Id:", user1_Id, "to game of stones")
    print("------------------------------------------\n")

    user2 = input("Please enter in your username Player 2!: ");
    global user2_Id
    user2_Id = input("Please enter in Player2 MIT Id: ");
    print("\n------------------------------------------")
    print("Welcome Player2:", user2.lower().capitalize(), "with the MIT Id:", user2_Id, "to game of stones")
    print("------------------------------------------\n")

    user3_AI = input("Please give the Computer a username: ")
    print("\n------------------------------------------")
    print("Welcome Computer:", user3_AI.lower().capitalize(), "to game of stones")
    print("This is an AI computer that will take it's turn after Player2")
    print("------------------------------------------\n")

    userReady = ""
    while userReady != "ready":
        userReady = input("If you are ready to play type, ready: ")
        if userReady == "ready": PlayGame()
        else: print("that is not the correct input please try again!\n")

#Game intro is over, set stone and play game function
def PlayGame():
    print("\n------------------------------------------")
    print("The number of stones in this game has been set to", r_total_stones)
    print("------------------------------------------\n")
    Player1() #GoTo Player1 Function

def Player1():
    global r_total_stones
    global user1_Id 
    user = 0
    while user != 1 or user != 2 or user != 3:
          print("\nPLAYER1 TURN")
          print("Player1: Remove [1-3] stones from the total of ", r_total_stones, "stones")
          user = input("Amount of stones to remove: ")
          if user.isdigit():
              if int(user) == 1 or int(user) == 2 or int(user) == 3:
                  r_total_stones = r_total_stones - int(user)
                  break;
          else: print("Invalid entry please try again!")
      #check for win con
    if r_total_stones <= 0:
        print("\nPlayer1 has won the game, has he followinig MIT ID:!", user1_Id)
        PlayAgain() #PlayAgain Condition
    else: Player2()

def Player2():
    global r_total_stones
    global user2_Id 
    user = 0
    while user != 1 or user != 2 or user != 3:
          print("\nPLAYER2 TURN")
          print("Player2: Remove [1-3] stones from the total of ", r_total_stones, "stones")
          user = input("Amount of stones to remove: ")
          if user.isdigit():
              if int(user) == 1 or int(user) == 2 or int(user) == 3:
                  r_total_stones = r_total_stones - int(user)
                  break;
          else: print("Invalid entry please try again!")
      #check for win con
    if r_total_stones <= 0:
        print("\nPlayer2 has won the game, has he followinig MIT ID:!", user2_Id)
        PlayAgain() #PlayAgain Condition
    else: Computer_AI()

#AI Function
def Computer_AI():
    global r_total_stones
    print("\nCOMPUTER_AI TURN")
    print("Computer_AI: Remove [1-3] stones from the total of ", r_total_stones, "stones")

    #AI Logic Here
    stones_to_take = random.randint(1, 3)
    r_total_stones = r_total_stones - stones_to_take 
    print("Computer_AI has removed", stones_to_take, "from the pile")

    #Win Con
    if r_total_stones <= 0:
        print("\nComputerAI has won the game!")
        PlayAgain() #PlayAgain Condition
    else: Player1()
        
#PlayAgain Function
def PlayAgain():
    user = ""
    while user.lower() != "y" or user != "yes":
        user = input("\nPlease enter in y or yes to play again: ")
        if  user == "y" or user == "Y" or user == "yes" or user == "YES": GameIntro()
        else: print("Not a valid entry, please try again!")
#Main
GameIntro()
