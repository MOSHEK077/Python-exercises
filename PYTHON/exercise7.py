# write a program to count the sum of the degits of the given number
number = 13341
total = 0
while number >0 :
    total += number % 10
    number //= 10
print("Sum of the digits:",total)