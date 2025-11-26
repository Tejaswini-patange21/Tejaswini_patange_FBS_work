cp = float(input("Enter Cost Price (CP): "))
sp = float(input("Enter Selling Price (SP): "))

# Calculate and display profit or loss
if(sp > cp):
    profit = sp - cp
    print("Profit of", profit)
elif(cp > sp):
    loss = cp - sp
    print("Loss of", loss)
else:
    print("No Profit No Loss.")
