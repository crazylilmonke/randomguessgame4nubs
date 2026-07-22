import random
import sys
print("Choose number between 0 and 9! Guessing Game Begins")
x = int(input("enter number:"))
if x>9:
    print("0 to 9 only please!")
    sys.exit()
elif x<0:
    print("0 to 9 only please!")
    sys.exit()
n = random.randrange(0,9)
print("My number is:",n)
if x == n:
    print("Our minds work similarly! We Both have Chosen",n)
else:
    print("oops different number! Try again.")
