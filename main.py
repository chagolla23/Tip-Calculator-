#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
user_name = input('Name ')
print(f"Welcome {user_name} to the tip calculator!")
total_bill = float((input("What was the total bill? $")))
tip = total_bill * float((input("What percent tip would you like to give? "))) / 100 
new_total = total_bill + tip
people = int(input("How many people to split the bill? "))
split = new_total / people
total_amount = "{:.2f}".format(split) 
print(f"Each person should pay ${total_amount}") 