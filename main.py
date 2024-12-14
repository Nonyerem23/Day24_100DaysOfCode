import random
print("InfiniDice")
print()
sides = int(input("How many sides?: "))
playGame = "yes"
print()
def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
  rollDice(sides)
  playGame = input("Roll again? ")
  if playGame == "yes" or playGame == "Yes":
    continue
  else:
      print("Thanks for playing!")
      break
  
