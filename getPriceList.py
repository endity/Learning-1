from xlrd import open_workbook

book = open_workbook("ChateauReference.xls")
sheet = book.sheet_by_index(0) #First sheet

WineReference = []

#for row in range(3, 4):
for row in range(3, 69):
    WineReference.append(sheet.cell(row, 2).value)

#print(WineReference)
