from openpyxl import load_workbook
from datetime import datetime


my_file = load_workbook("report.xlsx")
page = my_file["Лист2"]

area = page[f"A2:D{len(page["A"])}"]
matrix = []


print(matrix[-1])
print(matrix[-2])
my_file.save(f"new_file{datetime.now()}.xlsx")
