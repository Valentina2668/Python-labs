phoneBook = {'Вася' : '12345',
             'Федя' : '456789',
             'Света' : '987234345',
             'Маша' : '8765',
             'Катя' : '3645',}
			 
print(len(phoneBook))
print (phoneBook)

query = input("Введите имя: ")

if query in phoneBook:
    print(phoneBook[query])
else:
    print("Нет в телефонной книге.")
