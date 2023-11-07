m='A'
n=0
for i in range(1,6):
    print("")
    for j in range(i):
        print(chr(ord(m)+n),end='')  
        n=n+1


m='A'
for i in range(1,6):
    print("")
    for j in range(i):
        print(chr(ord(m)+(j)),end='')
        
