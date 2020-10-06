## 2020-10-06 plotting 

import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
MC38 = pd.read_excel("MC38_Raw data summary.xlsx",skiprows=3,nrows=35,usecols="A:AF")

##print(MC38.loc['Days after inoculation'])
#y=MC38.iloc[0:3,list(i for i in range(10,15) if i > 12)]
#print(list(i for i in range(10,15) if i > 12))

y=pd.concat([MC38.iloc[:,[0]],MC38.iloc[:,[1]]],axis=1)
print(y.columns)
y["Day"]=1
y.columns=["Group","Tumor_volume","Day"]


for i in range(1,len(MC38.columns)-1):
    x=pd.concat([MC38.iloc[:,[0]],MC38.iloc[:,[i+1]]],axis=1) 
    x["Day"]=i+1
    x.columns=["Group","Tumor_volume","Day"]
    y=pd.concat([x,y],axis=0)


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

print("input 의 실험 그룹 index 는 {} 이며, 총 실험 그룹 개수는 [{}]개 입니다. ".format(index_of_group,len(index_of_group)+1))

## 각 그룹별로 statistic information 확인
temp=0
mean_df=pd.DataFrame()
std_df=pd.DataFrame()
for i in sorted(index_of_group):
    mean_df=pd.concat([MC38.iloc[temp:i,].describe().iloc[[1],:],mean_df])
    std_df=pd.concat([MC38.iloc[temp:i,].describe().iloc[[2],:],std_df]) ## 그룹별 mean, std 값 추출완료 
    temp=i
print(mean_df)
## naming group
print(MC38)
#mean_df.index=MC38.iloc[index_of_group,0]
#std_df.index=MC38.iloc[index_of_group,0]

## ploting 

x=mean_df.iloc[0,:]
#print(x)
#x=x.astype('float64')
#x=pd.Series(x)
#y=MC38.iloc[0,1:]
#y=y.astype('float64')



""" ymask=np.isfinite(y)
x.index=list(range(1,32))
plt.plot(x[ymask],y[ymask], linestyle='-', marker='o')
plt.show()
print(type(x),type(y)) """
