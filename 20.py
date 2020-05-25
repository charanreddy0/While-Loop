a=10
b=a
while a!=0:
    if a%b==0 and a%1==0:
        print(a)
    a-=1
    print(a)
else:
    print('its not')
