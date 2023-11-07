m=0
n=1
for i in range(1,6):  #row
    print("")
    for j in range(i):    #column
        if j==1 or j==3:
            print(m,end=" ")    
        else:
            print(n,end=" ")    


n=0
for i in range(1,5):  #row
    print("")
    for j in range(i):    #column
        n=n+1
        print(n,end=" ")






