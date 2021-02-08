


\documentclass[a4paper, 11pt]{report}
\usepackage[left=1.5cm,right=1.5cm,top=2cm,bottom=4.5cm,a4paper]{geometry}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{booktabs}
\usepackage{kotex}
\usepackage[hangul, nonfrench]{dhucs}
\usepackage{titlesec}

\renewcommand{\arraystretch}{1.2}

\def\thesection{\arabic{section}}
\def\thesubsection{\arabic{section}.\arabic{subsection}}
\def\thesubsubsection{\arabic{section}.\arabic{subsection}.\arabic{subsubsection}}

\titleformat{\paragraph}
{\normalfont\normalsize\bfseries}{\theparagraph}{1em}{}
\titlespacing*{\paragraph}
{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}

\usepackage{fancyhdr}
\pagestyle{fancy}\setlength\headheight{100pt}
\fancyhead[L]{\includegraphics[width=4cm]{C://Users//user//Desktop//APEX//Logo//APEX_logo.png}}
\fancyhead[R]{\textbf{Center for Advancing Cancer Therapeutics\\}}

\renewcommand{\headrulewidth}{2pt}
\renewcommand{\footrulewidth}{1pt}

\usepackage{longtable}
\usepackage{caption}
\usepackage{indentfirst}
%\parindent=1em
 \usepackage{subcaption}
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{4}

\renewcommand{\contentsname}{TABLE OF CONTENTS}
%\newenvironment{knitrout}{}{} 
\renewcommand{\contentsname}{목록}

\usepackage{alltt}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage{makecell}
\usepackage{setspace}
\usepackage{type1cm}
\usepackage{array}
\usepackage{pdflscape, lipsum}
\usepackage{enumerate}

\usepackage{graphicx}
\DeclareGraphicsExtensions{.pdf,.png,.jpg}
\usepackage[table,xcdraw]{xcolor}
\usepackage{floatrow}

\linespread{1.5}
\IfFileExists{upquote.sty}{\usepackage{upquote}}{}

\begin{document}
\addtocounter{section}{5}

\section{결과 및 토의}

<<echo=FALSE, warning=FALSE, error=FALSE, results='asis', message=F >>=
Round = function(x, n=0)
{
  posneg = sign(x)
  z = abs(x)*10^n
  z = z + 0.5
  z = trunc(z)
  z = z/10^n
  return(z*posneg)
}
getTGIPercent = function(drugName,time=timeDay,controlName="vehicle"){
  deltaControl = mean(totalData$tumor_Volume[totalData$group==controlName & totalData$Time_Day==time]) - mean(totalData$tumor_Volume[totalData$group==controlName & totalData$Time_Day==0])
  deltaDrug = mean(totalData$tumor_Volume[totalData$group==drugName & totalData$Time_Day==time])  - mean(totalData$tumor_Volume[totalData$group== drugName & totalData$Time_Day== 0 ])
  return(Round((1-deltaDrug/deltaControl)*100,2))
}
prepCode<-function(fileName,sheetName,target="tumor"){
  library(stringr)
  library(readxl)
  library(dplyr)
  library(stringi)
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
##cat("?????????????????? ?????? ?????????  :" ,time , "?????? ?????? ?????? :" , "(",start_row_index ,",",start_col_index ,")", "????????? ????????? ??????: " ,range ,"??? ?????????????" )
edit(testcase)

##ans <-readline('insert plseas : ')
ans <-"yes"
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
      tempDf=data.frame(testcase[range[i]:(range[i+1]-1),repeated[j]+2],testcase[time,repeated[j]],testcase[range[i]:(range[i+1]-1),repeated[j]+3],testcase[range[i],repeated[j]+1])  ## ????????? df??? 
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
setwd("/Users/user/Desktop/RR_pilot/")
  tumorSize=prepCode("-----------.xlsx","효능평가 종양측정 및 종양 성장 그래프","tumor")
  weight= prepCode("------.xlsx","체중 측정 값 및 체중 변화 그래프",target = "weight")
groupSeparation = read_excel("GroupSeparation.xlsx")
tumorSize$TumorVolume=as.numeric(tumorSize$Long_mm)*((as.numeric(tumorSize$Short_mm)/2)**2)*2
totalData=data.frame(tumorSize[,1],as.numeric(tumorSize$Time_Day),tumorSize[,3:4],tumorSize$TumorVolume,as.numeric(weight$Weight),weight$Treatment)
colnames(totalData)=c("ID","Time_Day","Long_mm^3","Short_mm^3","tumor_Volume","weight","group")
totalData$group = str_replace_all(totalData$group,"[\r\n]"," ")
totalData$group = stri_trim(totalData$group)
getAvgAndSd= function(groupSeparation){
  temp = groupSeparation %>% group_by(Group) %>% summarise(Average=mean(tumorVolume)) %>% select(Group,tumorVolume=Average)
  temp$ID="Mean"
  temp2 = groupSeparation %>% group_by(Group) %>% summarise(SD=sd(tumorVolume)) %>% select(Group,tumorVolume=SD)
  temp2$ID="SD"
  tempDf = rbind(temp,temp2) %>% select(ID,tumorVolume,Group) %>% rbind(groupSeparation) %>% arrange(ID)
  return(tempDf)
}
library(dplyr)
library(ggplot2)
library(knitr)
library(kableExtra)
library(xtable)
 
@

\subsubsection{종양 성장 확인 및 군 분리}
\noindent - ----- 일째, ---- \Sexpr{Round(mean(groupSeparation$tumorVolume),2)} $mm^3$ 오차 $\pm$ \Sexpr{Round(sd(groupSeparation$tumorVolume),2)} -----------
\newline
<<echo=FALSE, warning=FALSE, error=FALSE, message=F >>=

groupSeparation = getAvgAndSd(groupSeparation = groupSeparation)
groupSeparation$tumorVolume = Round(groupSeparation$tumorVolume,2)
tempList=list()
groupingColume=2
group=unique(groupSeparation$Group)
  for(i in seq_along(group)){
   tempList[[i]] = groupSeparation%>% filter(Group == group[i]) %>% select(ID,tumorVolume) 
  }
tempList=do.call(cbind, tempList)
kable(tempList,format="latex", booktabs=T, align="c" , caption="군 분리 시 종양 부피")%>% kable_styling(font_size = 12,latex_options =c("hold_position")) %>% add_header_above(c(
    setNames(groupingColume,group[1]),setNames(groupingColume,group[2]),setNames(groupingColume,group[3]),setNames(groupingColume,group[4])
    ### 군분리 group별로 header를 추가합니다. 
  ),bold = T, italic = T)
@


\noindent - ---- \Sexpr{getTGIPercent("---  15mg/kg",35)}\% 
\newline
\newline
\noindent  * TGI: Tumor growth inhibition \{1-($\Delta$T/$\Delta$C)\}$\times100$
\newline
<<echo=FALSE, warning=FALSE, error=FALSE, results='asis', message=F>>=
tumorTable=totalData %>% select(ID,Time_Day,`Long_mm^3`,`Short_mm^3`,tumor_Volume,group)
for(i in 3:5){
  tumorTable[,i]=Round(as.numeric(tumorTable[,i]),2)
}
colnames(tumorTable)=c("ID","Time","Long(mm)","Short(mm)","Size(mm^3)","Group")
kable(
  x=tumorTable
                ,format="latex", longtable=T, booktabs=T, align="c", caption="종양부피의 평균 및 표준편차") %>% kable_styling(font_size = 12,latex_options =c("hold_position")) 
@






