#guess the number 
#using while loop
correct_number= 19  #var initialize
guess = 0 #including the variable 
while guess != correct_number: #it can check the correct number and guess while not equals
    guess = int(input("Guess the number between 10 to 20::"))#user input
    if guess == correct_number:  #conditon checking
        print('Congratulations You got the correct answer!') #print crt
    else:
        print("Don't worry ! Try again ") #else: print wrong21