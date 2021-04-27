import pandas as pd

# zoom chat txt -> 채팅 엑셀

print('출석 txt 파일 제목 예시: att-210311.txt')
print('출석 txt 파일 경로: 월/일/att-21{월}{일}.txt')
print('*******************')

month = input('월을 입력하세요(ex. 03): ')
day = input('일을 입력하세요(ex. 11): ')
attendanceCount = int(input('총 몇번의 출석을 했나요?'))

df_from_excel = pd.read_excel('Capstone-2021-1-att.xlsx')
studentDict = {}

for name in df_from_excel['월'][1:]:
    # 각 학생의 기본 출석 상태: 3(결석)
    studentDict[name] = attendanceCount

with open(f'./{month}/{day}/att-21{month}{day}.txt', 'r') as chatTxtFile:
    chatList = chatTxtFile.readlines()
    for chat in chatList:
        splitedChat = chat.split()
        try:
            # 만약 ATT로 시작하는 chat이라면
            if splitedChat[0].find('ATT') != -1:
                # 기존에 정의된 학생 이름 dict에 존재하는 이름이라면
                if studentDict.get(splitedChat[1]) != None:
                    studentDict[splitedChat[1]] -= 1
                # 만약 studentDict에 해당 학생 이름이 무릉이라면
                elif splitedChat[1] == '무릉':
                    studentDict['게를 사이칸 무릉'] -= 1
        except IndexError:
            print(chat)

with open(f'./{month}/{day}/chat-21{month}{day}.txt', 'r') as attChatTxtFile:
    attList = attChatTxtFile.readlines()
    for att in attList:
        splitedAtt = att.split()
        try:
            if splitedAtt[-2].find('ATT') != -1:
                if studentDict.get(splitedAtt[-1]) != None:
                    studentDict[splitedAtt[-1]] -= 1
                # 만약 studentDict에 해당 학생 이름이 무릉이라면
                elif splitedAtt[-1] == '무릉':
                    studentDict['게를 사이칸 무릉'] -= 1
        except IndexError:
            print(att)


# 새로운 학생 출석 데이터프레임 생성
df = pd.DataFrame(list(studentDict.items()), columns=['name', 'ATT'])
df.to_excel(f'./{month}/{day}/att-result-21{month}{day}.xlsx', index=False)
