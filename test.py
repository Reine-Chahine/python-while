salary = float(input("Enter a salary:"))
month = str(input("Enter the month:"))
saveper =float(input("Enter the percentage of savings:"))
rentper=float(input("Enter the percentage of  rent:"))
electricityper=float(input("Enter the percentage of electricity :"))

savings = (saveper / 100) * salary
rent = (rentper / 100) * salary
electricity = (electricityper / 100) * salary
total = savings +rent+electricity
remainder = salary-total
rentyear = rent * 12
electricitycosts = electricity * 12
totalsal = salary ** 2

newitem=float(input("additional ammount:"))
sum=0
while newitem != "stop":
 if newitem != "stop" :
  newitem=input("additional ammount:")
  

  sum += salary / savings 
  


print ("The month is:",month)
print(f"The savings for {month}: {round(savings, 2)}")
print ("The rent expenses  :", round(rent, 2))
print ("The electricity expenses :", round(electricity, 2))
print ("the total expenses:", round(total, 2))
print ("The remainder of Nabihas salary after these expenses:", round(remainder,2))
print ("yearly rent year expenses:", round(rentyear,2))
print ("yearly electricity year expenses:", round(electricitycosts,2))
print ("total salary for the month raised to the power of 2:", round(totalsal,2))
print ("the sum additional ammount of salary is:",sum)