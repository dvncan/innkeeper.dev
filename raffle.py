import random 
import sys

try:
	num1 = int(sys.argv[1])
	num2 = int(sys.argv[2])
	num3 = []

	for i in range (0, num1):
		num3.append(random.randint(1, num2))

	print("There can only be", num1, " winners.")
	print("... And they are: ", num3)

except IndexError:
	print("To run this script you need to enter two numbers, 1st for the # of winners & 2nd for the # of entries. - innkeeper")
