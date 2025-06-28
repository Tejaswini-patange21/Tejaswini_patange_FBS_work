p = int(input("enter principle amount: "))
t = int(input("enter no.of time:" ))
r = float(input("enter ratr of interest: "))

interest = p * (1+r) **t

print ("compound interest:" ,interest) 