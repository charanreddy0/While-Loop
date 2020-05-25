num1=int(input("enter the number:"))
count=1
num2=int(input("enter the number:"))
while count<=num1 or count<=num2:
    if num1%count==0 and num2%count==0:
        print('hcf are:',count)
    count+=1
    
    

