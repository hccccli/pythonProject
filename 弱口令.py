import pandas as pd
#from xpinyin import  Pinyin
import openpyxl
import numpy  as np

#from styleframe import StyleFrame
worker=r'C:\Users\litong\Desktop\pass分工\SaaS、PaaS产品接口负责人.xlsx'
person=r'C:\Users\litong\Desktop\pass分工\弱口令.xlsx'
yyresult=r'C:\Users\litong\Desktop\pass分工\yyresult.xlsx'
yy=pd.DataFrame(data=[])
yy.to_excel(yyresult)
file=pd.DataFrame(data=[])
file.to_excel(person)
resultPath =r"C:\Users\litong\Desktop\pass分工\result.xlsx"
writer = pd.ExcelWriter(person,mode='a', engine='openpyxl',if_sheet_exists='new')
writer2 = pd.ExcelWriter(yyresult,mode='a', engine='openpyxl',if_sheet_exists='new')
person=pd.DataFrame(pd.read_excel(person))
yycp=pd.DataFrame(pd.read_excel(worker,4))
worker=pd.DataFrame(pd.read_excel(worker,3))

#worker.columns.values[[0,2,3,4]]
#worker.iloc[0,[0,2,3,4]].values

for i in range(len(worker.iloc[:,0])-1):
    a=worker.columns.values[[0,2,3,4]]
    b=worker.iloc[i,[0, 2, 3, 4]].values
    #mydata=np.row_stack([a, b])
    b=np.array(b).reshape(1,4)
    mydata=pd.DataFrame(data=b,columns=a)
    mydata.to_excel(writer, sheet_name=worker.iloc[i,0],index=False)
writer.save()
writer.close()


jkyz=yycp['监控1组']
setjk=list(set(jkyz))
for i in range(len(setjk)):
    b=yycp[yycp['监控1组']==setjk[i]].values[:,[3,4,14,15]]
    a=yycp.columns.values[[3,4,14,15]]
    mydata = pd.DataFrame(data=b, columns=a)
    mydata.to_excel(writer2, sheet_name=setjk[i],index=False)

writer2.save()
writer2.close()
