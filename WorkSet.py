import xlrd
import pandas as pd
from xpinyin import  Pinyin

p=Pinyin()
worker=r'C:\Users\litong\Desktop\pass分工\psaas分工.xlsx'
ques=r'C:\Users\litong\Desktop\pass分工\问题流程角色与人员.xlsx'
person=r'C:\Users\litong\Desktop\pass分工\CMDB业务信息.xlsx'
resultPath =r'C:\Users\litong\Desktop\pass分工\result.xlsx'
#nonepro=pd.DataFrame(pd.read_excel(r'C:\Users\litong\Desktop\pass分工\未分工.xlsx'))
worker=pd.DataFrame(pd.read_excel(worker))
person=pd.DataFrame(pd.read_excel(person))
production=worker['产品名称']
cpxf=worker['产品细分领域']
jkyz=worker['监控1组']

def one():
    for i in range(len(person)):
        if person.iloc[i,1] in production.values:
            person.loc[i,'4A审批人员']='('+p.get_pinyin(jkyz[production[production.values==person.iloc[i,1]].index].values[0],'')+')'+'('+jkyz[production[production.values==person.iloc[i,1]].index].values[0]+')'
        elif person.iloc[i,1] in cpxf.values:
            person.loc[i,'4A审批人员']='('+p.get_pinyin(jkyz[cpxf[cpxf.values==person.iloc[i,1]].index].values[0],'')+')'+'('+jkyz[cpxf[cpxf.values==person.iloc[i,1]].index].values[0]+')'

    print(person)
    person.to_excel(resultPath,index = False,na_rep = 0,inf_rep = 0)
def two(person,production,nonepro=[]):
    name=[]
    for i in range(len(person)):
        if person.iloc[i, 1] in production.values:
            pass
        elif person.iloc[i, 1] in cpxf.values:
            pass
        else:
            nonepro.append(person.iloc[i, 1])
            name.append(person.iloc[i,5])
    print([nonepro,name])
    nonepro=pd.DataFrame(list(map(list, zip(*[nonepro,name]))))

    nonepro.to_excel(r'C:\Users\litong\Desktop\pass分工\未分工.xlsx',index = False,na_rep = 0,inf_rep = 0)
def three(ques,work):
    ques = pd.DataFrame(pd.read_excel(ques))
    #ques.loc['监控一组调度人员']
    jkyz = worker['监控1组']
    production = worker['产品名称']

    for i in range(len(ques['应用系统'])):
        if ques.loc[i,'应用系统'] in production.values:
            ques.loc[i,'监控调度一组人员']=jkyz[production[production.values==ques.loc[i,'应用系统']].index].values[0]


    ques.to_excel(r'C:\Users\litong\Desktop\pass分工\问题联系人.xlsx',index = False,na_rep = 0,inf_rep = 0)

if __name__=="__main__":
    #one()
    #two(person,production)
    three(ques,worker)