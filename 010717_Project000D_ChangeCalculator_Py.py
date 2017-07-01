#Project 000D, a change calculator


EUR = {"500.00":0,"200.00":0,"100.00":0,"50.00":0,"20.00":0,"10.00":0,"5.00":0,"2.00":0,
       "1.00":0,"0.50":0,"0.20":0,"0.10":0,"0.05":0,"0.02":0,"0.01":0}

def CalculateChange(paid, price, moneySystem):
    """ Takes 3 arguments: The amount paid by the customer, the price of the
        thing paid for and the monetary system (e.g. Euro, Dollar, Pounds).
        It returns a dictionary of denominations and the corresponding amounts"""
    
    if (paid < price):
        print ("The paid amount is not adequate")
        
    else:
        newDict = dict(moneySystem)
        change = paid - price

        for denom in newDict:
            while ((change - float(denom)) >= 0):
                newDict[denom] += 1
                change -= float(denom)

        return newDict, change
        
def PrintChange(paid, price, moneySystem):
    """ Removes all of the unnecessary information and prints a clean list."""

    denomDict, remainder = CalculateChange(paid, price, moneySystem)

    print("List of change" )
    
    for denom in denomDict:
        if (denomDict[denom] != 0):
            print(str(denom) + ": " + str(denomDict[denom]))

    print()
    print("Remainder: " + str(remainder))
