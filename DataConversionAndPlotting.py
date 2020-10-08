import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl


class DataConversionAndPlotting():
    """
    Date:2020.10.07
    Purpose: Data conversion  & plotting 
    Writer: kcs / katd6@naver.com
    """
    def __init__(self,dataFile,skipRows,nRows,useCols,sheet_name,tumorType):
        """
        skiprows= 생략할 행 수 
        nRows=mouse n 수
        useCols= tumour Volume 측정일수 
        tumorType= 암종 

        """

        self.data=pd.read_excel(dataFile,skiprows=skipRows,nrows=nRows,usecols=useCols,sheet_name=sheet_name)
        self._tumorType=tumorType
        print(self.data.head(3))
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
        print(" 실험 그룹은 {}이며, plotting할 총 실험 그룹 개수는 [{}]개 입니다. ".format(self.data.iloc[:,0],len(index_of_group)))
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
        cmap=plt.get_cmap('jet')
        colors=[cmap(i) for i in np.linspace(0,1,len(mean_df.index))]
        fig, axes = plt.subplots(nrows=1,ncols=2)
        for i in range(len(mean_df.index)):
            y=pd.Series(mean_df.iloc[i,:].astype('float64'))
            x=pd.Series(mean_df.columns.astype("int64"))
            sd=pd.Series(std_df.iloc[i,:].astype("float64"))
            x.index=range(1,len(x)+1)
            ymask=np.isfinite(y)
            axes[0].plot(x[ymask],y[ymask], linestyle='-', marker='o',label='{}'.format(mean_df.index[i]),color=colors[i])
            axes[1].errorbar(x[ymask],y[ymask],sd[ymask], linestyle='-', marker='o',label='{}'.format(mean_df.index[i]),color=colors[i])
        for i in [0,1]:
            axes[i].set_title("{} ".format(self._tumorType))
            axes[i].set_ylabel("Tumor volume (mm^3)")
            axes[i].set_xlabel("Days after inoculation")
            axes[i].legend()
        plt.show()
        

