import json
import xlwt

path = '/home/x8/Desktop/python/show-me-the-code/0014/student.txt'



workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('student', cell_overwrite_ok=True)

json_txt = None
with open(path,'r') as target:
    json_txt = json.load(target)

for x in range(len(json_txt)):
    worksheet.write(x, 0, x + 1)
    for y in range(len(json_txt[str(x + 1)])):
        worksheet.write(x, y + 1, json_txt[str(x + 1)][y])
workbook.save('students.xls')

print(json_txt)