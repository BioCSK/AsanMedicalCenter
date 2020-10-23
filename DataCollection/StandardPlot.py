from DataPreProcessing import DataConversion
from Recursion import RecursionSolve
from GetTimeData import GetTime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class StandardPlot(GetTime):

    def plot(self,usecol):
        
        plotDf=pd.read_excel("result.xlsx",skiprows=0,usecols=usecol,nrows=self.nrow,sheet_name=0)
        ## 2000이 한번넘은건 기록, 그외에는 결측치 처리 
        for j in range(len(plotDf.index)):
            print(len(plotDf.columns))
            size=0
            count=0
            
            for i in list(plotDf.iloc[j,:])[1:]:
                print(j)
                #print(size)
                size+=1
                plotDf.iloc[j,size] = float(i)
                if float(i) >=2000:
                    if count == 0:
                        count+=1
                        plotDf.iloc[j,size] = float(i)
                    elif count == 1:    
                        plotDf.iloc[j,size] = np.nan
       
        plotDf.iloc[:,0]=plotDf.iloc[:,0].astype('category')
        
        temp=plotDf.iloc[0,0]
        j=0
        index_of_group=[]
        for i in list(plotDf.iloc[:,0]):
            j+=1
            if temp != i:
                temp = i
                index_of_group.append(j-1)
        index_of_group.append(len(list(plotDf.iloc[:,0])))
        print("실험 그룹은 {}이며, plotting할 총 실험 그룹 개수는 [{}]개 입니다. ".format(plotDf.iloc[:,0],len(index_of_group)))
        ## 각 그룹별로 statistic information 확인
        temp=0
        mean_df=pd.DataFrame()
        std_df=pd.DataFrame()
        indexing=[]
        for i in sorted(index_of_group):
            indexing.append(plotDf.iloc[temp,0])
            mean_df=pd.concat([mean_df,plotDf.iloc[temp:i,].describe().iloc[[1],:]])
            std_df=pd.concat([std_df,plotDf.iloc[temp:i,].describe().iloc[[2],:]]) ## 그룹별 mean, std 값 추출완료
            temp=i
        ## naming group
        print(list(plotDf.iloc[:,0].cat.categories))
        mean_df.index=indexing  ## error 발생 소스코드수정피룡 
        std_df.index=indexing
        print(mean_df)
        ## ploting 
        cmap=plt.get_cmap('jet')
        ## 2000이상 한번넘은 경우 제외하기 
        ## soc 
        colors=[cmap(i) for i in np.linspace(0,1,len(mean_df.index))]
        fig, axes = plt.subplots(nrows=1,ncols=2)
        for i in range(len(mean_df.index)):
            y=pd.Series(mean_df.iloc[i,:].astype('float64'))
            print(mean_df.iloc[i,:])
            x=pd.Series(mean_df.columns.astype("int64"))
            sd=pd.Series(std_df.iloc[i,:].astype("float64"))
            ymask=np.isfinite(y)
                                                                  
            axes[0].plot(x[ymask],y[ymask], linestyle='-', marker='o',label='{}'.format(mean_df.index[i]),color=colors[i])
            axes[1].errorbar(x[ymask],y[ymask],sd[ymask], linestyle='-', marker='o',label='{}'.format(mean_df.index[i]),color=colors[i])
            
        for i in [0,1]:
            axes[i].set_ylabel("Tumor volume (mm^3)")
            axes[i].set_xlabel("Days after inoculation")
            axes[i].legend()
        plt.show()

a=StandardPlot("JIMT-1_anti-B7-H3-ADC_20200303-20200526_주은진.xlsx",56,"G:GI",5,8,9)
a.readByInterval()
#a.GetTimeData("B:GD",7)
a.plot("A:CH")