import numpy as np
import math

class mls:
    def __init__(self,X,U):
        self.s_max=0.30
        self.k=3
        downSample=30
        self.X_=X[0::downSample,:]
        self.U_=U[0::downSample]

        self.n =X.shape[0]
        self.n_ = self.X_.shape[0]

        self.PX_=np.zeros((self.k,self.n_))
        for i in range(self.n_):
            self.PX_[:, i] = self.P(self.X_[i, :]).T


    def P(self,x):
        return np.array([[1,x[0],x[1],
                             #x[0]**2,x[0]*x[1],x[1]**2
                             #,x[0]**3,x[0]**2*x[1],x[1]**2*x[0],x[1]**3,
                             #x[0] ** 4, x[0] ** 3 * x[1],x[0] ** 2 * x[1]**2 ,x[1] ** 3 * x[0], x[1] ** 3,
                         ]]).T
    def Gauss(self,d):
        beta = 4;
        b2 = beta ** 2
        eb2 = math.exp(-beta ** 2)
        r2 = d ** 2
        w = (math.exp(-b2 * r2) - eb2) / (1.0 - eb2);
        return w

    def u(self,xi):
        w=np.zeros(self.n_)
        for i in range(self.n_):
            r=(xi-self.X_[i,:])/self.s_max
            w[i]=self.Gauss(r[0])*self.Gauss(r[1])
        w=np.diag(w)
        G=np.matmul(np.matmul(self.PX_,w),self.PX_.T)
        Ginv=np.linalg.inv(G)
        Nxi=np.matmul(np.matmul(np.matmul(self.P(xi).T,Ginv),self.PX_,),w)
        uxi=np.matmul(Nxi,self.U_.T)
        return uxi


    #这个有问题
    def getDownSample(self):
        ret=np.zeros((self.X_.shape[0],self.X_.shape[1]+1))
        ret[:,0:2]=self.X_
        ret[:,2]=self.U_
        return ret

    def fit(self,X):
        n=X.shape[0]
        fittedU=np.zeros(n)
        for i in range(n):
            fittedU[i]=self.u(X[i,:])
        return fittedU


