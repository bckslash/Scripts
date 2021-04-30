import random
import string
import os

with open('wordlist.txt', 'r') as f:
	words = f.readlines()
word = random.choice(words)[:-1]

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

errors = 8
guesses = []
done = False
alphabet = string.ascii_lowercase

clear()
print(f'''Welcome to the game, Hangman!
I am thinking of a word that is {len(word)} letters long.
--------------''')

while not done:

	print(f"You have {errors} left")
	print(f"Available letters: {alphabet}")
	guess = input("Please guess a letter: ")
	alphabet = alphabet.replace(guess, '')

	if guess.lower() == word:
		done = True
		break

	guesses.append(guess.lower())
	if guess.lower() not in word:
		errors -= 1
	if errors == 0:
		break

	if guess in word:
		print("Good guess: ", end='')
	else:
		print("Oops! That letter is not in my word: ", end='')
	for letter in word:
		if letter.lower() in guesses:
			print(letter, end=" ")
		else:
			print("_", end=" ")
	print("\n--------------")

	done = True

	for letter in word:
		if letter.lower() not in guesses:
			done = False

if done:
	print("Congratulations, you won!")
elif done == False:
	print(f"Sorry, you ran out of guesses. The word was {word}.")
elif done == None:
	print(f"Sorry, bad guess. The word was {word}.")
