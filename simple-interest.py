#compound_interest = p*((1+r/100)**t-1)
# Python Program for simple interest
p = float(input("enter the principle amount: "))
t = float(input("enter the time : "))
r = float(input("enter the rate : "))

simple_interest = (p*t*r)/100
print(f"Simple interest is : {simple_interest:.3f}")
total = p+simple_interest
print(f"Total Amount is : {total:.3f}")
