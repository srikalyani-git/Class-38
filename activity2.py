weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in Centimeters: "))
bmi = weight / (height/100)**2
if bmi <= 18.5:
    print("Underweight")
elif 18.5 < bmi <= 24.9:
    print("Healthy")
elif 24.9 < bmi <= 29.9:
    print("Overweight")
elif 29.9 < bmi <= 34.9:
    print("Severely Overweight")
elif 34.9 < bmi <= 39.9:
    print("Obese")
else:
    print("Severely Obese")