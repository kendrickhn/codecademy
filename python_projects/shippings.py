#input weight(lb)
weight = float(input("Enter the weight of the package: "))

#Ground & Drone Shipping Rate
if weight < 0:
    print('Error: Weight cannot be negative. Please enter a valid weight.')
elif weight <= 2:
  ground_rate = 1.5
  drone_rate = 4.5
elif weight > 2 and weight <= 6: 
  ground_rate = 3
  drone_rate = 9
elif weight > 6 and weight <= 10: 
  ground_rate = 4
  drone_rate = 12
elif weight > 10: 
  ground_rate = 4.75
  drone_rate = 14.25

ground_flat_rate = 20
premium_flat_rate = 125

#Calculate shipping price base on weight
ground_price = weight * ground_rate + ground_flat_rate

premium_price = premium_flat_rate 

drone_price = weight * drone_rate

#Print price for each shipping option
if ground_price < premium_price and ground_price < drone_price:
    print("Cheapest option: Ground Shipping at $", ground_price)
elif premium_price < ground_price and premium_price < drone_price:
    print("Cheapest option: Premium Shipping at $", premium_price)
else:
    print("Cheapest option: Drone Shipping at $", drone_price)