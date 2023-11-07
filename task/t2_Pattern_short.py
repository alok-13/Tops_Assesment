for i in range(5):
    print('*'*i)

print("-----------------")


for i in range(5):
    print(' '*(5-i)+'*'*i)

print("-----------------")


for i in range(5):
    print(' '*(5-i)+'* '*i)

print("-----------------")

for i in range(5):
    print(' '*(i)+'* '*(5-i))

print("-----------------")

for i in range(10):
    if i<=5:
        print(' '*(10-i)+'* '*(i))
    else:
        print(' '*(i)+'* '*(10-i))
