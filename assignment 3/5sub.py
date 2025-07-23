s1 = int(input("Enter the 1st sub marks:"))
s2 = int(input("Enter the 2nd sub marks:"))
s3 = int(input("Enter the 3rd sub marks:"))
s4 = int(input("Enter the 4th sub marks:"))
s5 = int(input("Enter the 5th sub marks:"))

sum_of_marks=(s1+s2+s3+s4+s5)/500
percentage=sum_of_marks*100

if(percentage >= 75):
    print("Distinction")
elif(percentage >= 60):
    print("First Class")
elif(percentage >= 50):
    print("Second Class")
elif(percentage >= 35):
    print("Pass Class")
else:
    print("Fail")





