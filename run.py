# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def game():
    print("""Welcome to Your Next Adventure!
        Every decision you make along the 
        way will determine how your story goes.
        """)

    print("""Its time for your monthly guilt-induced jog.
        You put on your barely worn runners and head for the door.
        You pause with your hand on the door knob.
        """)

    answer = input("Type 'stay' or type 'go':")
    if answer.lower == 'go':
        print("Better get going before it starts to get dark!")
        start = True  
    elif answer.lower == 'stay':
        print("Maybe tomorrow. It looks like it might rain.")
    else:
        print("Type only 'stay' or 'go':")

if start == True:
    print("You head for the quiet county road at the end of your drive.")   
    print("Left will bring you through a hilly narrow road surrounded only by fields")     
    print("Right brings you through a quiet village to the busy main road")
    choice=input("Choose to go 'left' or 'right':")

if choice == 'left':  
    choice1 = True
    print("Less cars but more hills..your legs will hurt tomorrow!")
elif choice == 'right':
    print("Right you are! Keep a steady pace")  
else:
    print("Type only 'left' or 'right':")      

    

      
    

