number = int(input('Enter a number:'))
def fact_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac
print(fact_iterative(number))

def fac_recursion(n):
    if n==1:
        return 1
    else:
        return n*fac_recursion(n-1)
print(fac_recursion(number))

#findind fibonacci number
num =int(input("Enter a number:"))
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(num))
