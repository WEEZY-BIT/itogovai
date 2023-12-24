n = int(input("Введите количество строк в массиве: "))
arr = []
for i in range(n):
    arr.append(input("Введите строку: "))

new_arr = []
for string in arr:
    if len(string) <= 3:
        new_arr.append(string)

print(new_arr)
