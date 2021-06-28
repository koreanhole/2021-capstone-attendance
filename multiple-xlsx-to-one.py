from asyncore import write
import pandas as pd
import os
from openpyxl import load_workbook


def deleteDS(fileList: list):
    try:
        fileList.remove('.DS_Store')
    except:
        pass

fileList = os.listdir('./concatinated-reviews')
deleteDS(fileList)

book = load_workbook('./all-students.xlsx')
writer = pd.ExcelWriter('./all-students.xlsx', engine='openpyxl')
writer.book = book

fileList.sort()
for fileName in fileList:
    print(fileName[:-5])
    student_review = pd.read_excel(f'./concatinated-reviews/{fileName}', index_col=None)
    student_review.to_excel(writer, sheet_name=fileName, index=None)

writer.save()
writer.close()