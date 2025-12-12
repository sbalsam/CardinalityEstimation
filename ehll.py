import math
import numpy as np

# -*- coding: utf-8 -*-
""" 
Implementation of the Extended HyperLogLog algorithm to estimate the number 
of distinct items in a stream. 
"""
class EHLL:

    def __init__(self, bins: int):
        self.m: int = bins                          # How many registers
        self.gamma: float = 0.962
        self.C1: list[int] = [0] * self.m   
        self.C2: list[int] = [1] * self.m
        self.resetBits()

    def resetBits(self):
        """Helper function to reset bits between experiments
        """
        for i in range(0, self.m):
            self.C1[i] = 0
            self.C2[i] = 1

    def query(self) -> float:
        """Returns an estimation of the number of items
        """
        result: int = 0
        for i in range(0,self.m):
            result += 2**(-self.C1[i]) + (1-self.C2[i]) * 2 **(-self.C1[i]+1)
        E: float = self.gamma * self.m * self.m * 1/result
        if E <= 5/2 * self.m:
            sumreg: int = self.C1.count(0)
            if sumreg > 0:
                return self.m * math.log(self.m/sumreg)
            else:
                return E
        return E

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
        j: int = h % self.m
        y: int = int(h / self.m)
        count: int = self.rho(y)
        if count == self.C1[j] + 1:
            self.C1[j] = count
            self.C2[j] = 1
        elif count > self.C1[j] + 1:
            self.C1[j] = count
            self.C2[j] = 0
        elif count == self.C1[j] - 1 and self.C2[j] == 0:
            self.C2[j] = 1

if __name__ == "__main__":
    hll = EHLL(256)
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
