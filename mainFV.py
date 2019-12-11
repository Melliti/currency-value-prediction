# FV = PV * (1 + r) ^ n 

def main():
    pv = float(input(">> Enter the present value: \n"))
    i = float(input(">> Enter the interest rate: \n"))
    n = float(input(">> enter the number of year: \n"))
    fv = pv * (1 + i) ** n
    print(format(fv, '.2f'))

main()