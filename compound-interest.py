# Python Program for compound interest
p = float(input("enter the principle amount: "))
t = float(input("enter the time : "))
r = float(input("enter the rate : "))

compound_interest = p*((1+r/100)**t-1)
total = p+compound_interest
print(f"Co interest is : {compound_interest:.3f}")
print(f"Total Amount : {total:.3f}")
