try:
    hr = float(input("Enter the working hours: "))
    rate = float(input("Enter the rate per hour: "))
except ValueError:
    print("You were supposed to enter number... -_-")
    exit(0)
if hr > 40:
    sal = (hr-40)*(1.5*rate)+(40*rate)
else:
    sal = hr*rate
print("The salary of the employee=", sal, "Rupees")
