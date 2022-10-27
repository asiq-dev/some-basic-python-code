#  Python Program for factorial of a number
num = int(input("input range for factorial : "))
fact = 1
if (num <= 0):
    print("Factorial does not exist in negative number or 0")
else:
    for i in range(1, num+1):
        fact = fact*i
    print(f"the factorial value of {num} is : {fact}")
