# now let i write the programm to find the factorial of any number using while loops
num = int(input('Enter the Number :'))
factorial = 1
while num > 0 : #true 
    factorial *= num
    num -= 1
print("The factorial of this number is:",factorial)
    