dictionary = {
    'Россия': 'Москва, Казань, Астрахань',
    'Беларусь': 'Минск, Гомель',
    'Венесуэла': 'Каракас, Маракай'
    }
print(len(dictionary))
for country, city in dictionary.items():
    print (country,' ', city )

query = input ('Enter a city ')

country_list = [country for country, city in dictionary.items() if query in city]
if country_list:
    print(', '.join(country_list))
else:
    print()
