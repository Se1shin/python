a = [1, 2.1, 3]  # list
tuple(a)  # tuple
b = tuple('abc')

a = (1, 1.1, 'a')
a[0]
a[3]  # Error
a[-4]  # Error

a = {'a': 1, 'b': 2, 1: 'lol'}
a['a']
a[0]  # Error
a.get(0)  # return None or value
a.get(0, 'a')  # return value or second

a = {1, }
a = {1, [3], 1}  # Error contains mutable and duplicated item