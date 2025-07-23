a1=int(input("Enter 1st person age:"))
a2=int(input("Enter 2nd person age:"))
a3=int(input("Enter 3rd person age:"))
a4=int(input("Enter 4th person age:"))
a5=int(input("Enter 5th person age:"))

amt = 100

if(a1<12):
    fair1= amt - amt *0.3
elif(a1>59):
    fair1= amt*0.5
else:
    fair1= amt
 

if(a2<12):
    fair2= amt - amt *0.3
elif(a2>59):
    fair2= amt*0.5
else:
    fair2= amt
 

if(a3<12):
    fair3= amt - amt *0.3
elif(a3>59):
    fair3= amt*0.5
else:
    fair3= amt
           
    
if(a4<12):
    fair4= amt - amt *0.3
elif(a4>59):
    fair4= amt*0.5
else:
    fair4= amt
     

if(a5<12):
    fair5= amt - amt *0.3
elif(a5>59):
    fair5= amt*0.5
else:
    fair5= amt

total = fair1+fair2+fair3+fair4+fair5
print("the total",total)  


 

