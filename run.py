# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Import sleep from time to add delays between strings
import time

# Choice lists
choice1 = ['no', 'yes']
choice2 = ['left', 'right']
choice3 = ['run', 'stand', 'jog', 'talk']

# Opening intro and input name
print("****Welcome to Your Next Adventure!****\n")
time.sleep(1)
print("Every decision you make will determine how your story goes.\n")
time.sleep(2)
name1 = input("What shall I call you?\n")

# Greeting and first question
print("\nWell hello, " + name1 + "! Nice to meet you.")
time.sleep(2)
print("\nGood news, " + name1 + "! Time for your monthly guilt-induced run!")
print("\nPut on your barely worn runners and head for the door.\n")
print("Are you ready to go?")
time.sleep(1)

# choice1
choice1 = input("Type 'no' or type 'yes':")
# Action taken depending on input for choice1
while True:

    if choice1 == 'yes':
        print("\nBetter get going before it starts to get dark!\n")
        print("\nHead for the quiet county road at the end of your drive.\n")
        print("Left brings you up a hilly narrow road surrounded by fields\n")
        print("Right brings you to a quiet village to the busy main road\n")
        break
    if choice1 == 'no':
        print("\nMaybe tomorrow. It looks like it might rain.\n")
        time.sleep(1)
        print("\nGame Over!")
        quit()
        break
    else:
        print(input("Type 'no' or type 'yes':"))

# Choice 2
choice2 = input("Choose to go 'left' or 'right':")

# Action dependant on Choice 2 input
while True:

    if choice2 == 'left':
        print("\nLess cars but more hills..your legs will hurt tomorrow!\n")
        time.sleep(1)
        print("\nWhen your muscles burn, you stop to catch your breath.")
        time.sleep(1)
        print("\nJust then, you hear a rustling from the trees nearby.")
        print("\nYour heart pounds as you see a bear lumbering towards you!")
        time.sleep(1)
        print(input("Type 'run' to run away, or 'stand' to stand still:"))

    if choice2 == 'right':
        print("\nRight you are! Keep a steady pace.\n")
        time.sleep(1)
        print("\nAt the end of the sleepy street you reach the main road.\n")
        print("Cars whizz past as you jog on to the hard shoulder.\n")
        time.sleep(1)
        print("\nSuddenly, a white van screeches to a halt in front of you\n")
        time.sleep(1)
        choice3 = input("Type 'jog' to go on or 'talk' to hear what he wants:")
    else:
        print(input("Choose to go 'left' or 'right':"))


# game over function
def game_over():

    print("If only you had made different choices today!")
    print("\n*********GAME OVER********\n")
    quit()


# Winning is getting home safe in one piece!

def you_win():

    print("/nYou run for home faster than you have ever run before")
    print("You fling open the door and kick your runners off with relief.")
    print("Congratulate yourself for making it through another monthly jog.\n")
    print("/n********YOU SURVIVED********/n")


# choice3 input consequences
while True:

    if choice3 == 'run':
        print("You turn and run for home but the hills slow you down")
        print("The bear gains on you with surprising speed!")
        print("You become the bear's dinner")
        game_over()
        break

    if choice3 == 'stay':
        print("Every inch of your being screams at you to run.")
        print("You remember from somewhere that you need to be still.")
        print("You can feel the bear's breath on your neck!")
        print("Just as you think it's curtains for you, the bear ambles away.")
        you_win()
        break

    if choice3 == 'jog':
        print("You watch way too much true crime to get close to that van!")
        print("The driver door swings open as you jog past.")
        print("A man with a crazed look in his eyes jumps out!")
        you_win()
        break

    if choice3 == 'talk':
        print("You approach the driver's door just as he flings it open!")
        print("You jump back but the driver is too fast for you.")
        print("He grabs you and pulls you into the van with shocking speed!")
        print("The homicidal maniac takes you back to his murder-house.")
        game_over()
        break

    else:
        print(choice3)
