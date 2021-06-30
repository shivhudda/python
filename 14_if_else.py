var1 = 34
var2 = int(input('Enter a number:'))
if var2>var1:
    print("Greater")
elif var2==var1:
    print("equal")
else:
    print('lesser')

l1 = [12,34,56,34,5,755]
if 12 not in l1:
    print('yes')
else:
    print('No')

# exercises
# Quiz 1
'''A company decided to give bonus of 5% to employee if his/her year of service is 
more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.'''
# solution
service = int(input("Enter year of service:"))

if service>= 5:
    salary = int(input("Enter your salary:"))
    bonus = salary + salary/100*5
    print('your total salary with bonus is:',bonus)
elif service< 5:
    print("you have not experince of five years.")
else:
    print("Enter valid value")

# Quiz 2   
'''Take values of length and breadth of a rectangle from user 
and check if it is square or not.'''
# solution
length = int(input("Enter length of rectangle:"))
breadth = int(input("Enter breadth of rectangle:"))
if length==breadth:
    print('yes, it is square.')
else:
    print('no,itsn\'t not a square')