'''
You have to follow certain instructions, which are as follows:
You have to take an integer type variable, and the input of the variable will define the length of the triangle.
You have to declare another Boolean variable.
When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
But if the value of Boolean is 0 or false, then the triangle will be printed upside down.
Exercise 4
Pattern Printing
Input = Integer n
Boolean = True or False
True n=5
*
**
***
****
False n=5
****
***
**
*
'''
# solution
while True:
    inp = int(input('Enter a number:'))
    boolean = int(input('Enter 1 for True and 2 for False or 3 for Exit:'))
    if boolean==1:
        for i in range(1,inp):
            print('*'* i)
    elif boolean==2:
        for j in range(inp-1,0,-1):
            print('*'* j)
    elif boolean==3:
        print('Thanks for join us.')
        exit()
    else:
        print('Enter Valid values!')    
