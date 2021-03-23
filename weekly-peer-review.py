import pandas as pd
import os

month = input('월을 입력하세요(ex. 03): ')
day = input('일을 입력하세요(ex. 11): ')

# peer-review 엑셀 폴더의 위치
dirPath = f'./{month}/{day}/peer-review'

# peer-review 폴더 내 모든 엑셀 파일의 이름
fileList = os.listdir(dirPath)
reviews = []

for fileName in fileList:
    filePath = f'{dirPath}/{fileName}'
    try:
        reviewDf = pd.read_excel(filePath, index_col=None, header=1, dtype={ '팀명': str, '점수': float, '의견': str })
        # 점수가 없는 row삭제
        reviewDf.dropna(subset=['점수'], inplace=True)
        reviews.append(reviewDf)
    except:
        print(fileName)

resultDf = pd.concat(reviews)
resultDf = resultDf.drop(columns=resultDf.columns[range(3, len(resultDf.columns))], axis=1)
# 팀명 기준으로 정렬
resultDf = resultDf.sort_values(by='팀명')

# 팀명 별로 점수의 평균을 구한다.
groupedMean = resultDf['점수'].groupby(resultDf['팀명']).mean()
meanDf = pd.DataFrame({'팀명': groupedMean.index, '점수': groupedMean.values})

# 점수 기준으로 정렬
meanDf = meanDf.sort_values(by='점수', ascending=False)

# 종합 결과와 팀별 평균점수를 엑셀 파일에 저장
resultDf.to_excel(f'./{month}/{day}/peer-review-result.xlsx', index=None)
meanDf.to_excel(f'./{month}/{day}/peer-review-rank.xlsx', index=None)
