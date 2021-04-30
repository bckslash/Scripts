import random
import os

game_list = ["kamen", "papier", "noznice"]
gameloop = True
player_score, bot_score = 0, 0

def clear(): 
	os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("============= Kamen, Papier, Noznice =============\n")

while gameloop:

	if player_score == 3:
		print(f"============= Vyhral si {player_score}:{bot_score} =============")

		Yn = input("Restart ? [Y/n]")
		if Yn.lower() == "y":
			player_score, bot_score = 0, 0
			clear()
			continue

		if Yn.lower() == "n":
			clear()
			print("Thank you for playing")
			break

	if bot_score == 3:
		print(f"============= Prehral si {player_score}:{bot_score} =============")

		Yn = input("Restart ? [Y/n]")
		if Yn.lower() == "y":
			player_score, bot_score = 0, 0
			clear()
			continue

		if Yn.lower() == "n":
			clear()
			print("Thank you for playing")
			break

	print(f"Hrac: {player_score} Bot: {bot_score}\n")

	game = random.choice(game_list)
	guess = input("Hraj!: ")

	if guess.lower() == "kamen" and game == "kamen":
		clear()
		print(f"{guess} vs {game}, REMIZA\n")

	elif guess.lower() == "kamen" and game == "papier":
		clear()
		bot_score += 1
		print(f"{guess} vs {game}, PREHRA\n")

	elif guess.lower() == "kamen" and game == "noznice":
		clear()
		player_score += 1
		print(f"{guess} vs {game}, VYHRA\n")

	elif guess.lower() == "papier" and game == "papier":
		clear()
		print(f"{guess} vs {game}, REMIZA\n")

	elif guess.lower() == "papier" and game == "kamen":
		clear()
		player_score += 1
		print(f"{guess} vs {game}, VYHRA\n")

	elif guess.lower() == "papier" and game == "noznice":
		clear()
		bot_score += 1
		print(f"{guess} vs {game}, PREHRA\n")

	elif guess.lower() == "noznice" and game == "noznice":
		clear()
		print(f"{guess} vs {game}, REMIZA\n")

	elif guess.lower() == "noznice" and game == "kamen":
		clear()
		bot_score += 1
		print(f"{guess} vs {game}, PREHRA\nHrac: {player_score} Bot: {bot_score}\n")

	elif guess.lower() == "noznice" and game == "papier":
		clear()
		player_score += 1
		print(f"{guess} vs {game}, VYHRA\nHrac: {player_score} Bot: {bot_score}\n")

	elif guess.lower() == "exit":
		clear()
		break

	else:
		clear()
		print("Wrong input!\n")
		continue