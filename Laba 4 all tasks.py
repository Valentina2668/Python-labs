# 4.1
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# unique_numbers = list(set1.union(set2))
# print("Уникальные числа в множествах:", unique_numbers)
# common_numbers = list(set1.intersection(set2))
# common_numbers.sort()
# print("Числа, которые входят и в первое, и во второе множества:", common_numbers)



# 4.2.1 
# a = input("Введите последовательность цифр от 0 до 9: ")
# b = set(a)
# print("Множество элементов последовательности цифр от 0 до 9:",
#       ''.join([x for x in b if x.isdigit()]))



# 4.2.2.
# a = input("Введите последовательность символов буквы от ‘А’ до ‘Z’ и цифры от ‘0’ до ‘5’: ")
# letters_And_Digits = set()
# for char in a.upper():
#     if char >= 'A' and char <= 'Z' or char >= '0' and char <= '5':
#         letters_And_Digits.add(char)
# print('letters_And_Digits: ', letters_And_Digits)



# 4.2.3 (цифры от ‘5’ до ‘9’ и знаки арифметических операций)
# a = input("Введите последовательность символов цифры от ‘5’ до ‘9’ и знаки арифметических операций: ")
# signsAndDigits = set()
# for char in a:
#     if char >= '5' and char <= '9' or char in '+-*/':
#         signsAndDigits.add(char)
# print('signsAndDigits: ', signsAndDigits)



# 4.2.4 
# a = input("Введите последовательность символов знаки арифметических операций и знаки препинания: ")
# signsAndDigits = set()
# for char in a:
#     if char in '+-*/.,:;"!?':
#         signsAndDigits.add(char)
# print('signsAndDigits: ', signsAndDigits)



# 4.2.5
# a = input("Введите последовательность символов знаки арифметических операций и знаки препинания: ")
# signs = set()
# for i in range(len(a)):
#     char = a[i]
#     if char in '.,:;"!?<>=':
#         signs.add(char)
#     if i + 1 < len(a):
#         nextChar = a[i + 1]
#     if char + nextChar in ['<=', '>=', '==', '!=']:
#         signs.add(char + nextChar)
# print('signs: ', signs)


# 4.2.6 
# b = input("Введите последовательность символов знаки арифметических операций: ")
# signs = set()
# for char in b:
#     if char in '+-*/':
#         signs.add(char)
# print('signs: ', signs)


# 4.2.7 
# c = input("Введите последовательность символов знаки препинания и буквы от ‘E’ до ‘N’: ")
# signs_And_Letters = set()
# for char in c.upper():
#     if char in ['.', ',', ':', ';', '"', '!', '?'] or char >= 'E' and char <= 'N':
#         signs_And_Letters.add(char)
# print('signs_And_Letters: ', signs_And_Letters)


# 4.2.8 (знаки арифметических операций и операций отношения)
# d = input('знаки арифметических операций и операций отношения: ')
# signs = set()
# for i in range(len(d)):
#     char = d[i]
#     if char in '+-*/<>=':
#         signs.add(char)
#     if i + 1 < len(d):
#         nextChar = d[i + 1]
#     if char + nextChar in ['<=', '>=', '==', '!=']:
#         signs.add(char + nextChar)
# print('signs: ', signs)



# 4.2.9 
# f = input("Введите последовательность символов цифры и знаки арифметических операций: ")
# digits = set()
# operators = set()
# for char in f:
#     if char.isdigit():
#         digits.add(char)
#     elif char in '+-*/':
#         operators.add(char)
# print("Множество цифр:", digits)
# print("Множество операторов:", operators)


# 4.2.10 
# g = input("Введите последовательность символов буквы от ‘A’ до ‘F’ и от ‘X’ до ‘Z): ")
# letters = set()
# for char in g.upper():
#     if char in 'ABCDEFXZ':
#         letters.add(char)
# print("Множество букв:", letters)


