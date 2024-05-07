#!/usr/bin/python3
def fizzbuzz():
	results = []
	for num in range(1, 101):
		if num % 3 == 0 and num % 5 == 0:
			results.append("FizzBuzz")
		elif num % 3 == 0:
			results.append("Fizz")
		elif num % 5 == 0:
			results.append("Buzz")
		else:
			results.append(str(num))
	print(" ".join(results), end=' ')
