import random
p_ions=["Nitrate", "NO3 -", "Carbonate", "CO3 2-", "Sulfate", "SO4 2-", "Phosphate", "PO4 3-", "Chlorate", "ClO3 -", "Ammonium", "NH4 +", "Hydroxide", "OH -", "Acetate", "C2H3O2 -", "Cyanide", "CN -"]
ions=["Hydrogen ion", "H+", "Lithium ion", "Li+", "Potassium ion", "K+", "Silver ion", "Ag+", "Magnesium ion", "Mg2+", "Calcium ion", "Ca2+", "Zinc ion", "Zn2+", "Gallium ion", "Ga3+", "Aluminum ion", "Al3+", "Sulfide ion", "S2-", "Oxide ion", "O2-", "Hydride ion", "H-", "Cyanide ion", "CN-", "Hydroxide ion", "OH-"]
##mode=str(input("(I)ons, (N)ames, (B)oth  "))
print("Ions quiz, using both ion names and notation. Please capitalize all element symbols appropriately.  Type Q or q to exit.")
c_or_p = str(input("(C)ommon or (P)olyatomic ions?"))
if c_or_p == "C":   
    while True:
        x=random.randint(0, int(len(ions)-1))
        myAnsw=str(input("%s :" % ions[x]))
        if myAnsw=="Q" or myAnsw=="q":
            break
        if x%2!=0:
            trueAnsw=int(x-1)
        if x%2==0:
            trueAnsw=int(x+1)
        if str(myAnsw)==str(ions[trueAnsw]):
            print("Well done!!")

        else:
            print("Wrong. The correct answer is %s" % ions[trueAnsw])


if c_or_p == "P":
    print('''Ions are formatted as Symbol# Charge
For example. Hydroxide is OH -''')
    while True:
        x=random.randint(0, int(len(p_ions)-1))
        myAnsw=str(input("%s :" % p_ions[x]))
        if myAnsw=="Q" or myAnsw=="q":
            break
        if x%2!=0:
            trueAnsw=int(x-1)
        if x%2==0:
            trueAnsw=int(x+1)
        if str(myAnsw)==str(p_ions[trueAnsw]):
            print("Well done!!")

        else:
            print("Wrong. The correct answer is %s" % p_ions[trueAnsw])
        
