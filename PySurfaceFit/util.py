from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
import numpy as np

def readFromClothObj(path):
    aList = []
    flag=False;
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split(' ')  #去掉列表中每一个元素的换行符
            if line[0] == '#next':
                flag = True
            if line[0]=='v' and flag:
                listRow=[float(line[1]),float(line[2]),float(line[3])]
                aList.append(listRow)
    return np.array(aList,dtype="double")

def readFromBodyObj_(path):
    aList = []
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split(' ')  #去掉列表中每一个元素的换行符
            if line[0]=='v':
                listRow=[float(line[1]),float(line[2]),float(line[3]),float(line[4])]
                aList.append(listRow)
    return np.array(aList,dtype="double")

def readFromBodyObj(path):
    aList = []
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.strip('\n').split(' ')  #去掉列表中每一个元素的换行符
            if line[0]=='v':
                listRow=[float(line[1]),float(line[2]),float(line[3])]
                aList.append(listRow)
    return np.array(aList,dtype="double")


import matplotlib.pyplot as plt

def show3d(arrX3,title):
    if not hasattr(show3d, 'fig_count'):
        show3d.fig_count = 0

    show3d.fig_count += 2
    x = arrX3[:, 0]
    y = arrX3[:, 1]
    z = arrX3[:, 2]
    fig = plt.figure(show3d.fig_count)
    ax = plt.axes(projection='3d')
    ax.set_xlim(x.min() - 0.2, x.max() + 0.2)
    ax.set_ylim(y.min() - 0.2, y.max() + 0.2)
    #ax.set_zlim(z.min() - 0.2, z.max() + 0.2)
    #ax.set_zlim(-0.2704132, 0.376334)
    ax.set_zlim(-0.5, 0.5)


    ax.scatter(x, y, z,s=1)
    ax.set_title(title,fontsize=12,fontproperties=font_set)

def show2d(arrX2,title):
    if not hasattr(show2d, 'fig_count'):
        show2d.fig_count = 1

    show2d.fig_count += 2
    x = arrX2[:, 0]
    y = arrX2[:, 1]

    fig = plt.figure(show2d.fig_count)
    ax = plt.axes()
    ax.set_xlim(x.min() - 0.2, x.max() + 0.2)
    ax.set_ylim(y.min() - 0.2, y.max() + 0.2)
    ax.scatter(x, y,1)
    ax.set_title(title,fontsize=12,fontproperties=font_set)