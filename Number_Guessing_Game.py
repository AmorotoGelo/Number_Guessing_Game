import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
     top_of_range = int(top_of_range)

     if top_of_range <= 0:
          print('Please type a number larger than zero next time. ')
          quit()
else:
     print('Please type a number next time. ')
     quit() 

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
     guesses += 1
     user_guesses = input("Make a guess: ")