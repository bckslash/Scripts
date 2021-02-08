import random

rolls = int(input("How many dices: "))
print("\n{} dices was thrown".format(rolls))
all_dices = []
one, two, three, four, five, six = 0, 0, 0, 0, 0, 0

for i in range(rolls):
	all_dices.append(random.randint(1, 6))

	if all_dices[i] == 1:
		one += 1
	elif all_dices[i] == 2:
		two += 1
	elif all_dices[i] == 3:
		three += 1
	elif all_dices[i] == 4:
		four += 1
	elif all_dices[i] == 5:
		five += 1
	elif all_dices[i] == 6:
		six += 1

print("{} Ones: {}%".format(one, 100*(one/rolls)))
print("{} Twos: {}%".format(two, 100*(two/rolls)))
print("{} Threes: {}%".format(three, 100*(three/rolls)))
print("{} Fours: {}%".format(four, 100*(four/rolls)))
print("{} Fives: {}%".format(five, 100*(five/rolls)))
print("{} Sixex: {}%".format(six, 100*(six/rolls)))