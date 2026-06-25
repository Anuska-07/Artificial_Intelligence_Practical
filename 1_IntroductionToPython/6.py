#Calculate the total cost: price = 250, quantity = 5, discount = 10%. Apply 13% tax on the discounted price. 
#Values
price=250
quantity=5
discountPer=0.1
tax=0.13
#Calculation
cost=price*quantity
discountedprice=cost-(cost*discountPer)
Total=discountedprice+(discountedprice*tax)

print("The total cost with discount and tax is:", Total)

