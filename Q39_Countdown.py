# Q39 - Countdown using while loop

num = int(input("Enter a number: "))

while num >= 0:
    if num == 0:
        print("Blast!")
    else:
        print(num)
    num -= 1
