#Для списка Х, состоящего из 14 элементов,вывести на печать номера элементов,удовлетворяющих условию 0 < X(i) < 1
X = [4, 6, 12, 462, -13, 23, 0.1, -213, 3, -45, 1, 34, 57, 0.3]
for i in range(len(X)):
        if 0 < X[i] < 1:
            print(i)
        

