list = {'Johnson' :{'day': '2', 'month': 'june'},
           'Alist' :{'day': '7', 'month': 'december'},
           'Trusty' :{'day': '13', 'month': 'june'}
        }

print (len(list))
for surname, date in list.items():
    month = date['month']
    day = date['day']
    print (surname, day, month)
query = input('Enter a month')
result = [name for name, date in list.items()if date ['month'] == query]

if result:
    print (' '.join(result))
else:
    print ()

