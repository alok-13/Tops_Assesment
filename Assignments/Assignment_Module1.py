#Module 2
#Problem 1

##a=int(input("Enter a number: "))
##
##if a==0:
##    print("Entered number is Zero")
##
##elif a%2==0:
##    print("Entered number is Even")
##
##else:
##    print("Entered number is Odd")

#Problem 2

##b=int(input("enter a number : "))
##i=1
##c=1
##while i<b:
##    c=c*(i+1)
##    i=i+1
##print(c)

#Problem 3

##a=int(input("Enter a number: "))
##b=0
##i=1
##c=1
##d=1
##while i<=a:
##    b=c
##    c=d
##    if i==1:
##        b=0
##        i+=1
##        print(b)
##    elif i==2:
##        b=1
##        i+=1
##        print(b)
##    else:
##        d=b+c
##        i+=1
##        print(d)
        
#Problem 4

##Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the Python memory manager. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.
##
##At the lowest level, a raw memory allocator ensures that there is enough room in the private heap for storing all Python-related data by interacting with the memory manager of the operating system. On top of the raw memory allocator, several object-specific allocators operate on the same heap and implement distinct memory management policies adapted to the peculiarities of every object type. For example, integer objects are managed differently within the heap than strings, tuples or dictionaries because integers imply different storage requirements and speed/space tradeoffs. The Python memory manager thus delegates some of the work to the object-specific allocators, but ensures that the latter operate within the bounds of the private heap.
##
##It is important to understand that the management of the Python heap is performed by the interpreter itself and that the user has no control over it, even if they regularly manipulate object pointers to memory blocks inside that heap. The allocation of heap space for Python objects and other internal buffers is performed on demand by the Python memory manager through the Python/C API functions.

#Problem 5


#Problem 6
n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
temp=1
temp=n1
n1=n2

n2=temp

print(n1,n2)

#Problem 7

##a=input("Enter a character: ")
##
##if a=='a' or a=='i' or a=='o' or a=='u':
##    print("Entered character is a Vowel")
##
##else:
##    print("Entered character is a Consonent")

#Problem 8

##n1=int(input("Enter first number: "))
##n2=int(input("Enter second number: "))
##n3=int(input("Enter third number: "))
##
##if n1==n2 or n2==n3 or n1==n3:
##    print(0)
##else:
##    print(n1+n2+n3)


#Problem 9

##n1=int(input("Enter first number: "))
##n2=int(input("Enter second number: "))
##
##if n1==n2 or (n1+n2)==5 or ((n1-n2))==5:
##    print('TRUE')

#Problem 10

##n=int(input("Enter a number: "))
##n=((n*(n+1)/2))
##print(n)
    
#Problem 11

##str=input("Enter a string: ")
##n=0
##for i in str:
##    if i!=' ':
##        n+=1
##print(n)

#Problem 12

##str=input("Enter a string: ")
##ch=input("Enter a character: ")
##n=0
##for i in str:
##    if ch==i:
##        n+=1
##print(n)

#Problem 13
