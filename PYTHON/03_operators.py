# + Addition  x + y 
# - Subtraction x - y 
# * Multiplication  x * y 
# / Division  x / y 
# % Modulus x % y 
# **  Exponentiation  x ** y  
# //  Floor division  x // y
print("All arithmetic operations utilizes (101,4)")
print(f'Addition:       101 + 4  = {101+4}')
print(f'Subtraction:    101 - 4  = {101-4}')
print(f'Multiplication: 101 * 4  = {101*4}')
print(f'Division:       101 / 4  = {101 / 4}')
print(f'Modulus:        101 % 4  = {101 % 4}')
print(f'Exponentiation: 101 ** 4 = {101 ** 4}')
print(f'Floor division: 101 // 4 = {101 // 4}')

print("\n\nLogical using (a = True, b = False) resulting in False, True, True")
a = True
b = False
print(f'a and b:      {a and b}')
print(f'a or b:       {a or b}')
print(f'a and not b:  {a and not b}')

print("\n\nIdentity and membership operators using (c = {'a':1,'b':2}, d = {'a':1,'b':2}, e = c)")
c = {"a":1,"b":2}
d = {"a":1,"b":2}
e = c
print(f'c is d: {c is d}')
print(f'c is e: {c is e}')
print(f'c is not d: {c is not d}')
print(f'"a" in d: {"a" in d}')
print(f'"c" not in d: {"c" not in d}')