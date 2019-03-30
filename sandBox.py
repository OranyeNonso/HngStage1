import random
numGames = int(input("How many Games do you want to play: "))

for x in range(1, numGames+1):
     print("Game start!")
     mainNum = random.randint(10, 100)

     userGuess = 0

     while not userGuess == mainNum:

         userGuess = int(input("Guess a number: "))

         if userGuess > mainNum:
             print("Too High!")
         elif userGuess < mainNum:
             print("Too Low!")
         else:
            print("That's right")
