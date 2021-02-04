prepCode<-function(fileName,sheetName,target="tumor"){
  library(readxl)
  library(dplyr)
testcase=read_excel(fileName,sheetName)
range=vector()
newDataframe=data.frame()
roof_break=0
temp=0
time=0
repeated=0
#get Start index
for( j in 1:ncol(testcase)){
  for ( i in 1:nrow(testcase)){
    if (grepl("roup",testcase[j,i]))  {
      roof_break=1
      start_row_index=j
      start_col_index=i
      break
    }
  }
  if (roof_break==1){
    break
  }
}
repeated=seq(start_col_index,ncol(testcase),8)
# get Time start index
for( j in 1:ncol(testcase)){
  for ( i in 1:nrow(testcase)){
    if (grepl("treatment",testcase[j,i]))  { 
      roof_break=2
      time=j
      break
    }
  }
  if (roof_break==2){
    break
  }
}
## get Group range 
while(TRUE){
  if(!is.na(testcase[start_row_index,start_col_index+1])){ 
    temp=temp+1
    range[temp]=start_row_index
  }
  if(is.na(testcase[start_row_index,start_col_index+2])){ 
    temp=temp+1
    range[temp]=start_row_index
    break
  }
  start_row_index=start_row_index+1 
}
cat("?????????????????? ?????? ?????????  :" ,time , "?????? ?????? ?????? :" , "(",start_row_index ,",",start_col_index ,")", "????????? ????????? ??????: " ,range ,"??? ?????????????" )
edit(testcase)

ans <-readline('insert plseas : ')
if(ans == "yes"){
  if(target == "tumor"){
  for( j in 1:length(repeated)){ 
  for(i in 1:(length(range)-1)){
    tempDf=data.frame(testcase[range[i]:(range[i+1]-1),repeated[j]+2],testcase[time,repeated[j]],testcase[range[i]:(range[i+1]-1),repeated[j]+3],testcase[range[i]:(range[i+1]-1),repeated[j]+4],testcase[range[i],repeated[j]+1])  ## ????????? df??? V 
    colnames(tempDf)=c("ID","Time_Day","Long_mm","Short_mm","Treatment")
    newDataframe=rbind(newDataframe,tempDf)
  }
  colnames(newDataframe)=c("ID","Time_Day","Long_mm","Short_mm","Treatment")
  } 
  head(na.omit(newDataframe))
  sample_n(newDataframe,20)
  return(newDataframe)
}
else if(target=="weight"){
repeated=seq(start_col_index,ncol(testcase),6)
  for( j in 1:length(repeated)){ 
    for(i in 1:(length(range)-1)){
      tempDf=data.frame(testcase[range[i]:(range[i+1]-1),repeated[j]+2],testcase[time,repeated[j]],testcase[range[i]:(range[i+1]-1),repeated[j]+3],testcase[range[i],repeated[j]+1])  ## ????????? df??? V 
      colnames(tempDf)=c("ID","Time_Day","Weight","Treatment")
      newDataframe=rbind(newDataframe,tempDf)
    }
    colnames(newDataframe)=c("ID","Time_Day","Weight","Treatment")
}
head(na.omit(newDataframe))
return(newDataframe)
}
    else{
      stop("읽고자 하는 대상이 tumor data입니까 또는 weight 데이터 입니까");
    }
  }
  else{
    stop("원본 데이터 재확인해주세요. ")
  }
}

getwd()
setwd("/Users/user/Desktop/RR_pilot/")
tumorSize=prepCode("(----.xlsx","효능평가 종양측정 및 종양 성장 그래프","tumor")
weight= prepCode("---.xlsx","체중 측정 값 및 체중 변화 그래프",target = "weight")
tumorSize$TumorVolume=as.numeric(tumorSize$Long_mm)*(as.numeric(tumorSize$Short_mm)/2)**2
totalData=data.frame(tumorSize[,1:4],tumorSize$TumorVolume,weight$Weight,weight$Treatment)
