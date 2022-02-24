# program that prompts the user to guess a number
# And tells the user if the guess is too high or too low

# Author: Tosin Araba

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
  if guess < numberToGuess:
      print("too low")
  else: # I know it cant be equal or too low, so it must be too high
      print("too high")
guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)
