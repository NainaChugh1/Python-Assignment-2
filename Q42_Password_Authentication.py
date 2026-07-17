# Q42 - Password Authentication

password = "python123"

attempt = 1

while attempt <= 3:

    entered = input("Enter Password: ")

    if entered == password:
        print("Access Granted")
        break
    else:
        print("Wrong Password")
        attempt += 1

if attempt > 3:
    print("Access Denied")
