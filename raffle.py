import random 
import sys

#print ('Number of arguments:', len(sys.argv), 'arguments.')

#print(random.randint(1,8)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = []

print(num1)

for i in range (0, num1):
	num3.append(random.randint(1, num2))

print(num3)