salary = float(input("Enter a salary:"))
month = input("Enter the month:")
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
  print ("the sum additional ammount of salary is:",sum)


  print ("The month is:",month)