# in Python zip is nothing to do with file compression

# some collections
days = ('mon', 'tue', 'wed', 'thur', 'fri') # 5 members
fruits = ['banana', 'orange', 'kiwi', 'durian']
drinks = ('coffee', 'tea', 'water') # 3 members
after  = ['tiramasu', 'icea cream', 'pie', 'creme caramel']

# zip lets us combine collection together

j = zip(days, fruits, drinks, after) # zip respects thet shortest collection
print(j)
for d, f, dr, a in j:
    print('On {} I ate {} with {} then {}'.format(d, f, dr, a))