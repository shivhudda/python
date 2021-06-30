'''
Exercise 2 - Faulty Calculator
45 * 3 = 555, 56+9 = 77, 56/6 = 4
Design a calculator which will correctly solve all the problems except
the following ones:
45 * 3 = 555, 56+9 = 77, 56/6 = 4
Your program should take operator  and the two numbers as input from the user
and then return the result
'''
# Solution
print('Welcome to on my calculator')
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))
choice = input("choice = +,-,*,/\fwhat do you want->")
if num1==num1 and num2==num2 and choice=='*':
    if num1==45 and num2==3:
        print('your result:',555)
    else:
        print('your result:',num2*num1)
elif num1==num1 and num2==num2 and choice=='+':
    if num1==56 and num2==9:
        print('your result:',77)
    else:
        print('your result:',num2+num1)
elif num1==num1 and num2==num2 and choice=='/':
    if num1==56 and num2==6:
        print('your result:',4)
    else:
        print('your result:',num1/num2)
elif num1==num1 and num2==num2 and choice=='-':
    print('your result:',num1-num2)
else:
    print('enter valid values!')
