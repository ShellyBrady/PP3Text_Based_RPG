# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Opening intro and input name
print("""Welcome to Your Next Adventure!\n
Every decision you make along the way will determine how your story goes.\n""")
print()
name = input("What shall I call you?\n")

# Greeting and first choice
print("\nWell hello! Nice to meet you, " + name)
print("""\nGood news! Its time for your monthly guilt-induced jog.\n
Put on your barely worn runners and head for the door.\n
Are you ready to go?\n""")

# Action taken depending on input
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
        print("\nWhen your muscles burn, you stop to catch your breath.")
        print("\nJust then, you hear a rustling from the trees nearby.")
        print("\nYour heart pounds as you see a bear lumbering towards you!")
        break
    if choice2 == 'right':
        print("\nRight you are! Keep a steady pace.\n")
        print("\nAt the end of the sleepy street you reach the main road.\n")
        print("Cars whizz past as you jog on to the hard shoulder.\n")
        print("\nJust then, a white van pulls quickly up in front of you.")
        break
    else:
        choice2 = input("Choose to go 'left' or 'right':")

# Choice 3
    if choice2 == 'left':
        print("\nRun away or stand still?:\n")
        choice3 = input("run" or "stand")
    if choice2 == 'right':
        print("\nJog on or talk to the driver?\n")
        choice3 = input("Type 'jog' or 'talk' /n")
    else:
        input("Type 'jog' or 'talk':")

