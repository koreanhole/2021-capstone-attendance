import pandas as pd

# zoom chat txt -> 채팅 엑셀

print('출석 txt 파일 제목 예시: att-210311.txt')
print('출석 txt 파일 경로: 월/일/att-21{월}{일}.txt')
print('*******************')

month = input('월을 입력하세요(ex. 03): ')
day = input('일을 입력하세요(ex. 11): ')

df_from_excel = pd.read_excel('Capstone-2021-1-att.xlsx')
studentDict = {}

for name in df_from_excel['월'][1:]:
    # 각 학생의 기본 출석 상태: 3(결석)
    studentDict[name] = [2, "", ""]
with open(f'./{month}/{day}/att-21{month}{day}.txt', 'r') as chatTxtFile:
    chatList = chatTxtFile.readlines()
    for chat in chatList:
        splitedChat = chat.split()
        try:
            # 만약 ATT로 시작하는 chat이라면
            if splitedChat[0].find('ATT') != -1:
                # 기존에 정의된 학생 이름 dict에 존재하는 이름이라면
                if studentDict.get(splitedChat[1]) != None:
                    studentDict[splitedChat[1]][0] -= 1
                # 만약 studentDict에 해당 학생 이름이 무릉이라면
                elif splitedChat[1] == '무릉':
                    studentDict['게를 사이칸 무릉'][0] -= 1
            if splitedChat[0] == 'FACE':
                # 기존에 정의된 학생 이름 dict에 존재하는 이름이라면
                if studentDict.get(splitedChat[1]) != None:
                    studentDict[splitedChat[1]][1] = 'FACE'
                # 만약 studentDict에 해당 학생 이름이 무릉이라면
                elif splitedChat[1] == '무릉':
                    studentDict['게를 사이칸 무릉'][0][1] = 'FACE'
            if splitedChat[0] == 'DUP':
                # 기존에 정의된 학생 이름 dict에 존재하는 이름이라면
                if studentDict.get(splitedChat[1]) != None:
                    studentDict[splitedChat[1]][2] = 'DUP'
                # 만약 studentDict에 해당 학생 이름이 무릉이라면
                elif splitedChat[1] == '무릉':
                    studentDict['게를 사이칸 무릉'][0][1] = 'DUP'
        except IndexError:
            print(splitedChat)

studentInfo = []
for key, value in studentDict.items():
    studentInfo.append((key, "".join([str(value[0]), value[1], value[2]])))

# 새로운 학생 출석 데이터프레임 생성
df = pd.DataFrame(studentInfo, columns=['name', 'ATT'])
df.to_excel(f'./{month}/{day}/att-result-21{month}{day}.xlsx', index=False)
