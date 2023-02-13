cost=float(input("Enter cost of laptop:"))
allowance=float(input("Enter monthly allowance:"))
sf=float(input("Enter savings fraction:"))
r=float(input("Enter rate of interest:"))

bankAcc=0
month=0

while True:
    bankAcc+=bankAcc*(r/100)
    bankAcc+=(allowance*sf)

    month+=1

    if bankAcc>=cost:
        print(bankAcc-cost)
        break

print(month)
