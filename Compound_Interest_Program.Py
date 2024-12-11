def comp_interest(principal, rate, time):
    amount = principal * (1 + rate/time) ** time
    compound_interest = amount - principal

    print("Compound interest of ", principal," is ", compound_interest)




prin = float(input("Enter principal : "))
rate = float(input("Enter rate(%) : "))
time = float(input("Enter time(years) : "))


comp_interest(prin, rate, time)