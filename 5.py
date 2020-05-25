num = int(input("enter the number of rows to print:"))
j=0
while j<=num:
    print(' '*(j),end='')
    print("*"*(num*2-(j*2)-1),end='')
    print('')
    j+=1
