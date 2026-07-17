# Q40 - Grade Checker Program

print("Welcome to the Grade Checker Program")

while True:

    marks = float(input("Enter your marks (0-100): "))

    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: Fail")

    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() == "no":
        print("Thank You!")
        break
