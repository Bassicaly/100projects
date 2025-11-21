height = int(input("Enter your height in cm: "))
if height >= 120:
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Youth ticket: $5")
    elif age <= 18:
        print("Teen ticket: $7")
    else:
        print("Adult ticket: $12")
else:
    print("Sorry, you are not tall enough to ride.")