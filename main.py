import numpy as np
from PySurfaceFit.util import *
import PySurfaceFit.mls as mls

clothData3d=readFromClothObj("data/cloth1.obj")


def simplefit():
    X=clothData3d[:,0:2]
    U=clothData3d[:,2]
    mlsSolver=mls.mls(X,U)
    result=mlsSolver.fit(X)
    show3d(clothData3d,u"原始衣物")
    clothData3d[:,2]=result
    show3d(clothData3d,u"MLS拟合衣物")
    plt.show()

simplefit()