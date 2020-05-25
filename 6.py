#star pattern
i=0
num=int(input("Enter the number of rows to print:"))
while i<=num:
    print(" "*(i),end='')
    if num%2!=0:
        print("1"*(((num*2)-(i*2)-1)%2!=0),end='')
    else:
        print("0"*(((num*2)-(i*2)-1)%2==0),end='')
    print('')
    i+=1
