#fibonacii series using while loops
a,b = 0,1
count = 0
while count < 10:
    print(a)
    a,b = b , a+b
    count += 1
print("Congratulations you finished ten exercise using while loop all the best for your carrier")