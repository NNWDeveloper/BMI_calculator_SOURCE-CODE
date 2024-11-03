
import time


print("BMI (Body mass index) calculator")
print("Coded by NNW Developer")

height = input("Enter your height in meters:")
weight = input("Enter your weight in kilograms:")

bmi1 = float(weight) / (float(height)*float(height))


bmi1 = str(bmi1)

bmi = bmi1

print("Your BMI is: "+bmi)
               

time.sleep(15)



