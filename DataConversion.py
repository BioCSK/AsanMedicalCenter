class DataConversion():
    """
    Date:2020.10.05
    Purpose: Data conversion
    Writer: kcs / katd6@naver.com
    """
    import pandas as pd
    import numpy as np

    def __init__(self,dataFile,skipRows,nRows,useCols,tumorType):
        """
        skiprows= 생략할 행 수 
        nRows=mouse n 수
        useCols= tumour Volume 측정일수 
        tumorType= 암종 
        """
        self._skipRows=skipRows
        self._nRows=nRows
        self._useCols=useCols
        self._dataFile=dataFile
        self._tumorType=tumorType

    def dataConvert(self):
        data=pd.read_excel(self._dataFile,skiprows=self._skipRows,nrows=self._nRows,usecols=self._useCols)
        y=pd.concat([data.iloc[:,[0]],data.iloc[:,[1]]],axis=1)
        y["Day"]=1
        y.columns=["Group","Tumor_volume","Day"]
        for i in range(1,len(data.columns)-1):
            x=pd.concat([data.iloc[:,[0]],data.iloc[:,[i+1]]],axis=1) 
            x["Day"]=i+1
            x.columns=["Group","Tumor_volume","Day"]
            y=pd.concat([x,y],axis=0)
        print("변환된 {} Tumor.xlsx 파일이 생성되었습니다.".format(self._tumorType))
        return y.to_excel("{} Tumor.xlsx".format(self._tumorType))

    def __call__(self):
        return self.dataConvert()

