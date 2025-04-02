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
        elif (re.search(r"一、概述", i) or re.search(r"一、定义", i) or re.search(r"一、病因", i)
              or re.search(r"一、临床表现", i) or re.search(r"一、诊断", i)):
            ls.extend([ls[1]] * 2)
            jb= 1
            if (re.search(r"一、概述", i) or re.search(r"一、定义", i) or re.search(r"一、病因", i)):
                jz = 1
            elif (re.search(r"一、临床表现", i)):
                ls.append('')
                jz = 2
            else:
                ls.extend([''] * 2)
                jz = 3
        elif (re.search(r"[一二三四五六七八九十]{1,2}、", i)):
            if (len(ls) == 0):
                ls.extend(['']*2)
            i = i.split('、')
            ls.append(i[1][:-1])
        elif (re.search(r"\(一\)概述", i) or re.search(r"\(一\)定义", i) or re.search(r"\(一\)病因", i)
              or re.search(r"\(一\)临床表现", i) or re.search(r"\(一\)诊断", i)):
            ls.append(ls[2])
            jb=2
            if(re.search(r"\(一\)概述", i) or re.search(r"\(一\)定义", i) or re.search(r"\(一\)病因", i)):
                jz=1
            elif(re.search(r"\(一\)临床表现", i)):
                ls.append('')
                jz=2
            else:
                ls.extend(['']*2)
                jz=3
        elif (re.search(r"\([一二三四五六七八九十]+\)", i)):
            if (len(ls) == 0):
                ls.extend(['']*3)
            i = i.split(')')
            ls.append(i[1][:-1])
        elif (re.search(r"1.概述", i) or re.search(r"1.定义", i) or re.search(r"1.病因", i)
              or re.search(r"1.临床表现", i) or re.search(r"1.诊断", i)):
            jb=3
            if(re.search(r"1.概述", i)):
                ls.append(i.split('1.概述')[1])
                jz=1
            elif (re.search(r"1.定义", i)):
                ls.append(i.split('1.定义')[1])
                jz=1
            elif (re.search(r"1.病因", i)):
                ls.append(i.split('1.病因')[1])
                jz=1
            elif(re.search(r"1.临床表现", i)):
                ls.append('')
                ls.append(i.split('1.临床表现')[1])
                jz=2
            else:
                ls.extend(['']*2)
                ls.append(i.split('1.诊断')[1])
                jz=3
    elif (jz == 1):
        if (len(ls)==4):
            ls.append(i)
        elif (re.search(r"[一二三四五六七八九十]+、诊断\w*", i)
              or re.search(r"\([一二三四五六七八九十]+\)诊断\w*",i)
              or re.search(r"[1-9]+.诊断\w*",i)):
            ls.append('')
            if('.诊断' in i):
                ls.append(i.split('.诊断')[1])
            jz = 3
        elif (re.search(r"第[一二三四五六七八九十]{1,2}节", i)):
            jz = 6
        elif(re.search(r"[一二三四五六七八九十]+、临床表现\w*", i)
              or re.search(r"\([一二三四五六七八九十]+\)临床表现\w*",i)
              or re.search(r"[1-9]+.临床表现\w*",i)):
            if ('.临床表现' in i):
                ls.append(i.split('.临床表现')[1])
            jz = 2
        elif (re.search(r"[一二三四五六七八九十]+、治疗\w*", i)
            or re.search(r"\([一二三四五六七八九十]+\)治疗\w*", i)
            or re.search(r"[1-9]+.治疗\w*", i)
            or re.search(r"[一二三四五六七八九十]+、防治原则\w*", i)
            or re.search(r"\([一二三四五六七八九十]+\)防治原则\w*", i)
            or re.search(r"[1-9]+.防治原则\w*", i)):
            if ('.治疗' in i):
                ls.append(i.split('.治疗')[1])
            if ('.防治原则' in i):
                ls.append(i.split('.防治原则')[1])
            ls.extend([''] * 2)
            jz = 4
        else:
            ls[4] += i
    elif (jz == 2):
        if (len(ls) == 5):
            ls.append(i)
        elif (re.search(r"[一二三四五六七八九十]+、诊断\w*", i)
                  or re.search(r"\([一二三四五六七八九十]+\)诊断\w*", i)
                  or re.search(r"[1-9]+.诊断\w*", i)):
            if ('.诊断' in i):
                ls.append(i.split('.诊断')[1])
            jz = 3
        elif (re.search(r"[一二三四五六七八九十]+、治疗\w*", i)
                  or re.search(r"\([一二三四五六七八九十]+\)治疗\w*", i)
                  or re.search(r"[1-9]+.治疗\w*", i)
                  or re.search(r"[一二三四五六七八九十]+、防治原则\w*", i)
                  or re.search(r"\([一二三四五六七八九十]+\)防治原则\w*", i)
                  or re.search(r"[1-9]+.防治原则\w*", i)):
            if ('.治疗' in i):
                ls.append(i.split('.治疗')[1])
            if ('.防治原则' in i):
                ls.append(i.split('.防治原则')[1])
            ls.append('')
            jz = 4
        else:
            ls[5] += i
    elif (jz == 3):
        if (len(ls) == 6):
            ls.append(i)
        elif (re.search(r"[一二三四五六七八九十]+、治疗\w*", i)
                  or re.search(r"\([一二三四五六七八九十]+\)治疗\w*", i)
                  or re.search(r"[1-9]+.治疗\w*", i)
                  or re.search(r"[一二三四五六七八九十]+、防治原则\w*", i)
                  or re.search(r"\([一二三四五六七八九十]+\)防治原则\w*", i)
                  or re.search(r"[1-9]+.防治原则\w*", i)):
            if ('.治疗' in i):
                ls.append(i.split('.治疗')[1])
            if ('.防治原则' in i):
                ls.append(i.split('.防治原则')[1])
            jz = 4
        elif(re.search(r"第[一二三四五六七八九十]{1,3}章", i)
             or re.search(r"第[一二三四五六七八九十]{1,2}节", i)
             or (re.search(r"[一二三四五六七八九十]{1,2}、", i) and jb>=2)
            or (re.search(r"\([一二三四五六七八九十]+\)",i) and jb>=3)):
            ls.append('')
            jz=5
        else:
            ls[6] += i
    elif (jz == 4):
        if (len(ls) == 7):
            ls.append(i)
        elif (re.search(r"第[一二三四五六七八九十]{1,3}章", i)
            or re.search(r"第[一二三四五六七八九十]{1,2}节", i)
            or (re.search(r"[一二三四五六七八九十]{1,2}、", i) and jb >= 2)
            or (re.search(r"\([一二三四五六七八九十]+\)", i) and jb >= 3)):
            jz=5
        else:
            ls[7] += i
    return jz
zhang=[];jie=[];xj=[];bm=[];gs=[];lcbx=[];zdyd=[];zlyz=[];ls=[]
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
        jz =jb=0
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
        bm.append(ls[3])
        gs.append(ls[4])
        lcbx.append(ls[5])
        zdyd.append(ls[6])
        zlyz.append(ls[7])
        ls.clear()
        fz(i,jz)
if(len(ls)!=7):
    ls.append('')
zhang.append(ls[0])
jie.append(ls[1])
xj.append(ls[2])
bm.append(ls[3])
gs.append(ls[4])
lcbx.append(ls[5])
zdyd.append(ls[6])
zlyz.append(ls[7])
df = pds.DataFrame({'章': zhang,'节':jie,'小节':xj,'病名':bm,'概述':gs,'临床表现':lcbx,'诊断要点':zdyd,'治疗原则':zlyz})
#输出路径，请自行更改
df.to_excel('D:\常用\测试.xlsx', sheet_name='Sheet1', index=False)