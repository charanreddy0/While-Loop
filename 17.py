print('enter the number:')
num=int(input())
sum=0
while True:
    sum=sum+int((num%10))
    num=int(num)/10
    if num<10:
        sum=sum+num
        break
print(int(sum))
