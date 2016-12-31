#value = raw_input("What Planet are you from? ")
#print(value)

def currency_converter(rate,euros):
    dollars = euros*rate
    return dollars

r = raw_input("Enter rate: ")
e = raw_input("Enter euros: ")
print (currency_converter(float(r),float(e)))