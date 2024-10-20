p= int(input("Enter initial principle balance:"))
r= int(input("Enter interest rate:"))
n= int(input("Enter number of times interest applied per time period :"))
t= int(input("Enter time:"))
a= p*(1+r/n)*n*t
print("Compound interest is:",a)
