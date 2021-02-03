def FizzBuzz(lenght):

	for i in range(1, lenght + 1):

		if i % 15 == 0:
			print(i, "\nFizzBuzz")

		elif i % 5 == 0:
			print(i, "\nBuzz")

		elif i % 3 == 0:
			print(i, "\nFizz")

		else:
			print(i)

FizzBuzz(100)