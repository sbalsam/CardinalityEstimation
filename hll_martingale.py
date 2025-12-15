import math
import numpy as np

# -*- coding: utf-8 -*-
""" 
Implementation of the HyperLogLog algorithm to estimate the number 
of distinct items in a stream. 
"""
class HLL_Martingale:

    def __init__(self, bins: int):
        self.m: int = bins                          # How many bins
        # self.alpha: float = 0.7213 / (1 + 1.079/self.m)    # for m >= 128
        self.alpha = 0.7213/(1+1.079/self.m)
        self.bits: list[int] = [0] * self.m # The pseudo - bitmap to store data
        self.n : float = 1
        self.resetBits()

    def resetBits(self):
        """Helper function to reset bits between experiments
        """
        for i in range(0, self.m):
            self.bits[i] = 0 
        self.n = 1

    def query(self) -> float:
        """Returns an estimation of the number of items
        """
        return self.n

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

        result: float = 0
        if self.bits[bin_num] < count:
            for i in range(0,self.m):
                result += 2**(-self.bits[i])
            p =  1 / self.m * result
            self.n += (1 / p)

        self.bits[bin_num] = max(self.bits[bin_num], count)



if __name__ == "__main__":
    hll = HLL_Martingale(256)
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
    globalAvg:float = 0
    for i in vals:
        print( (i / runs) - 1)
        globalAvg += ((i/runs)-1)
    print("===================")
    print(globalAvg/runs)
