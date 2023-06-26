import random
a=int(input("Enter a  first number:\n"))
b=int(input("Enter a  second number:\n"))

print("Chosse your operator:'+,-,*,/'")
operator=input("Enter your operator")

if operator=="+":
    c=random.randrange(1,100)
    print(c)

elif operator=="-":
    c=random.randrange(1,100)
    print(c)
    
elif operator=="*":
    c=random.randrange(1,200)
    print(c)
    
else:
