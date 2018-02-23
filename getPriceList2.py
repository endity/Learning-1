from xlrd import open_workbook
import math

book = open_workbook("/Users/nguyenducthanh/code/Wine project/ListForPricing.xls")
sheet = book.sheet_by_index(3) #First sheet

WineReference = [] #Looking for wine name
WineYearExcel = [] #Looking for millesime

#for row in range(3, 4):
for row in range(0, 20):
    WineReference.append(sheet.cell(row, 0).value)
    WineYearExcel.append(sheet.cell(row, 3).value)

#print(WineReference)

WineYear = []
for i in WineYearExcel:
    x = str(i)
    x = x[0:4]
    WineYear.append(x)

# print(WineYear)
