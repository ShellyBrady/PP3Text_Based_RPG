# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
def choice1():
    import time
    print("""Welcome to Your Next Adventure!
        Every decision you make along the 
        way will determine how your story goes.

        Its time for your monthly guilt-induced jog.
        You put on your barely worn runners and head for the door.
        You pause with your hand on the door knob.
        Type stay or type go
        """)
    
    c1 = input()
    time.sleep(2)
    ans = 'one'
    while (ans == 'one'):
        if (c1() == 'stay'):
            print("\nTomorrow, you can do it tomorrow.")    
            ans = "correct"
            choice2()
        else:
            print("Type either stay or go") 
            c1= input()

