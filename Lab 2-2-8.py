temperatures = [2, -1, 5, -3, 8, -6, 3, -2, 10]

count = 0
for i in range(len(temperatures)):
    if temperatures[i] < 0:
        count += 1

print("Количество раз, когда температура опускалась ниже нуля:", count)
