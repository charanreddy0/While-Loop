num=int(input("enter the number:"))
count=0
while count<=num:
    print(" "*count,end='')
    if ((num*2)-(count*2)-1)==9 or ((num*2)-(count*2)-1)==1:
        print("1"*((num*2)-(count*2)-1),end='')
    else:
        print("0"*((num*2)-(count*2)-1),end='')   
    count+=1
    print('')
    
