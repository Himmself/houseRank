print("----House Rank----\n")

import sys
import csv
import homeRank

# print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
csvFile = open(str(sys.argv[1]))
csvreader = csv.reader(csvFile)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

for house in rows:

    totalPrice = int(house[1])
    totalAnnualRent = int(house[2])*12
    monthlyGrossRent = totalAnnualRent/12
    netAnnualOperatingIncome = totalAnnualRent - int(house[3])*12
    financingCostAnnually = int(house[4])*12
    downPayment = totalPrice * 0.2

    GRM = homeRank.getGrossRentMultiplier(totalPrice, totalAnnualRent)
    isOnePercent = homeRank.meetsOnePercentRule(monthlyGrossRent, totalPrice)
    capRate = homeRank.getCapRate(netAnnualOperatingIncome, totalPrice)
    NIAF = homeRank.getNetIncomeAfterFinance(netAnnualOperatingIncome, financingCostAnnually)
    cashOnCash = homeRank.getCashOnCashReturn(netAnnualOperatingIncome, financingCostAnnually, downPayment)

    print("Down Payment: ",str(downPayment))
    print("GRM: ",str(GRM))
    print("1% Rule: ",str(isOnePercent))
    print("Cap Rate: ",str(capRate*100), "%")
    print("Net Income After Financing: ",str(NIAF))
    print("Net Income After Financing (perMonth): ",str(NIAF/12))
    print("Cash On Cash: ",str(cashOnCash*100), "%")
