# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time

choice1 = ['no', 'yes']
choice2 = ['left', 'right']
choice3 = ['run', 'stand', 'jog', 'talk']

# Opening intro and input name
print("Welcome to Your Next Adventure!\n")
time.sleep(1)
print("Every decision you make will determine how your story goes.\n")
time.sleep(2)
name1 = input("What shall I call you?\n")

# Greeting and first choice
print("\nWell hello, " + name1 + "! Nice to meet you.")
time.sleep(2)
print("\nGood news, " + name1 + "! Time for your monthly guilt-induced run!")
print("\nPut on your barely worn runners and head for the door.\n")
print("Are you ready to go?")
time.sleep(1)

# Action taken depending on input for choice1
choice1 = input("Type 'no' or type 'yes':")

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
        choice1 = input("Type 'no' or type 'yes':")

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
        choice3 = input("Type 'run' to run away, or 'stand' to stand still:")

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
        choice2 = input("Choose to go 'left' or 'right':")

