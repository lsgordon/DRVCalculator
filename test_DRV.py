import math
class DRV:
    ExpectedValue = 0
    Variance = 0
    StandardDeviation = 0
    def __init__(self,c: list,pxc: list) -> None: #creates two input lists
        assert(len(c) != 1 and len(pxc) !=1) #it's not a drv if it has one input
        assert(len(c)==len(pxc)) #assert that c and pxc are the same size
        for i in pxc: #check that all probabilities in between 0 to 1
            assert(0<i<1)
        pxcsum = 0
        for i in pxc:
            pxcsum += i
        assert(pxcsum == 1) # check that all the probabilites add up to one
        for i in range(0,len(c)): #expected value calculation
            self.ExpectedValue += (c[i]*pxc[i])
        for i in range(0,len(c)): #variance calculation
            self.Variance += ((abs(c[i]-self.ExpectedValue)**2)*pxc[i]) 
        self.StandardDeviation = self.Variance**0.5 #cute 1 line without using math.sqrt



#doctests
"""
>>> x.ExpectedValue
2.5
>>> x.Variance
1.25
"""

def test_DRV():
    c = [0,1,2]
    pxc = [.5,5/18,2/9]
    x = DRV(c,pxc)
    print(x.ExpectedValue,x.Variance)
    # Test case 1: Test with all probabilities equal
    c = [1, 2, 3, 4]
    pxc = [.25, .25, .25, .25]
    x = DRV(c, pxc)
    assert math.isclose(x.ExpectedValue, 2.5, rel_tol=1e-9)
    assert math.isclose(x.Variance, 1.25, rel_tol=1e-9)

    # Test case 2: Test with different probabilities
    c = [1, 2, 3, 4]
    pxc = [.1, .2, .3, .4]
    x = DRV(c, pxc)
    assert math.isclose(x.ExpectedValue, 3.0, rel_tol=1e-9)
    assert math.isclose(x.Variance, 1, rel_tol=1e-9)

    # Test case 3: Test with only one outcome, throws
    """c = [1]
    pxc = [1]
    x = DRV(c, pxc)
    assert math.isclose(x.ExpectedValue, 1, rel_tol=1e-9)
    assert math.isclose(x.Variance, 0, rel_tol=1e-9)
"""
    # Test case 4: Test with negative outcomes
    c = [-1, 0, 1]
    pxc = [.25, .5, .25]
    x = DRV(c, pxc)
    assert math.isclose(x.ExpectedValue, 0, rel_tol=1e-9)
    assert math.isclose(x.Variance, 1/2, rel_tol=1e-9)

if __name__ == "__main__":
    import doctest
    c =  [1,2,3,4]
    pxc = [.25,.25,.25,.25]
    x = DRV(c,pxc)
    doctest.testmod()
    test_DRV()
