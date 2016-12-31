def celtoFah(deg):
    fah = float(deg*(9.0/5)) + 32.0
    if(fah < -273.15):
        fah = "Cannot go below -273.15"
    return fah
    
temperatures = [10,-20,-289, 100]
for temp in temperatures:
    print celtoFah(float(temp))
    

