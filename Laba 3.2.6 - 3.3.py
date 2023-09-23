# 3.2.6	
# word = "contemplation"  
# letter_count = {}  
# for letter in word:
#     if letter in letter_count:
#         letter_count[letter] += 1
#     else:
#         letter_count[letter] = 1
# print(letter_count) 

# 3.2.7	
# n = int(input('Введите количество одноклассников:'))  
# dates = {}  
# for _ in range(n):
#     name, day, month = map(str.lower, input('Введите имя, число. месяц через пробел: ').split())
#     if month not in dates:
#         dates[month] = []
#     dates[month].append(name)
# query_month = input('Введите месяц для поиска:').lower() 
# if query_month in dates:
#     print(" ".join(dates[query_month]))
# else:
#     print()

# 3.2.8	

# list_one = [1, 2, 3, 4, 5, 6, 7, 8]
# list_second = ['dog', 'cat', 'owl', 'horse', 'squierrel', 'hamster', 'racoon', 'mouse']
# new_dict = dict(zip(list_one, list_second))
# print(new_dict)

# 3.2.9	
# students = {
# 'John Smith' : {'month' : 'August', 'day' : '13'},
# 'Dan Frame' : {'month' : 'February', 'day' : '5'},
# 'Lana Brown' : {'month' : 'Oktober', 'day' : '13'},
# 'Sammy Frost' : {'month' : 'June', 'day' : '7'},
# 'Mary Star' : {'month' : 'June', 'day' : '18'}
# }
# print(len(students))
# query_month = input('Enter the month')
# result = []
# for student, info in students.items():
#   if info['month'] == query_month:
#    result.append(student + ' ' + info['day'])
# print(' '.join(result))

# 2.10	
# list_one = [1, 2, 3, 4, 5, 6, 7, 8]
# list_second = ['dog', 'cat', 'owl', 'horse', 'squierrel', 'hamster', 'racoon', 'mouse']
# new_dict = dict(zip(list_second, list_one))
# print(new_dict)



# Задание 3.  
# text = input('Введите текст на русском для перевода:')
# table = {
# 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D',
# 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I',
# 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
# 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
# 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH',
# 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Ъ': '', 'Ь': '',
# 'Э': 'E', 'Ю': 'IU', 'Я': 'IA',
# 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
# 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
# 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
# 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
# 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch',
# 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'ъ': '', 'ь': '',
# 'э': 'e', 'ю': 'iu', 'я': 'ia'
# }
# a = ''
# for char in text:
#   if char in table:
#    a += table[char]
# else:
#    a += char
# print(a)