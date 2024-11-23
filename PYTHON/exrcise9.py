# this is exercise 9 for checking prime number using while loops
num = 313
i = 2
is_prime = True 
while i <= num // 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print('Prime number ',num)
else:
    print("Not prime",num)