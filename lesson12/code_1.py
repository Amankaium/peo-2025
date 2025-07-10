from openpyxl import load_workbook


def count_medium(nums): # [5, 3, 7]
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums) # 15 / 3


def count_solved(cells): # [B2, C2, D2, E2]
    marks_lst = [] # список оценок
    for cell in cells:
        value = cell.value
        if value != None and value > 0:
            marks_lst.append(value)
    medium = count_medium(marks_lst)
    return medium


def count_all_marks(cells): # [B2, C2, D2, E2]
    marks_lst = [] # список оценок
    for cell in cells:
        value = cell.value
        if value == None:
            value = 0
        marks_lst.append(value)
    medium = count_medium(marks_lst)
    return medium
   
        
my_file = load_workbook("report.xlsx")
page = my_file["Лист5"]

i = 2
for row in page["B2:G13"]: # row = [B2, C2, ...] # i = 2
    page["H" + str(i)] = count_solved(row) # page["H2"] = 100.3
    page[f"I{i}"] = count_all_marks(row) # page["I2"] = 50.16
    i += 1   

my_file.save("result.xlsx")
