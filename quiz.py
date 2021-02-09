class blueprint:
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer

prompts, answers = [
	"5 * 5:\na) 25\nb) 10\nc) 5\n",
	"100 * 5:\na) 1000\nb) 50\nc) 500\n",
	"2 * 2:\na) 4\nb) 2\nc) 8\n",
	"(86 * 5)*0:\na) 1\nb) 430\nc) 0\n",
	"1 + 1:\na) 1\nb) 2\nc) 3\n",
],[
	'a',
	'c',
	'a',
	'c',
	'b'
]

questions = []
for i in range(len(prompts)):
	questions.append(blueprint(prompts[i], answers[i]))

def game(questions):
	score = 0
	questions_count = len(questions)
	for question in questions:
		guess = input(question.prompt)
		print()
		if guess == question.answer:
			score += 1
	print("You guessed {} out of {} questions, {}%".format(score, questions_count, (score/questions_count)*100))

game(questions)