import random
num = random.randint(1,100)

n=int(input('Enter a number:- '))
a=True
while a:
    for i in range(1,6):
   
        if n==num:    
            print('You won')
            a=False            
            break
        elif i==5:
            ch=input('Do you want to continue ? [y/n]: ')
            if ch=='y':
                i=1
                n=int(input('Enter a number:- '))
            else:
                a=False
                break                
        elif n>num:
            print(f'You have {5-(i)} chances left')
            n=int(input('Enter a smaller number:- '))
        elif n<num:
            print(f'You have {5-(i)} chances left')
            n=int(input('Enter a larger number:- '))
        
