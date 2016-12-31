def celtoFah(deg):
    fah = float(deg*(9.0/5)) + 32.0
    if(fah < -273.15):
        fah = "Cannot go below -273.15"
    return fah

file = open("Awesome.txt","w")
temperatures = [10,-20,-289,100]
for temp in temperatures:
    temp = celtoFah(temp)
    file.write(str(temp)+"\n")
    
file.close()