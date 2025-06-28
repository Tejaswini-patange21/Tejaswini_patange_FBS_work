#to find years,weeks,&days from given no.of days

days = int(input("enter no of days:"))

years =days//365
days = days%365

weeks=days//7
days=days%7

#print("years:",years) 
#print("weeks:",weeks)
#print("days:",days) 
print("years:",years,"weeks:",weeks,"days:",days)

