from logic import BMI
#displaying the user with warm welcome
print("=========*******welcome to healthylife program********============")

#Taking user weight
weight=float(input("Enter the wight in (kgs): "))

#Taking user height
height= float(input("Enter the height in (ms): "))

#calling BMI function
bmi=BMI(weight,height)

#displaying his BMI
print(f"Your BMI is {bmi}")
