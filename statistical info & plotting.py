## 2020-10-06 plotting version-1/10-7 version 2 

import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
import itertools
MC38 = pd.read_excel("MC38_Raw data summary.xlsx",skiprows=3,nrows=35,usecols="A:AF")

##print(MC38.loc['Days after inoculation'])
#y=MC38.iloc[0:3,list(i for i in range(10,15) if i > 12)]
#print(list(i for i in range(10,15) if i > 12))
MC38.iloc[:,0]=MC38.iloc[:,0].astype('category')
##초기 값설정 
temp=MC38.iloc[0,0]
j=0
index_of_group=[]
## 각 그룹이 어디까지인지를 확인후 describe 함수를 통해 각그룹의 시간대별로 평균 및 평균편차를 구해 그래프그리고자함 
for i in list(MC38.iloc[:,0]):
    j+=1
    if temp != i:
        temp = i
        ## 각 그룹의 인덱스값 확인 
        index_of_group.append(j-1)
index_of_group.append(len(list(MC38.iloc[:,0])))
print(index_of_group)

print(" 총 실험 그룹 개수는 [{}]개 입니다. ".format(len(index_of_group)))

## 각 그룹별로 statistic information 확인
temp=0
mean_df=pd.DataFrame()
std_df=pd.DataFrame()
for i in sorted(index_of_group):
    mean_df=pd.concat([MC38.iloc[temp:i,].describe().iloc[[1],:],mean_df])
    std_df=pd.concat([MC38.iloc[temp:i,].describe().iloc[[2],:],std_df]) ## 그룹별 mean, std 값 추출완료 
    temp=i
## naming group
mean_df.index=list(MC38.iloc[:,0].cat.categories)
std_df.index=list(MC38.iloc[:,0].cat.categories)
## ploting 

for i in range(len(mean_df.index)):
    y=pd.Series(mean_df.iloc[i,:].astype('float64'))
    x=pd.Series(mean_df.columns).astype("int64")
    x.index=range(1,len(x)+1)
    ymask=np.isfinite(y)
    plt.plot(x[ymask],y[ymask], linestyle='-', marker='o',label='{}'.format(mean_df.index[i-1]))
    
plt.title("{} Tumor type ".format(" "))
plt.ylabel("Tumor volume (mm^3)")
plt.xlabel("Days after inoculation")
plt.legend()
plt.show()
