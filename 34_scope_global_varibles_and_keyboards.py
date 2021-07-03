def main():
    a = 10          #local variable cannot be accessed outside the function
    b = 20
    sum =a+b
    print(sum)
main()

# global variable
a=1  #global variable
def print_Number():
    global a
    a=a+1;
    print(a)
print_Number()

x = 89
def shiv():
    x = 20
    def rohan():
        global x
        x = 88
    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

shiv()
print(x)

