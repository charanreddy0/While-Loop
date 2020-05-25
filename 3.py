#star pattern
num= int(input("enter the number of rows to print:"))
i=0
while i<=num:
    print("*"*i,end='')
    print("")
    i+=1
j=0
while j<=num:
    print("*"*num,end='')
    num-=1
    print('')
    
