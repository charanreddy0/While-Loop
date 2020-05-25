count=0
x=0
pro=1
print("enter the numbers to find the Average:")
while count!=10:
    num=int(input())
    x=x+num
    pro=pro*num
    count+=1
print("average",x/count)
print('count is:',count)
print('product',pro)

