import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
import sys
import sqlite3


class DataConversionAndPlotting():
    """
    Date:2020.10.07
    Data conversion & plotting 
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
        database_input=pd.DataFrame()
    def dataConvert(self):
        y=pd.concat([self.data.iloc[:,[0]],self.data.iloc[:,[1]]],axis=1)
        y["Day"]=1
        y.columns=["Group","Tumor_volume","Day"]
        print(y)
        for i in range(1,len(self.data.columns)-1):
            x=pd.concat([self.data.iloc[:,[0]],self.data.iloc[:,[i+1]]],axis=1) 
            x["Day"]=i+1
            x.columns=["Group","Tumor_volume","Day"]
            y=pd.concat([x,y],axis=0)
        y.to_excel("{} Tumor.xlsx".format(self._tumorType))
        mask=np.isfinite(y.loc[:,"Tumor_volume"])
        database_input=y[mask]
        print(database_input)
        return self.connectToSqlite3(database_input)

    def __call__(self):
        return self.dataConvert()

    def __str__(self):
        return self._tumorType

    def plot(self):
        print(self.data)
        ## 2000이 한번넘은건 기록, 그외에는 결측치 처리 
        for j in range(len(self.data.indedx)):
            size=0
            count=0
            print(j)
            print("########################################################################")
            print(list(self.data.iloc[j,:])[1:])
            for i in list(self.data.iloc[j,:])[1:]:
                print(i)
                size+=1
                self.data.iloc[j,size] = float(i)
                if float(i) >=2000:
                    if count == 0:
                        count+=1
                        self.data.iloc[j,size] = float(i)
                    elif count == 1:    
                        self.data.iloc[j,size] = np.nan
        print(self.data)
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
        print("실험 그룹은 {}이며, plotting할 총 실험 그룹 개수는 [{}]개 입니다. ".format(self.data.iloc[:,0],len(index_of_group)))
        ## 각 그룹별로 statistic information 확인
        temp=0
        mean_df=pd.DataFrame()
        std_df=pd.DataFrame()
        for i in sorted(index_of_group):
            mean_df=pd.concat([mean_df,self.data.iloc[temp:i,].describe().iloc[[1],:]])
            std_df=pd.concat([std_df,self.data.iloc[temp:i,].describe().iloc[[2],:]]) ## 그룹별 mean, std 값 추출완료
            temp=i
        ## naming group
        print(std_df.index)
        print(list(self.data.iloc[:,0].cat.categories))
        mean_df.index=list(self.data.iloc[:,0].cat.categories)
        std_df.index=list(self.data.iloc[:,0].cat.categories)
        ## ploting 
        cmap=plt.get_cmap('jet')
        ## 2000이상 한번넘은 경우 제외하기 
        ## soc 
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
        
    def connectToSqlite3(self,database_input):   
        print(database_input)
        conn=sqlite3.connect("TumorGrowthCurve.db")
        cursor=conn.cursor()
        listoftuple=list(zip(list(range(1,len(database_input.index)+1)),list(database_input.loc[:,"Group"]),list(database_input.loc[:,"Tumor_volume"]),list(database_input.loc[:,"Day"])))
        conn.execute('CREATE TABLE IF NOT EXISTS TumorgrowthData(id INTEGER PRIMARY KEY ,experimentalGroup text, tumorVolume REAL,day INTEGER)')
        conn.executemany("INSERT INTO TumorgrowthData(id,experimentalGroup,tumorVolume,day) VALUES(?,?,?,?)",listoftuple)
        conn.commit()
        conn.close()
        


if __name__ == "__main__":
    object_t=DataConversionAndPlotting(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5]),sys.argv[6])
    object_t.plot()
    
