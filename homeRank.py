def getGrossRentMultiplier(totalPrice, totalAnnualRent):
    return(totalPrice/totalAnnualRent)

def meetsOnePercentRule(monthlyGrossRent, totalPrice):
    meetsRule:bool = False
    if(monthlyGrossRent >= .01*totalPrice):
        meetsRule = True
    return meetsRule

def getCapRate(netOperatingIncome, totalPrice):
    return(netOperatingIncome/totalPrice)

def getNetIncomeAfterFinance(netOperatingIncome, financingCosts):
    return(netOperatingIncome - financingCosts)

def getCashOnCashReturn(netOperatingIncome, financingCosts, downPayment):
    niaf = getNetIncomeAfterFinance(netOperatingIncome, financingCosts)
    return(niaf/downPayment)

