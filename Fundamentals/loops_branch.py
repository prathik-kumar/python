a=15

if a<15:
	print('a is less than 15')

if a == 15:
	print('a is equal to 15')
else:
	print('a is something other than 15')

b= 'hello'

if b == 'goodbye':
	print(b)
elif b == 'hello':
	print(b + ' , world')
else:
	print('????')

c = [1, 'hi', 2, 'hello', 3, 'greetings']
#while loop
print('\n simple while loop\n')
while a>0:
	print(a, end=' ')
	a-=1
#for loop
print('\n simple for loop over a list:\n')
for i in c:
	print(i, end= ' $')

#while loop with break
print('\n while loop with a break\n')
while a < 15:
	if a == 7:
		break
	print(a, end=' ')
	a+=1
print()

#for loop with continue
print('\nfor loop with continue\n')
for i in c:
	if i == 3:
		continue #goes back to the beginning of the loop
	print(i, end=' ')
print()

