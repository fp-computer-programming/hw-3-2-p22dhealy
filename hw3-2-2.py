# author: DMH 9/30/21

weight = input("Input Weight:")

height = input("Input Height:")

bmi = int(weight) / float(height)

if int(bmi) < 19:
    print("You are underweight")
elif int(bmi) < 25:
    print("You are healthy")
elif int(bmi) < 30:
    print("You are overweight")
elif int(bmi) < 40:
    print("You are obese")
else:
    print("You are extremely obese")
