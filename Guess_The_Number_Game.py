import random
computer=random.randrange(1,100)
#randrange is use to define a range for computer to choose a random number 
user=int(input("Enter your number : \n"))


#Comperision

if user>computer:
    print("computer : ",computer)
    print("Your Guess number is too High")

elif computer>user:
    print("computer number : " , computer )
    print("Your Guess number is too Low ")

else:
    print ("Computer number : " ,computer)
    print("Your Guess number is equal ! You win !!")


#we can make this game more difficult ! by increasing range 