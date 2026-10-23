# Write a Program that takes total bill amount and number of friends as input and calculate how much each person will pay. 
# Also print the data types of each variables used.

Total_bill_amount = float(input("Enter your total bill amount: "))
Number_of_friends = int(input("Enter your Number of Friends: "))
Each_person_pay = Total_bill_amount / Number_of_friends
print("Each person will pay: ", Each_person_pay)
print("Data type of Total_bill_amount:", type(Total_bill_amount))
print("Data type of Number_of_friends:", type(Number_of_friends))
print("Data type of Each_person_pay:", type(Each_person_pay))

