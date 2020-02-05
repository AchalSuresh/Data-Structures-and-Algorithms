
# Use of recursive functions
def power(num,pwr):
	if pwr ==0:
		return 1

	else:
		return num * power(num,pwr-1)

	

def factorial(num):
	if num == 0:
		return 1

	else:
		return num*factorial(num-1)

print(power(2,3))
print(factorial(4))