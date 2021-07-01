num1 = input('enter first number:')
num2 = input('enter second number:')

try:
    print('the sum of numbers is:',int(num1)+int(num2))
except Exception as e:
    print (e)
