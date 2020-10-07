import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class DataConversionAndPlotting():
    """
    Date:2020.10.07
    Purpose: Data conversion  & plotting 
    Writer: kcs / katd6@naver.com
    """
    def __init__(self,dataFile,skipRows,nRows,useCols,tumorType):
        """
        skiprows= 생략할 행 수 
        nRows=mouse n 수
        useCols= tumour Volume 측정일수 
        tumorType= 암종 
        """

        self.data=pd.read_excel(dataFile,skiprows=skipRows,nrows=nRows,usecols=useCols)
        self._tumorType=tumorType

    def dataConvert(self):

        y=pd.concat([self.data.iloc[:,[0]],self.data.iloc[:,[1]]],axis=1)
        y["Day"]=1
        y.columns=["Group","Tumor_volume","Day"]
        for i in range(1,len(self.data.columns)-1):
            x=pd.concat([self.data.iloc[:,[0]],self.data.iloc[:,[i+1]]],axis=1) 
            x["Day"]=i+1
            x.columns=["Group","Tumor_volume","Day"]
            y=pd.concat([x,y],axis=0)
        print("변환된 {} Tumor.xlsx 파일이 생성되었습니다.".format(self._tumorType))
        return y.to_excel("{} Tumor.xlsx".format(self._tumorType))

    def __call__(self):
        return self.dataConvert()

    def __str__(self):
        return self._tumorType

    def plot(self):
        self.data.iloc[:,0]=self.data.iloc[:,0].astype('category')
        temp=self.data.iloc[0,0]
        j=0
        index_of_group=[]
        for i in list(self.data.iloc[:,0]):
            j+=1
            if temp != i:
                temp = i
                index_of_group.append(j-1)
        index_of_group.append(len(list(self.data.iloc[:,0])))
        print(" plotting할 총 실험 그룹 개수는 [{}]개 입니다. ".format(len(index_of_group)))
        ## 각 그룹별로 statistic information 확인
        temp=0
        mean_df=pd.DataFrame()
        std_df=pd.DataFrame()
        for i in sorted(index_of_group):
            mean_df=pd.concat([self.data.iloc[temp:i,].describe().iloc[[1],:],mean_df])
            std_df=pd.concat([self.data.iloc[temp:i,].describe().iloc[[2],:],std_df]) ## 그룹별 mean, std 값 추출완료 
            temp=i
        ## naming group
        mean_df.index=list(self.data.iloc[:,0].cat.categories)
        std_df.index=list(self.data.iloc[:,0].cat.categories)
        ## ploting 
        for i in range(len(mean_df.index)):
            y=pd.Series(mean_df.iloc[i,:].astype('float64'))
            x=pd.Series(mean_df.columns).astype("int64")
            x.index=range(1,len(x)+1)
            ymask=np.isfinite(y)
            plt.plot(x[ymask],y[ymask], linestyle='-', marker='o',label='{}'.format(mean_df.index[i-1]))
    
        plt.title("{} Tumor type ".format(self._tumorType))
        plt.ylabel("Tumor volume (mm^3)")
        plt.xlabel("Days after inoculation")
        plt.legend()
        plt.show()




