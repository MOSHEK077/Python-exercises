#now i write the programm for login system using while loop real world exercisesatt
attempt = 0
username = "Moshek07"
passcode = "Jon$jon12"
while attempt < 3:
    user = input("Enter your Username:")
    passcodes = input("Enter your passcode:")
    if username == user and  passcode == passcodes:
        print("Login successful")
        break
    else:
        attempt += 1
        print(f"Incorrect ! You have { 3 - attempt } attempts left.")
else:
    print("Account locked due to too many fail attempts")