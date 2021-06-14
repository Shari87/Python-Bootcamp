height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# code below this line
new_height = float(height)
new_weight = int(weight)
# formula to calculate the BMI
BMI = new_weight / (new_height*new_height)
# convert to integer
print(int(BMI))
