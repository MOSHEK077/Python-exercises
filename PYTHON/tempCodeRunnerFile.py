#guess the number 
correct_number = 21
guess = 0
while guess != correct_number:
    guess = int(input("Guess the number between 10 to 30:"))
    if guess == correct_number:
        print("Correct!")
    else:
        print("Wrong!")