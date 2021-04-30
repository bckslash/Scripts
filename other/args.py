with open ("list.txt", "r") as file:
    words = file.readlines()

words = sorted(words, key=len, reverse=True)
print(words)

with open("list.txt", "w") as file:
    file.writelines(words)
