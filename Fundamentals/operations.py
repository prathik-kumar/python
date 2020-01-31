"""
order of operations: PEDMAS
() parantheses
** exponent
~-+ unary operations(complement, minus, plus)
* / % // division, multiplication
+ - Addition, subtraction
>>  <<  Shift bitwise
&  AND bitwise
^ |  OR, NOT bitwise
<= < > >= Comparison
<> == !=  Equality
= %= /= //= *= **= += -= Assignment
"""

amount = 16332
time = 33.33
rate = amount/time
print("Rate: "+str(rate))

bits=16
size= 2**16
print('Size: ' +str(size))

print('11//3: '+str(11//3)) #integer division
print('11/3: '+str(11/3)) #float division
print('11%3: '+str(11%3)) #modulus, gives remainder
#print('11/0: '+str(11/0)) #division by zero!!! error!!

#PEDMAS
print(10 - 2 ** 2 / 2 + 5)

