"""
This document can be used to store a DRV. It automatically computes the SD, 
Var, and EV for a given DRV. It also runs some checks to make sure that what is
being put in is representative of a DRV. 

These DRVs are also finite, and unlike geometric DRVs, their is an integer number of possible outcomes.

If you get an assert error that points to this script, it is highly likely
the DRV inputted did not meet the following requirements:

The length of c and pxc was not equal.
pxc was not equal to one.



"""
from math import isclose
class FiniteDRV:
    ExpectedValue = 0
    Variance = 0
    StandardDeviation = 0
    def __init__(self,c: list,pxc: list) -> None: #creates two input lists
        assert(len(c) != 1 and len(pxc) !=1) #it's not a drv if it has one input
        assert(len(c)==len(pxc)) #assert that c and pxc are the same size
        #for i in pxc: #check that all probabilities in between 0 to 1
        #    assert(0<i<1)
        pxcsum = 0
        for i in pxc:
            pxcsum += i
        assert isclose(pxcsum, 1, rel_tol=1e-9)# check that all the probabilites add up to one
        for i in range(0,len(c)): #expected value calculation
            self.ExpectedValue += (c[i]*pxc[i])
        for i in range(0,len(c)): #variance calculation
            self.Variance += ((abs(c[i]-self.ExpectedValue)**2)*pxc[i]) 
        self.StandardDeviation = self.Variance**0.5 #cute 1 line without using math.sqrt



if __name__ == "__main__":
    c = [2,8,12]
    pxc= [1/5,1/2,3/10]
    x = FiniteDRV(c,pxc)
    print(x.ExpectedValue,x.Variance)