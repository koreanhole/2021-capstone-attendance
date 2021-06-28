import pandas as pd
import os

def deleteDS(fileList: list):
    try:
        fileList.remove('.DS_Store')
    except:
        pass


dirPath = './peer-reviews'

dirList = os.listdir(dirPath)
deleteDS(dirList)

for dirName in dirList:
    fileList = os.listdir(f'{dirPath}/{dirName}')
    deleteDS(fileList)
    reviews = []
    for fileName in fileList:
        filePath = f'{dirPath}/{dirName}/{fileName}'
        try:
            reviewDf = pd.read_excel(filePath, index_col=None, header=1, dtype={ '팀명': str, '점수': float, '의견': str })
            # 점수가 없는 row삭제
            reviewDf.dropna(subset=['점수'], inplace=True)
            reviews.append(reviewDf)
        except KeyError:
            print(fileName + ' -> KeyError')
            
    resultDf = pd.concat(reviews)
    resultDf = resultDf.drop(columns=resultDf.columns[range(3, len(resultDf.columns))], axis=1)
    # 팀명 기준으로 정렬
    resultDf = resultDf.sort_values(by='팀명')
    resultDf.to_excel(f'./concatinated-reviews/{dirName}.xlsx', index=None)

