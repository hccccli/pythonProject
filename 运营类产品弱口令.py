import pandas as pd
import openpyxl
import numpy  as np

#from styleframe import StyleFrame
yyresult=r'C:\Users\litong\Desktop\pass分工\yyresult.xlsx'
yyresult2=r'C:\Users\litong\Desktop\pass分工\yyresult2.xlsx'
yy=pd.DataFrame(data=[])
yy.to_excel(yyresult2)
writer = pd.ExcelWriter(yyresult2,mode='a', engine='openpyxl',if_sheet_exists='new')
meta = pd.DataFrame(pd.read_excel(yyresult, 0))
for i in range(1,18):
    meta2=meta
    worker = pd.DataFrame(pd.read_excel(yyresult, i))
    meta2.iloc[0, 0]=worker.iloc[0,0]
    for j in range(len(worker)-1):
        meta2=meta2.append(meta,ignore_index=True)
        meta2.iloc[12*j,0]=worker.iloc[j+1,0]
    worker=worker.append(meta2)
    worker.to_excel(writer,sheet_name=worker.iloc[0,2],index=False)
writer.save()
writer.close()
