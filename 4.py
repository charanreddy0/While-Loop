# star pattern
num=int(input("enter the values to print:"))
i,j=1,0
while i<=num:
    print(' '*(num-i),end='')
    print("*"*(i*2-1),end='')
    print('')
    i+=1
while j<=num:
    print(' '*(j),end='')
    print("*"*(num*2-(j*2)-1),end='')
    print('')
    j+=1
