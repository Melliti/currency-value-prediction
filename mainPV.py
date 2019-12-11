# pv = fv * [1/(1+i)^n]

def main():
    fv = float(input(">> Enter the future value: \n"))
    i = float(input(">> Enter the interest rate: \n"))
    n = float(input(">> enter the number of year: \n"))
    pv = fv * (1 / (1 + i) ** n)
    print(format(pv, '.2f'))

main()
