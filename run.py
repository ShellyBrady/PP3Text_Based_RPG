# Write your code to expect a terminal of 80 characters wide and 24 rows high

print("""Welcome to Your Next Adventure!\n
Every decision you make along the way will determine how your story goes.\n""")
print()
name = input("What shall I call you?\n")

print("\nWell hello! Nice to meet you, " + name)
print("""\nGood news! Its time for your monthly guilt-induced jog.\n
Put on your barely worn runners and head for the door.\n
Are you ready to go?\n""")

choice1 = input("Type 'no' or type 'yes':")

while True:

    if choice1 == 'yes':
        print("\nBetter get going before it starts to get dark!\n")
        break
    if choice1 == 'no':
        print("\nMaybe tomorrow. It looks like it might rain.\n")
        break
    else:
        choice1 = input("Type 'no' or type 'yes':")

print("Head for the quiet county road at the end of your drive.\n")
print("Left will bring you through a hilly narrow road surrounded by fields\n")
print("Right brings you through a quiet village to the busy main road\n")

choice2 = input("Choose to go 'left' or 'right':")

while True:

    if choice2 == 'left':
        print("\nLess cars but more hills..your legs will hurt tomorrow!\n")
        break
    if choice2 == 'right':
        print("\nRight you are! Keep a steady pace\n")
        break
    else:
        choice2 = input("Choose to go 'left' or 'right':")

