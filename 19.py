#Armstrong Number:
print("enter the number:")
num=int(input())
c=num
a=0;b=0
while num!=0:
    a=num%10
    b=b+(a*(a**2))
    num=num//10
if b==c:
    print(b,':is an Armstrong Number:')
else:
    print(c,':Not an armstrong number')
