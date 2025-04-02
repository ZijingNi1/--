import pandas as pds
import re
def fz(i,jz):
    if (jz == 0):
        if (re.search(r"第[一二三四五六七八九十]{1,3}章", i)):
            i = i.split('章')
            ls.append(i[1][:-1])
        elif (re.search(r"第[一二三四五六七八九十]{1,2}节", i)):
            if (len(ls) == 0):
                ls.append('')
            i = i.split('节')
            ls.append(i[1][:-1])
        elif (re.search(r"[一二三四五六七八九十]{1,2}、", i)):
            if (len(ls) == 0):
                ls.extend(['']*2)
            i = i.split('、')
            ls.append(i[1][:-1])
        elif (re.search(r"【\w*概述】", i)):
            if(len(ls)==1):
                ls.extend([ls[0]]*2)
            elif(len(ls)==2):
                ls.append(ls[1])
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 1
        elif (re.search(r"【临床\w+】", i)):
            if(len(ls)==1):
                ls.extend([ls[0]]*2)
            elif(len(ls)==2):
                ls.append(ls[1])
            ls.append('')
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 2
        elif (re.search(r"【诊断\w*】", i)):
            if(len(ls)==1):
                ls.extend([ls[0]]*2)
            elif(len(ls)==2):
                ls.append(ls[1])
            ls.extend([''] * 2)
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 3
    elif (jz == 1):
        if (len(ls)==3):
            ls.append(i)
        elif (re.search(r"【诊断\w*】", i)):
            ls.append('')
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 3
        elif (re.search(r"第[一-龥]{1,2}节", i)):
            jz = 6
        elif(re.search(r"【临床表现】", i)):
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 2
        elif (re.search(r"【治疗\w*】", i)):
            ls.extend([''] * 2)
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 4
        else:
            ls[3] += i
    elif (jz == 2):
        if (len(ls) == 4):
            ls.append(i)
        elif (re.search(r"【诊断\w*】", i)):
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 3
        elif (re.search(r"【治疗\w*】", i)  or re.search(r"【处理原则】",i)):
            ls.append('')
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 4
        else:
            ls[4] += i
    elif (jz == 3):
        if (len(ls) == 5):
            ls.append(i)
        elif (re.search(r"【\w*治疗\w*】", i)):
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 4
        elif(re.search(r"第[一-龥]{1,3}章", i)
             or re.search(r"第[一-龥]{1,2}节", i)
             or re.search(r"[一二三四五六七八九十]{1,2}、", i)):
            ls.append('')
            jz=5
        else:
            ls[5] += i
    elif (jz == 4):
        if (len(ls) == 6):
            ls.append(i)
        elif(re.search(r"第[一-龥]{1,3}章", i)
             or re.search(r"第[一-龥]{1,2}节", i)
             or re.search(r"[一二三四五六七八九十]{1,2}、", i)):
            jz=5
        else:
            ls[6] += i
    return jz
zhang=[];jie=[];bm=[];gs=[];lcbx=[];zdyd=[];zlyz=[];ls=[]
#输入路径，请自行更改
with open(r'D:\常用\11.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
data = [item for item in data if item != "\n"]
data=[s.replace(' ', '') for s in data]
jz=0
for i in data:
    #下条代码解除注释后可以查看读取到哪条出错
    #print(i)
    pd=fz(i,jz)
    if(pd==6):
        jz = 0
        tzhang = ls[0]
        ls.clear()
        ls.append(tzhang)
        fz(i, jz)
    elif(pd!=5):
        jz = pd
    else:
        jz=0
        zhang.append(ls[0])
        jie.append(ls[1])
        bm.append(ls[2])
        gs.append(ls[3])
        lcbx.append(ls[4])
        zdyd.append(ls[5])
        zlyz.append(ls[6])
        ls.clear()
        fz(i,jz)
if(len(ls)!=7):
    ls.append('')
zhang.append(ls[0])
jie.append(ls[1])
bm.append(ls[2])
gs.append(ls[3])
lcbx.append(ls[4])
zdyd.append(ls[5])
zlyz.append(ls[6])
df = pds.DataFrame({'章': zhang,'节':jie,'病名':bm,'概述':gs,'临床表现':lcbx,'诊断要点':zdyd,'治疗原则':zlyz})
#输出路径，请自行更改
df.to_excel('D:\常用\测试.xlsx', sheet_name='Sheet1', index=False)