arr = [0, 1]

for i in range(1, 51):
    arr.append(arr[i]+arr[i-1])
    print(arr[i-1], end=' ')