#This proram will convert Great British Pounds into 
#either Euros, Yuan, Yen or United States Dollars

#Exchange
gbp=1
usd=1.3
euro=1.11
yuan=8.92
yen=138.44
#Main program
exchange=str(input("What currency would you like to convert to?"))
conversion=float(input("How many Great British Pounds would you like to convert?"))
if exchange=="usd":
    conversion=conversion*1.3
elif exchange=="euro":
    conversion=conversion*1.11
elif exchange=="yuan":
    conversion=conversion*8.92
elif exchange=="yen":
    conversion=conversion*138.44
print(conversion)