import pandas as pd
import numpy as np
import csv
import mygene

# meta data 전처리
with open("GSE127165_series_matrix.txt","r",encoding="UTF-8") as f:
    reader=csv.reader(f,delimiter="\t")
    fieldnames=[]
    for i in reader:
        try:
            #print(i[0])
            fieldnames.append(i[0])
        except IndexError as e:
            pass
    fieldnames=list(map(lambda x: x[1:],filter(lambda x: "!"  in x ,fieldnames))) 
    index=dict()
    print(fieldnames)

with open("GSE127165_series_matrix.txt","r",encoding="UTF-8") as f:
    reader=csv.reader(f,delimiter="\t")
    count=0
    try:
        for i in reader:
        #print(i)
            fieldnames[count]
            index[fieldnames[count]]=i[1:]
            count+=1
    except IndexError as e:
        print(e)

print(index["Sample_source_name_ch1"])
## meta data {} : data 0

## RNA-seq data 전처리
#fieldnameOfSample=("ID	C_1	C10	C11	C12	C13	C14	C15	C16	C17	C18	C19	C_2	C20	C22	C23	C24	C25	C26	C27	C28	C29	C_3	C30	C31	C34	C35	C36	C37	C_4	C46	C_5	C50	C51	C52	C53	C54	C55	C56	C57	C58	C59	C_6	C60	C61	C62	C63	C64	C65	C66	C_7	C73	C74	C75	C76	C77	C_8	C_9	P_1	P10	P11	P12	P13	P14	P15	P16	P17	P18	P19	P_2	P20	P22	P23	P24	P25	P26	P27	P28	P29	P_3	P30	P31	P34	P35	P36	P37	P_4	P46	P_5	P50	P51	P52	P53	P54	P55	P56	P57	P58	P59	P_6	P60	P61	P62	P63	P64	P65	P66	P_7	P73	P74	P75	P76	P77	P_8	P_9".split("\t"))
df=pd.read_csv("GSE127165_114_samples_RNA_seq_FPKM.txt",sep="\t")
print(df)
mg = mygene.MyGeneInfo()
ens = df.loc[:,"ID"]
ginfo = mg.querymany(ens, scopes='ensembl.gene')
result=[]
for i in ginfo:
    if "notfound" in i.keys():
        result.append(i["query"])
    else:
        result.append(i["symbol"])

print(len(result),len(df.index))
df.index=result

a_series=(df !=0).all(axis=1)
new_df=df.loc[a_series,:]
new_df.to_excel("GSE127165.xlsx")
