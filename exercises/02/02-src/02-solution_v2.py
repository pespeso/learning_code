from random import randrange
import time

initTime = time.time()

number = int(random.random()*1000000)
step = int(random.random()*10)
result1 = 0
result2 = 0

for n in range(0,number+1):
    result1 += n

for n in reversed(range(0,number+1,2)):
    result2 += n

print("RandomNumber:",number)
print("The difference is",result1-result2)
print("Time execution:", time.time() - initTime)