# Write your solution for 1.4 here!

def is_prime(x):
	for i in range(2,x):
		if x%i==0:
			return False
else:
	return True


print(is_prime(15))
print(is_prime(17))