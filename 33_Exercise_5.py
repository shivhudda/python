'''Health Management System
3 clients - shiv, mahesh and mukesh

def getdate():
    import datetime
    return datetime.datetime.now()

op.write(str([str(gettime())])+": "+content+"\n")

Total 6 files
write a function that when executed takes as input client name
One more function to retrieve exercise or food for any client
'''
import datetime
print('\t\t\t\t\t\t\t\t\t🖖Welcome🖖')
print('Health Management System')
def gettime():
    return datetime.datetime.now()
def log(k):
    if k==1:
        c = int(input('what do you want to log:Press 1(food) or 2(Exercise):'))
        if c==1:
            content = input('Type Here:')
            with open('33_shiv_food.txt','a') as f:
                f.write(str([str(gettime())])+':'+content+'\n')
                print('successfully written.')
        if c==2:       
            content = input('Type Here:')
            with open('33_shiv_exer.txt','a') as f:
                f.write(str([str(gettime())])+':'+content+'\n')
                print('Successfully written.')
    elif k==2:
        c = int(input('what do you want to log:Press 1(food) or 2(Exercise):'))
        if c==1:
            content = input('Type Here:')
            with open('33_mahesh_food.txt','a') as f:
                f.write(str([str(gettime())])+':'+content+'\n')
                print('Successfully written.')
        if c==2:
            content = input('Type Here:')
            with open('33_mahesh_exer.txt','a') as f:
                f.write(str([str(gettime())])+':'+content+'\n')
                print('Successfully written.')
    elif k==3:
        c = int(input('what do you want to log:Press 1(food) or 2(Exercise):'))
        if c==1:
            content = input('Type Here:')
            with open('33_mukesh_food.txt','a') as f:
                f.write(str([str(gettime())])+':'+content+'\n')
                print('Successfully written.')
        if c==2:
            content = input('Type Here:')
            with open('33_mukesh_exer.txt','a') as f:
                f.write(str([str(gettime())])+':'+content+'\n')
                print('Successfully written.')
    else:
        print('Please enter valid details!')

def retrive(k):
    if k==1:
        c = int(input('what do you want to retrive:Press 1(food) or 2(Exercise):'))
        if c==1:
            with open('33_shiv_food.txt') as f:
                for lines in f:
                    print(lines,end='')
        if c==2:
            with open('33_shiv_exer.txt') as f:
                for lines in f:
                    print(lines,end='')
    elif k==2:
        c = int(input('what do you want to retrive:Press 1(food) or 2(Exercise):'))
        if c==1:
            with open('33_mahesh_food.txt') as f:
                for lines in f:
                    print(lines,end='')
        if c==2:
            with open('33_mahesh_food.txt') as f:
                for lines in f:
                    print(lines,end='')
    elif k==3:
        c = int(input('what do you want to retrive:Press 1(food) or 2(Exercise):'))
        if c==1:
            with open('33_mukesh_food.txt') as f:
                for lines in f:
                    print(lines,end='')
        if c==2:
            with open('33_mukesh_food.txt') as f:
                for lines in f:
                    print(lines,end='')
    else:
        print('Please enter valid details!')

choice = int(input('Press 1(log) or 2(retrive):'))
if choice==1:
    b = int(input('Press 1(shiv), 2(mahesh), 3(mukesh)'))
    log(b)
elif choice==2:
    b = int(input('Press 1(shiv), 2(mahesh), 3(mukesh)'))
    retrive(b)



                
  
