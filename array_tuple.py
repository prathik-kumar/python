#array - similar types of items
from array import array

a1 = array('l') #l - integer type
a2 = array('l', [0,1,2,3,4,5,56,67,7,6])
a3 = array('u', 'hello') #u - unicode characters
a4 = array('d', [2.2, 4.4, 4.2324, 24.543]) #d - floating numbers

print(f"Before pop: {a2}")
a2.pop()
print(f'After pop:{a2}')

a3.append('!')
print(a3)
a3.insert(5, '?')
print(a3)

print('a4[0]: '+str(a4[0]))

print()

#tuples
#immutable sequences or lists

t1 = (1,2,3,4)
t2 = (2.3,3.4,4.3,3.3)
t3 = ('Hello', 'world')
t4 = ('!')

print(f't1: {t1}')
print(f't2[0]: {t2[0]}')
print('t1+t2: {}'.format(t1+t2))


