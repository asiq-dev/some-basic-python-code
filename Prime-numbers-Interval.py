# Python program to print all Prime numbers in an Interval
start = int(input("Enter the lower bound: "))
stop = int(input("Enter the upper bound: "))
for num in range(start, stop+1):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
        print(num)
