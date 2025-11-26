side1 = float(input("Enter  side length of first square:"))
side2 = float(input("Enter side length of second square:"))
height = float(input("Enter height of the walls:"))
    
cost_interior = float(input("Enter cost  for interior painting:"))
cost_exterior = float(input("Enter cost for exterior painting:"))


interior_area = 4 * (side1 + side2) * height
exterior_area = 4 * (side1 + side2) * height

interior_cost = interior_area * cost_interior
exterior_cost = exterior_area * cost_exterior
total_cost = interior_cost + exterior_cost



