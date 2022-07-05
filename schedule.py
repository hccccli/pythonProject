import pandas as pd
from xpinyin import  Pinyin
p=Pinyin()
sch=r'C:\Users\litong\Desktop\pass分工\工作簿1.xlsx'
sch=pd.DataFrame(pd.read_excel(sch))
person=sch.iloc[:,3].values
d={}
for i in person:
    d[i]=d.get(i,0)+1
print(d)
d=sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in d:
    print(i)

