n = int(input("Введите количество номеров телефонов: "))
phone_book = {}
for _ in range(n):
    phone, name = input("Введите номер телефона и имя через пробел: ").split()
    phone_book[name] = phone
query = input("Введите имя, чей телефон нужно найти: ")

if query in phone_book:
       print("Номер телефона:", phone_book[query])
else:
    print("Нет в телефонной книге")




