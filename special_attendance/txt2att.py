import pandas as pd

print('출석 txt 파일 제목 예시: att-210311.txt')
print('출석 txt 파일 경로: 월/일/att-21{월}{일}.txt')
print('*******************')
print('채팅 txt 파일 제목 예시: chat-210311.txt')
print('채팅 txt 파일 경로: 월/일/chat-21{월}{일}.txt')
print('*******************')

month = input('월을 입력하세요(ex. 03): ')
day = input('일을 입력하세요(ex. 11): ')

studentDict = {}

# 첫번째 출석 확인
f = open(f'./{month}/{day}/att-21{month}{day}.txt', 'r')
attendanceList = f.readlines()
f.close()

for attendance in attendanceList:
    student = attendance.split()
    studentName = student[1].strip()
    studentDict[studentName] = 1

# 두번째 출석 확인
f = open(f'./{month}/{day}/chat-21{month}{day}.txt', 'r')
lateChatList = f.readlines()
f.close()

for chat in lateChatList:
    index = chat.find('ATT2')
    # 각 채팅 줄마다 ATT2라는 단어가 있다면
    if index != -1:
        student = chat[index:].split()
        studentName = student[1].strip()
        # 교수님 이름은 건너뛰기
        if studentName == '유하진':
            continue

        # 만약 이미 출석한 학생이라면
        if studentDict.get(studentName) != None:
            # 정상 출석
            studentDict[studentName] = 0
        else:
            # 지각
            studentDict[studentName] = 1

# 새로운 학생 출석 데이터프레임 생성
df = pd.DataFrame(list(studentDict.items()), columns=['name', 'ATT'])
# 출석 결과를 엑셀로 내보내기
# 1: 지각 및 조퇴
# 0: 출석
df.to_excel(f'./{month}/{day}/att-result-21{month}{day}.xlsx', index=False)

