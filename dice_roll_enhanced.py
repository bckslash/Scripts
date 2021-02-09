import random

dice_size = int(input("How many sides: "))
rolls = int(input("How many dices: "))
all_dices = []

for i in range(rolls):
	all_dices.append(random.randint(1, dice_size))

temp = 0
for dice_number in range(1, dice_size + 1):
	for i in range(len(all_dices)):
		if all_dices[i] == dice_number:
			temp += 1
	print("Number {} dropped {} times, the odds are {}%".format(dice_number, temp, 100*(temp/rolls)))
	temp = 0
