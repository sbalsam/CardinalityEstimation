import math
import numpy as np

# -*- coding: utf-8 -*-
""" 
Implementation of the LogLogBeta algorithm to estimate the number 
of distinct items in a stream.

Some of the precalculated values for beta are taken from the Go implementation
https://github.com/axiomhq/hyperloglog/tree/main
"""
class LLBeta:

    # The precalculated coefficient for different values of m
    p = {}
    p[16] = [-0.582581413904517,-1.935300357560050,11.079323758035073,-22.131357446444323,
            22.505391846630037,-12.000723834917984,3.220579408194167,-0.342225302271235]
    p[32] = [-0.7518999460733967,-0.9590030077748760,5.5997371322141607,-8.2097636999765520,
            6.5091254894472037,-2.6830293734323729,0.5612891113138221,-0.0463331622196545]
    p[64] = [29.8257900969619634,-31.3287083337725925,-10.5942523036582283,-11.5720125689099618,
            3.8188754373907492,-2.4160130328530811,0.4542208940970826,-0.0575155452020420]
    p[128] = [2.8102921290820060,-3.9780498518175995,1.3162680041351582,-3.9252486335805901,
            2.0080835753946471,-0.7527151937556955,0.1265569894242751,-0.0109946438726240]
    p[256] = [1.00633544887550519,-2.00580666405112407,1.64369749366514117,-2.70560809940566172,
            1.39209980244222598,-0.46470374272183190,0.07384282377269775,-0.00578554885254223]
    p[512] = [-0.09415657458167959,-0.78130975924550528,1.71514946750712460,-1.73711250406516338,
            0.86441508489048924,-0.23819027465047218,0.03343448400269076,-0.00207858528178157]
    p[1024] = [-0.25935400670790054,-0.52598301999805808,1.48933034925876839,-1.29642714084993571,
             0.62284756217221615,-0.15672326770251041,0.02054415903878563,-0.00112488483925502]
    p[2048] = [-4.32325553856025e-01,-1.08450736399632e-01,6.09156550741120e-01,-1.65687801845180e-02,
             -7.95829341087617e-02,4.71830602102918e-02,-7.81372902346934e-03,5.84268708489995e-04]
    p[4096] = [-3.84979202588598e-01,1.83162233114364e-01,1.30396688841854e-01,7.04838927629266e-02,
             -8.95893971464453e-03,1.13010036741605e-02,-1.94285569591290e-03,2.25435774024964e-04]
    p[8192] = [-0.41655270946462997,-0.22146677040685156,0.38862131236999947,0.45340979746062371,
             -0.36264738324476375,0.12304650053558529,-0.01701540384555510,0.00102750367080838]
    p[16384] = [-3.71009760230692e-01,9.78811941207509e-03,1.85796293324165e-01,2.03015527328432e-01,
             -1.16710521803686e-01,4.31106699492820e-02,-5.99583540511831e-03,4.49704299509437e-04]
    p[32768] = [-0.38215145543875273,-0.89069400536090837,0.37602335774678869,0.99335977440682377,
             -0.65577441638318956,0.18332342129703610,-0.02241529633062872,0.00121399789330194]
    p[65536] = [-0.37331876643753059,-1.41704077448122989,0.40729184796612533,1.56152033906584164,
             -0.99242233534286128,0.26064681399483092,-0.03053811369682807,0.00155770210179105]
    p[131072] = [-0.36775502299404605,0.53831422351377967,0.76970289278767923,0.55002583586450560,
             -0.74575588261146941,0.25711835785821952,-0.03437902606864149,0.00185949146371616]
    p[262144] = [-0.36479623325960542,0.99730412328635032,1.55354386230081221,1.25932677198028919,
             -1.53325948209110163,0.47801042200056593,-0.05951025172951174,0.00291076804642205]

    def __init__(self, bins: int):
        self.m: int = bins                          # How many bins
        self.bits: list[int] = [0] * self.m # The pseudo - bitmap to store data
        self.resetBits()

    def alpha(self, m : int):
        if m == 16: 
            return 0.673
        if m == 32: 
            return 0.697
        if m == 64:
            return 0.789
        return 0.7213 / (1 + 1.079/self.m)    # for m >= 128

    def resetBits(self):
        """Helper function to reset bits between experiments
        """
        for i in range(0, self.m):
            self.bits[i] = 0  

    def beta(self, m: int, z: int) -> float:
        """Bias minimizer function 
        """
        params = LLBeta.p[m]
        zl = math.log(z + 1)
        sum = params[0] * z
        for i in range(1,8):
            sum += params[i] * math.pow(zl,i)
        return sum

    def query(self) -> float:
        """Returns an estimation of the number of items
        """
        sum: int = 0
        for i in range(0,self.m):
            sum += 2**(-self.bits[i])
        z: int = self.bits.count(0)
        return self.alpha(self.m) * self.m * (self.m - z) / (self.beta(self.m, z) + sum)

    def rho(self, value: int) -> int:
        """returns the position of the rightmost 1-bit
           rho(1)=1, rho(1000)=4 
        """
        bit: int = 1
        count: int = 0
        while value >= bit:
            if value & bit:
                break
            bit <<= 1
            count += 1
        return count + 1

    def add(self, item : str):
        """Adds an item to the estimator
        """
        h: int = hash(item) % (9999999999999)
        bin_num: int = h % self.m
        hashval: int = int(h / self.m)
        count: int = self.rho(hashval)
        self.bits[bin_num] = max(self.bits[bin_num], count)


if __name__ == "__main__":
    hll = HLL(256)
    assert(hll.rho(int('01010101'))==1)
    assert(hll.rho(int('00101000'))==4)
    runs = 30
    vals = []
    testvalues = np.logspace(0, 5, num=200, dtype=int)
    print(testvalues)
    for run in range(1,runs+1):
        hll.resetBits()
        avg = 0
        num = 0
        k = 0
        for i in range(1,10000):
            hll.add("item"+str(i)+str(run))
            if i in testvalues:
                if run == 1:
                    vals.append(0)
                num += 1
                res1 = hll.query()
                print(f"{i} {int(res1)} - { res1 / i }")
                vals[k] += res1 / i 
                k += 1
        print("-------")
    globalAvg = 0
    for i in vals:
        print( (i / runs) - 1)
        globalAvg += ((i/runs)-1)
    print("===================")
    print(globalAvg/runs)
