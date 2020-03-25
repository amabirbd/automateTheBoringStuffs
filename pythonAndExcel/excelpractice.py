import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))
print(wb.sheetnames)
sheet = wb['Sheet3']
print(sheet.title)

actvsheet = wb.active
print(actvsheet)

# Getting Cells from the Sheets
print('\n')

sheet = wb['Sheet1']
print(type(sheet))

for i in sheet.__iter__():
    for j in i.__iter__():
        print(j.value)
    print('\n')


print('\n')

print(sheet['A1'])

print(sheet['A1'].value)

c = sheet['B1']
print(c.value)

print(f'Row {c.row}, Column {c.column}, is {c.value} ')

# row and column can be accessed with number starting frm 1
print('\n')

print(sheet.cell(row=1, column=1))
print(sheet.cell(row=1, column=2).value)

for i in range(1, 8, 2):
    print(i, sheet.cell(row=1, column=2).value)

print('\n')

print(sheet.max_row)
print(sheet.max_column)

print('\n')

# Converting Between Column Letters and Numbers
from openpyxl.utils import get_column_letter, column_index_from_string
print(get_column_letter(1))
print(get_column_letter(2))
print(get_column_letter(27))
print(get_column_letter(sheet.max_column))

print(column_index_from_string('A'))
print(column_index_from_string('AA'))

print('\n')
print(tuple(sheet['A1':'C3']))
print('\n')

for rowOfCellObj in sheet['A1':'C3']:
    for cellObj in rowOfCellObj:
        print(cellObj.coordinate, cellObj.value)
    print('---end of row---')

