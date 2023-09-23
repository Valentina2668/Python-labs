
# # 2.3.1 
# a = [15, 4, 8, -62, 89, -2, 64, 0, 36, -34, 23, 1, 2, 3, 4, -68, 4, 94, 35, -487]
# max_number = max(a)
# for index, value in enumerate(a):
#     if value == max_number:
#         print(f"Максимальное значение: {max_number} найдено на позиции {index}")
#         break
# a[index], a[0] = a[0], a[index]
# print(a)



# 2.3.2 
# a = [54, -6, 4, 176, -23, 4, 12, 98, -456, 13]
# min_number = min(a)
# for index, value in enumerate(a):
#     if value == min_number:
#         print ("Минимальное значение:", min_number, "имеет следущий индекс:", index)
#         break
# a[index], a[-1] = a[-1], a[index]
# print(a)



# 2.3.3 
# a = [187, 24, 34.456, -2.45, 123, -456.765, 23, 8, 354.123, -345.765, 12, 65.34, 345, -123, 0]
# max_number = max(a)
# for index, value in enumerate(a):
#     if value == max_number:
#         print('Максимальное значение:', max_number, 'имеет следущий индекс:', index)
#         break
# a[index], a[-1] = a[-1], a[index]
# print(a)



# 2.3.4 
# b = [65, 34.765, 123.56, -34.76, -5, 78, 2.56, -254, 67, -23.45, 345, 5.45]

# min_number = min(b)
# for index, value in enumerate(b):
#     if value == min_number:
#         print('Минимальное значение:', min_number, 'имеет следущий индекс:', index)
#         break
# b[index], b[0] = b[0], b[index]
# print(b)



# 2.3.5 
# c = [65, 34.765, 123.56, -34.76, -5, 78, 2.56, -254, 67, -23.45]
# print('Before sorting: ',c)

# c.sort(reverse=True)
# print('After sorting:', c)

# 2.3.6 

# list = [1, 2, 3, 4, 5, 6, 7, 8, -7, -6, -5, -4, -3, 9, 10]
# print('Before sorting: ', list)

# list.sort()
# print('After sorting:', list)



# 2.3.7 
# a = [-5, -4, -7, -2, 5, 6, 9, 10, 34, 36]
# negativ_number = list()
# for i in a:
#     if i < 0:
#         negativ_number.append(i)
#         a.remove(i)
# a.extend(negativ_number)
# print('After sorting:', a)



# 2.3.8 
# b = [65, 34.765, 123.56, -34.76, -5, 78, 2.56, -254, 67, -23.45, 345, 5.45]
# positiv_number = list()
# for i in b:
#     if i > 0:
#         positiv_number.append(i)
#         b.remove(i)
# b.extend(positiv_number)
# print('After sorting:', b)



# 2.3.9 
# v = [-1, -2, -3, -4, 55, 6, -7, 8, -9, 10, 11, 12, 13, 14]
# v.reverse()
# print(v)


# 2.3.10 
# a = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
# one = list()
# for i in a:
#     if i == 1:
#         one.append(i)
#         a.remove(i)
# a.extend(one)
# print(a)        