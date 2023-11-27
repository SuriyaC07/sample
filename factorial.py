def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

print("Enter a number ")
n=int(input())
p=fact(n)
print(f"The factorial of {n} is -> {p}")
