#list
l0 = []
l1 = [2,3,4,5,6,7]
l2 = [3, 'hello', 4.34234, 'world']

print(f'l1: {l1}')
l1.append(2334)
print(f'l1: {l1}')

print(f'l2: {l2}')
print(l2[1]+','+l2[3])
print(f'l2[:2]: {l2[:2]}')
print(f'l2[2:]: {str(l2[2:])}')

l2[0]=6
print(l2[0])

print(l1+l2)
print()

#dictionary
d0 = {}
d1 = {'greeting':'Hello', 'place': 'World'}

print(d1['greeting']+','+d1['place'])
d1['time']='now'
print(d1)
print(d1.keys())
print(d1.values())

