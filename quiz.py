import os

class blueprint:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

general_prompts, general_answers = [
	"5 * 5:\n\na) 25\nb) 10\nc) 5",
	"100 * 5:\n\na) 1000\nb) 50\nc) 500",
	"2 * 2:\n\na) 4\nb) 2\nc) 8",
	"(86 * 5)*0:\n\na) 1\nb) 430\nc) 0",
	"1 + 1:\n\na) 1\nb) 2\nc) 3"
],[
	'a',
	'c',
	'a',
	'c',
	'b'
]

general_questions = []
for i in range(len(general_prompts)):
	general_questions.append(blueprint(general_prompts[i], general_answers[i]))

TF_prompts, TF_answers = [
	"Earth is flat.\n\nTrue or False?",
	"Covid is fake.\n\nTrue or False?",
	"Tesla is motor company.\n\nTrue or False?",
	"Bitcoin is an cryptocurrency.\n\nTrue or False?",
	"Obama is dead.\n\nTrue or False?"
],[
	'false',
	'false',
	'true',
	'true',
	'false'
]

TF_questions = []
for i in range(len(TF_prompts)):
	TF_questions.append(blueprint(TF_prompts[i], TF_answers[i]))

def clear(): 
	os.system('cls' if os.name == 'nt' else 'clear')

def general_game(general_questions):
	score = 0
	questions_count = len(general_questions)
	for question in general_questions:
		guess = ''
		while guess != 'a' and guess != 'b' and guess != 'c':
			play_screen(question.prompt)
			guess = input("enter: ").lower()
		print()
		if guess.lower() == question.answer:
			score += 1
	win_screen(score, questions_count)

def game_true_false(TF_questions):
	score = 0
	questions_count = len(TF_questions)
	for question in TF_questions:
		play_screen(question.prompt)
		guess = input("Enter: ")
		print()
		if guess.lower() == question.answer:
			score += 1
	win_screen(score, questions_count)

def main_menu():
	print("+-----------------------+")
	print("| WELCOME TO QUIZ GAME! |")
	print("+-----------------------+")
	print("| DO YOU WANT TO PLAY ? |")
	print("|                       |")
	print("|      YES  or  NO      |")
	print("+-----------------------+")

def select_game():
	print("+-----------------------+")
	print("|       GAME MODES      |")
	print("+-----------------------+")
	print("| 1. General Quiz       |")
	print("| 2. True or False Quiz |")
	print("|                       |")
	print("| 0. Quit               |")
	print("+-----------------------+")

def end_screen():
	print("+----------------------------------+")
	print("|       THANK YOU FOR PLAYING      |")
	print("+----------------------------------+")

def win_screen(score, count):
	print("+-------------------------------------------------+")
	print("| You guessed {} out of {} general_questions, {}% |".format(score, count, (score/count)*100))
	print("+-------------------------------------------------+")

def play_screen(question):
	print("+----------------------+")
	print("{}".format(question))
	print("+----------------------+")

clear()
while True:
	main_menu()
	play_input = input("Enter: ")
	if play_input.lower() == 'yes':
		clear()
		select_game()
		gamemode_input = input("Enter: ")
		if gamemode_input == '1':
			clear()
			general_game(general_questions)
		elif gamemode_input == '2':
			clear()
			game_true_false(TF_questions)
		elif gamemode_input == '0':
			clear()
			end_screen()
			break
	else:
		end_screen()
		break