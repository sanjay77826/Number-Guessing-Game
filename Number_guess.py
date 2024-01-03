import math
import random

lower=int(input("Enter the Lower Number: "))
upper=int(input("Enter the  Upper  Number: "))

r=random.randint(lower,upper)
print("\n\t You have only",round(math.log(upper-lower+1)),"Chances to guess the integer!\n")

count=0


while count<math.log(upper-lower+1):
    count+=1
    guess=int(input("Guess a Number: "))
    if r==guess:
        print(f"Congratulations you did it in {count}, try")
        break
    elif r<guess:
      print("You Guessed Too high! ")
    elif r >guess:
      print("You Guessed Too small! ")

if count>=math.log(upper-lower+1):
    print("\n The Number is  %d"% r)
    print("\t Better Luck Next Time!")
