from DRV import FiniteDRV
from math import comb
#this code generates the pmf of some very important DRVs.
c = []
pxc = []
def BinomialDRV(n:int ,p: float) -> FiniteDRV: #Binomial DRV with n trials, and probability p.
    c = []
    pxc = []
    for i in range(0,n+1):
        c.append(i)
        pxc.append(comb(n,i)*(p**i)*((1-p)**(n-i)))
    return(FiniteDRV(c,pxc))
def BernoulliDRV(p:float) -> FiniteDRV:
    c = [0,1]
    pxc = [1-p,p]
    return(FiniteDRV(c,pxc))
def DiscreteUniformDRV(n:int) -> FiniteDRV:
    for i in range(1,n+1):
        c.append(i)
        pxc.append(1/n)
    return(FiniteDRV(c,pxc))

x = BinomialDRV(15,.4)
print(x.ExpectedValue)