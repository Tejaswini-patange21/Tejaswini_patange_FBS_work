a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

ans= (b*b)-(4*a*c)
ans= ans**0.5
root1= (-b+ans)/(2*a)
root2= (-b-ans)/(2*a)

print("root1:" ,root1)
