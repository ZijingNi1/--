import pandas as pds
import re
def fz(i,jz):
    global jb
    if (jz == 0):
        if (re.search(r"第[一二三四五六七八九十]{1,3}章", i)):
            i = i.split('章')
            ls.append(i[1][:-1])
        elif (re.search(r"第[一二三四五六七八九十]{1,2}节", i)):
            if (len(ls) == 0):
                ls.append('')
            i = i.split('节')
            ls.append(i[1][:-1])
            jb=1
        elif (re.search(r"[一二三四五六七八九十]{1,2}、", i)):
            if (len(ls) == 0):
                ls.extend(['']*2)
            i = i.split('、')
            ls.append(i[1][:-1])
            jb=2
        elif(re.search(r"\([一二三四五六七八九十]+\)", i)):
            if (len(ls) == 0):
                ls.extend(['']*3)
            i = i.split(')')
            ls.append(i[1][:-1])
            jb=3
        elif(re.search(r"[1-9]+.", i)):
            if (len(ls) == 0):
                ls.extend(['']*4)
            i = i.split('.')
            ls.append(i[1][:-1])
            jb=4
        elif (re.search(r"【\w*概述】", i)):
            if(len(ls)==2):
                ls.extend([ls[1]]*3)
            elif(len(ls)==3):
                ls.extend([ls[2]] * 2)
            elif (len(ls) == 4):
                ls.append(ls[3])
            jz = 1
        elif (re.search(r"【临床\w+】", i)):
            if(len(ls)==2):
                ls.extend([ls[1]]*3)
            elif(len(ls)==3):
                ls.extend([ls[2]] * 2)
            elif (len(ls) == 4):
                ls.append(ls[3])
            ls.append('')
            jz = 2
    elif (jz == 1):
        if (len(ls)==5):
            ls.append(i)
        elif (re.search(r"第[一-龥]{1,2}节", i)):
            jz = 6
        elif(re.search(r"【临床表现】", i)):
            jz = 2
        elif (re.search(r"【\w*治疗\w*】", i)):
            ls.extend([''] * 2)
            jz = 4
        else:
            ls[5] += i
    elif (jz == 2):
        if (len(ls) == 6):
            ls.append(i)
        elif (re.search(r"【\w*治疗\w*】", i)):
            ls.append('')
            if(i.split('】')[1]!=''):
                ls.append(i.split('】')[1])
            jz = 4
        else:
            ls[6] += i
    elif (jz == 4):
        if (len(ls) == 7):
            ls.append(i)
        elif (re.search(r"第[一二三四五六七八九十]{1,3}章", i)
                or re.search(r"第[一二三四五六七八九十]{1,2}节", i)
                or (re.search(r"[一二三四五六七八九十]{1,2}、", i) and jb >= 2)
                or (re.search(r"\([一二三四五六七八九十]+\)", i) and jb >= 3)
                or (re.match("[123456789]{1}.", i) and jb >= 4)):
            jz=5
        else:
            ls[7] += i
    return jz
zhang=[];jie=[];xj=[];xjj=[];bm=[];gs=[];lcbx=[];zlyz=[];ls=[]
#输入路径，请自行更改
with open(r'D:\常用\11.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
data = [item for item in data if item != "\n"]
data=[s.replace(' ', '') for s in data]
jz=jb=0
for i in data:
    #下条代码解除注释后可以查看读取到哪条出错
    #print(i)
    pd=fz(i,jz)
    if(pd==6):
        jz = jb=0
        tzhang = ls[0]
        ls.clear()
        ls.append(tzhang)
        fz(i, jz)
    elif(pd!=5):
        jz = pd
    else:
        jz=jb=0
        zhang.append(ls[0])
        jie.append(ls[1])
        xj.append(ls[2])
        xjj.append(ls[3])
        bm.append(ls[4])
        gs.append(ls[5])
        lcbx.append(ls[6])
        zlyz.append(ls[7])
        ls.clear()
        fz(i,jz)
if(len(ls)!=7):
    ls.append('')
zhang.append(ls[0])
jie.append(ls[1])
xj.append(ls[2])
xjj.append(ls[3])
bm.append(ls[4])
gs.append(ls[5])
lcbx.append(ls[6])
zlyz.append(ls[7])
df = pds.DataFrame({'大类': zhang,'小类':jie,'节':xj,'小节':xjj,'病名':bm,'概述':gs,'临床表现':lcbx,'治疗原则':zlyz})
#输出路径，请自行更改
df.to_excel('D:\常用\测试.xlsx', sheet_name='Sheet1', index=False)