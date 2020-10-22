import pandas as pd
import numpy as np
from Recursion import RecursionSolve
class DataConversion:

    def __init__(self,data,nrow,range1,sheet_index,k):
        
        self.interval=k
        self.sheet_index=sheet_index
        self.range=range1
        self.nrow=nrow
        self.data=pd.read_excel(data,sheet_name=self.sheet_index,usecols=range1,nrows=nrow)

    def getColRange(self):
        return len(self.data.columns)

    def readByInterval(self):
     
        result=[]
        new_df=pd.DataFrame()
        sum=0
        count=0
        start,stop =tuple(self.range.split(":"))
        for i in stop:
            sum+=ord(i)
        start =ord(start)
        encoding=list(range(start,sum+1,self.interval))
        print(encoding)
        try:
            RecursionSolve(encoding,result,count)

        except Exception as e:
            print(e)

        print("#####################################")
        print(result)
        for i in result:
            df=pd.read_excel(self.data,sheet_name=self.sheet_index,usecols="{}".format(i),nrows=self.nrow)
            new_df=pd.concat([new_df,df],axis=0)
        print(new_df)

a=DataConversion("JIMT-1_anti-B7-H3-ADC_20200303-20200526_주은진.xlsx",56,"G:GI",5,8)
a.readByInterval()