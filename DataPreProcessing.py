import pandas as pd
import numpy as np
from Recursion import RecursionSolve
class DataConversion:

    def __init__(self,data,nrow,range1,sheet_index,k,skipRow):
        
        self.interval=k
        self.sheet_index=sheet_index
        self.range=range1
        self.nrow=nrow
        self.fileName=data
        self.skiprow=skipRow
        self.data=pd.read_excel(data,sheet_name=self.sheet_index,usecols=range1,nrows=nrow)

    def getColRange(self):
        return len(self.data.columns)

    def readByInterval(self):
        new_df=pd.DataFrame()
        sum=0
        count=0
        start,stop =tuple(self.range.split(":"))
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

        print("#####################################")
        print(result)
        for i in result:

            df=pd.read_excel(self.fileName,sheet_name=self.sheet_index,usecols=i,nrows=self.nrow,skiprows=self.skiprow)
            print(df)
            new_df=pd.concat([new_df,df],axis=1)

        print(new_df)

    def 기능구현():
        pass
        ## day mapping 
        
