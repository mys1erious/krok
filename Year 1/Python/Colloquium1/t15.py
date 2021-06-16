# q = infinity, so there`s no end of cycle.

n = int(input("Enter any number: "))
q = 1
if n>0:
    while q>=1:
        if n%q**2==0 and n%q**3!=0:
            print("When (n//q**2) = natural number and (n//q**3) != natural number, q =", q)
        q += 1
    else:
        print("Doesnt exist")
