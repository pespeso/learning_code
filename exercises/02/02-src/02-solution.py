from functools import reduce

number = int(input("Insert a integer number"))
result1 = 0
result2 = 0

for n in range(0,number+1):
    result1 += n

for n in reversed(range(0,number+1,2)):
    result2 += n

print("The difference is",result1-result2)