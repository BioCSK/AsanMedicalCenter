from DataPreProcessing import DataConversion
from Recursion import RecursionSolve
import pandas as pd
import numpy as np

class GetTime(DataConversion):
    """
    writer:김찬수
    input data :클래스 생성시 , 엑셀파일명,읽고자 하는 데이터 행 개수 ,열 범위(tgi data),sheet 선택,간격,스킵할 열개수)
    GetTimeData : 메소드 호출시, 열 범위(time data), 스킵할 열 개수 
    """
    
    def GetTimeData(self,range1,skiprow):
        new_df=[]
        timeData=[]
        sum=0
        count=0
        start,stop =tuple(range1.split(":"))
        ## stop 구현 
        sum=ord(stop[1])
        sum+=(ord(stop[0])-64)*26
        ##
        print(sum)
        start =ord(start)
      
        encoding=list(range(start,sum+1,self.interval))
        print(encoding,len(encoding))
        try:
            result=RecursionSolve(encoding)
            print(a)
        except Exception as e:
            print(e)
        print(result)
        for i in result:
            df=pd.read_excel(self.fileName,sheet_name=self.sheet_index,usecols=i,nrows=1,skiprows=skiprow)
            timeData+=list(df.columns)
        self.timeData=timeData
        print(self.timeData)

       

    def TimeMapping(self):
        emptyDf=np.empty(shape=(self.nrow,max(self.timeData)))
        emptyDf[:]=np.nan
        df=pd.DataFrame(emptyDf)
        df.columns=range(0,max(self.timeData))
        for i in range(len(self.timeData)):
            df.loc[:,self.timeData[i]]=self.new_df.iloc[:,i]
        print(df)
        df.to_excel("result.xlsx")

a=GetTime("JIMT-1_anti-B7-H3-ADC_20200303-20200526_주은진.xlsx",56,"G:GI",5,8,9)
a.readByInterval()
a.GetTimeData("B:GD",7)
