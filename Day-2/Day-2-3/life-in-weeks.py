# input your current age
age = input("What is your current age?")

#Write your code below this line
age_as_int = int(age)

# Assuming you live upto 90
years_remaining = 90 - age_as_int

# Calculate the number of days, weeks, months
days_remaining = years_remaining * 365
weeks_remaining =  years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
