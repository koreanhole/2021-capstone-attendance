# 출석을 수기로 기록

import pandas as pd

month = input('월을 입력하세요(ex. 03): ')
day = input('일을 입력하세요(ex. 11): ')

df_from_excel = pd.read_excel('Capstone-2021-1-att.xlsx')
studentDict = {}

for name in df_from_excel['월'][1:]:
    # 각 학생의 기본 출석 상태: 3(결석)
    studentDict[name] = 3

while True:
    studentName = input('학생 이름을 입력해주세요: ')
    if studentDict.get(studentName):
        studentDict[studentName] = 0
    else:
        break

# 새로운 학생 출석 데이터프레임 생성
df = pd.DataFrame(list(studentDict.items()), columns=['name', 'ATT'])
df.to_excel(f'./{month}/{day}/att-result-21{month}{day}.xlsx', index=False)