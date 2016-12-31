def celtoFah(deg):
    fah = float(deg*(9/5)) + 32.0
    if(fah < -273.15):
        fah = "Cannot go below -273.15"
    return fah
    
Functions = [celtoFah(10),celtoFah(20),celtoFah(-1000)]
print Functions