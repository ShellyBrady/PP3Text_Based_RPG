# Import sleep from time to add delays between strings
import time
import sys


# 'Play again' question to be posed when game is ended
def play_again():
    repeat = ['play', 'quit']
    repeat = input("\nType 'play' to play again or 'quit' to give up: ")
    if repeat == 'play':
        choice1_result()
        my_game()
    if repeat == 'quit':
        print('***********Thank you for playing. Goodbye!***********')
        sys.exit()
    else:
        repeat = input("Type 'play' to play again or 'quit' to give up: ")


# Game-over function
def game_over():
    print("\nIf only you had made different choices today!")
    time.sleep(1)
    print("\n*******************GAME OVER*******************\n")
    time.sleep(1)
    play_again()


# Winning is getting home safe in one piece!
def you_win():
    time.sleep(1)
    print("\nYou run for home faster than you have ever run before!")
    time.sleep(1)
    print("You fling open the door and kick your runners off with relief.")
    time.sleep(1)
    print("Congratulate yourself for making it through another monthly jog.\n")
    time.sleep(1)
    print("\n******************YOU SURVIVED******************\n")
    time.sleep(1)
    play_again()


# Opening intro and input name
def intro():
    print("*********Welcome to Your Next Adventure!*********\n")
    time.sleep(1)
    print("Every decision you make will determine how your story goes.\n")
    time.sleep(2)
    name1 = input("What shall I call you? ")

# Greeting and first question
    print("Hello, " + name1.capitalize() + "! Nice to meet you.")
    time.sleep(2)
    print("\nGood news! Its time for a monthly guilt-induced run!")
    time.sleep(1)


# choice1
def choice1_result():
    choice1 = ['no', 'yes']
    print("\nPut on your barely worn runners and head for the door.\n")
    print("****************Are you ready to go?****************")

    # Action taken depending on input for choice1
    while True:
        if choice1 == 'yes':
            print("\nBetter get going before it starts to get dark!\n")
            time.sleep(1)
            print("\nHead for the quiet county road at the end of your drive.")
            time.sleep(2)
            print("\nLeft brings you to a hilly road surrounded by fields.")
            time.sleep(1)
            print("Right brings you from quiet village to the busy main road.")
            time.sleep(2)
            break
        if choice1 == 'no':
            print("\n*****Maybe tomorrow. It looks like it might rain.*****\n")
            time.sleep(1)
            game_over()
        else:
            choice1 = input("Type 'no' or type 'yes': ")


def my_game():

    # Choice lists
    choice2 = ['left', 'right']
    choice3 = ['run', 'stand', 'jog', 'talk']

    # Action dependant on Choice 2 input
    choice2 = input("Choose to go 'left' or 'right': ")
    while True:

        if choice2 == 'left':
            print("\nLess cars but more hills-your legs will hurt tomorrow!\n")
            time.sleep(1)
            print("\nWhen your muscles burn, you stop to catch your breath.")
            time.sleep(1)
            print("\nJust then, you hear a rustling from the trees nearby.")
            time.sleep(1)
            print("....")
            time.sleep(1)
            print("\nYour heart pounds-you see a bear lumbering towards you!")
            time.sleep(1)
            choice3 = input("Type 'run' to run away, or 'stand' to stand: ")
            if choice3 == 'run':
                print("You turn and run for home but the hills slow you down.")
                time.sleep(2)
                print("The bear gains on you with surprising speed!")
                time.sleep(1)
                print("You become the bear's dinner")
                time.sleep(1)
                game_over()
            if choice3 == 'stand':
                print("Every inch of your being screams at you to run.")
                time.sleep(1)
                print("You remember from somewhere that you need to be still.")
                time.sleep(1)
                print('....')
                print("You can feel the bear's breath on your neck!")
                time.sleep(2)
                print("You think it's ended for you but the bear ambles off!")
                time.sleep(1)
                you_win()
            else:
                choice3 = input("Type 'run' to run away, or 'stand' to stand:")
        if choice2 == 'right':
            print("\nRight you are! Keep a steady pace.\n")
            time.sleep(1)
            print("\nAt the end of the sleepy street you reach the main road.")
            print("\nCars whizz past as you jog on to the hard shoulder.\n")
            time.sleep(1)
            print("Suddenly, a white van screeches to a halt in front of you!")
            time.sleep(1)
            choice3 = input("Type 'jog' to go on or 'talk' to talk to him: ")
            if choice3 == 'jog':
                print("You watch too much true crime to get close to the van!")
                time.sleep(1)
                print("The driver door swings open as you jog past.")
                time.sleep(1)
                print("A man with a crazed look in his eyes jumps out!")
                time.sleep(1)
                you_win()
            if choice3 == 'talk':
                print("You approach the driver's door just as it flings open!")
                time.sleep(1)
                print("You jump back but the driver is too fast for you.")
                time.sleep(1)
                print("He pulls you into the van with sudden speed!")
                time.sleep(2)
                print("The homicidal maniac takes you to his murder-house.")
                time.sleep(1)
                game_over()
            else:
                choice3 = input("Type 'jog' to go on or 'talk' to talk: ")
        else:
            choice2 = input("Choose to go 'left' or 'right': ")


intro()

choice1_result()

my_game()
