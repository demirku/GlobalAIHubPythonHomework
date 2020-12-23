a=input('Please enter your name: ')
b=input('Please enter your last name: ')
c=int(input('Please enter your age: '))
d=input('Please enter your dateofbirth (just year): ')

if c<=18:
    e= "You can not go out because it is too dangerous"
else:
    e= "you can go out to the street"

x=[a,b,c,d,e]

for i in x:
    print(i)
