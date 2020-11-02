import xlrd

filePath = "Alquileres.xlsx"

openFile = xlrd.open_workbook(filePath)

sheet = openFile.sheet_by_name("Data")

print("Numero de filas:", sheet.nrows)
print("Numero de columnas:", sheet.ncols)

for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0),"",sheet.cell_value(i,1),"",sheet.cell_value(i,2),"",sheet.cell_value(i,3),"",sheet.cell_value(i,4),"",sheet.cell_value(i,5))