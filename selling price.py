cost_price = float(input("enter the cost price of book is:"))
discount = float(input("enter the discount is:"))

discount = (discount/100)*cost_price
selling_price = cost_price-discount

print("The selling price of the book is:",selling_price)
