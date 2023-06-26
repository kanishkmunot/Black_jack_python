import random
print("Welcome to BlackJack!! \n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user1= []
comp= []
x = (random.choice(cards)) 
y = (random.choice(cards)) 
z = (random.choice(cards)) 
comp.append(z)
user1.append(x)
user1.append(y)
print("Your cards are: ",user1)
print("Computer's first card", comp)

sum_not_twenty_one = True

while(sum_not_twenty_one):
  z = input("Press 'y' for another cards OR 'n' to pass:\n")
  z.lower()
  if(z=='y'):
    a = (random.choice(cards))
    user1.append(a)
    if(sum(user1)<21):
     print("\nYour cards",user1)
     print("The sum of your cards is: ", sum(user1))
     print("Computer's first card", comp)
    else:
      print("\nThe sum of your cards is: ", sum(user1))
      print("Your cards = ",user1)
      print("You Lose, better luck next time")
      sum_not_twenty_one=False
      
  elif(z =='n'):
    b = (random.choice(cards))
    comp.append(b)
    print("\nComputer's card",comp)
    if (sum(comp)>21):
      print("\nYou Win!!")
      sum_not_twenty_one=False
      
  else:
    print("invalid input")
  
  




