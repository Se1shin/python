a = [1, '2', True, None]  # List with difference types
a = []  # Empty list
b = list()  # Empty list too

a = (1, 1.1, 22)  # tuple
list(a)  # returns a like list, but stay a a tuple
b = list('abc')

a = [1, 6, 2]
a[0]  # 1
a[1]  # 6
a[2]  # 2
a[3]  # Error
a[-1]  # 2
a[-2]  # 6
a[-3]  # 1
a[-4]  # Error

a = [1, 5, 'women']
a.index('women')  # returns index of item
a = ['g', 3, 5.5, 5.5]
a[0] = 5
a[1] = 'men'
a.append(4)  # adds item to end of list
a.insert(0, 4)  # adds item into given index
a.insert(['s', 'b'])  # add list into list, may add index
a.extend(['f', 'g'])

del a[0]  # delete item into given index
del a  # full delete a
a.clear()  # clear a list
a.pop()  # returns last item and remove him
a.remove('aa')  # remove element by value

a = [1, 2, 3]  # 1 dim list
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 2 dim list
b[0][0]  # first: list number second: item number into list

a.count(1)  # returns count of item has into list
a.copy  # copy value of list, if into list has list return reference
a.sort()  # sorting list
a.sort(reverse=True)  # sorting list reverse

from copy import deepcopy
b = deepcopy(a)  # copy list recourse