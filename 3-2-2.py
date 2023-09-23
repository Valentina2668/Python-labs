dictionary = {
    'Web-design': '1, 2',
    'Programming': '3, 4',
    'Business_analys': '5, 6'
    }
for speciality, group in dictionary.items():
    print (speciality, '-', group )

query = input ('Which group you`d like to found?')

speciality_list = [speciality for speciality, groups in dictionary.items() if query in groups]
if speciality_list:
    print(', '.join(speciality_list))
else:
    print()
