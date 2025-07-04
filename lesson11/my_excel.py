from openpyxl import load_workbook

# def count_kef(height, weight):
#     return height / weight

excel_file = load_workbook("report.xlsx")
page = excel_file["Лист4"]
page["D1"] = "Кэф"

page["D2"] = page["B2"].value / page["C2"].value
page["D3"] = page["B3"].value / page["C3"].value

excel_file.save("result.xlsx")
