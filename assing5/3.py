num_passengers = int(input("Enter number of passenger:"))
ticket_cost = float(input("Enter cost per ticket:"))

total = 0

for i in range(1,num_passengers + 1):
    age = int(input("Enter age of passenger"))

    if(age<12):
        amount = ticket_cost * 0.70
        
    elif(age>59): 
        amount = ticket_cost * 0.50

    else:
        amount = ticket_cost

    total += amount 


print("total ticket amount for passengers:", total)          