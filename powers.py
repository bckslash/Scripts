n, m, y = input("enter: ").split()

if -10 < int(n) < 10 and -10 < int(m) < 10 and -10 < int(y) < 10:
	for i in range(int(n), int(m) + 1):
		print(f"{i}: ", end="") 
		for j in range(int(y)):
			x = int(pow(i, j))
			print(f"{x} ", end="")
		print()
else:
	print("Range is too big!")