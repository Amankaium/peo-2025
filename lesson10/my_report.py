from openpyxl import load_workbook

my_file = load_workbook("report.xlsx")
page = my_file["Лист2"]

workers = {}
data = page["A:D"]
matrix = []
for row in data:
    matrix.append([])
    for cell in row:
        matrix[-1].append(cell.value)

print(matrix[-1])
print(matrix[-2])
my_file.save("new_file.xlsx")
