# check whether number is prime ot not :
num = int(input("Enter number : "))

if num > 1:
    for i in range(2, int(num/2)):
        if (num % i) == 0:
            print("is not prime")
            break
    else:
        print("This number is prime")
else:
    print("not possible")
