import random

dice_size = int(input("How many sides: "))
rolls = int(input("How many dices: "))
all_dices = []

for i in range(rolls):
	all_dices.append(random.randint(1, dice_size))

temp = 0
for i in range(1, dice_size + 1):
	for j in range(rolls):
		if all_dices[j] == i:
			temp += 1
	print("Number {} dropped {} times, the odds are {}%".format(i, temp, 100*(temp/rolls)))
	temp = 0
