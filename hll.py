import numpy as np

# -*- coding: utf-8 -*-
""" 
Implementation of an algorithm to estimate the number 
of distinct items in a stream as described in 
"Probabitistic Counting Algorithms for Data Base 
Applications" by Flajolet and Martin, 1985.
"""
class HLL:

    def __init__(self, bins: int):
        self.phi: float = 0.77351            # The magic number
        self.nmap: int = bins                # How many bins
        self.bitsets = [[]] * self.nmap # The pseudo - bitmap to store data
        self.resetBits()

    def resetBits(self):
        """Helper function to reset bits between experiments
        """
        for i in range(0, self.nmap):
            self.bitsets[i] = [0] * 32  # 32 bit set should be enough

    def query(self) -> int:
        """Returns an estimation of the number of items
        """
        result: int = 0
        for i in range(0,self.nmap):
            r: int = 0
            for idx, j in enumerate(self.bitsets[i]):
                if j == 0:
                    r = idx
                    break
            result += (r)
        return int(self.nmap / self.phi * 2 **(result / self.nmap))

    def rho(value):
        """returns the position of the rightmost 1-bit
           rho(1)=1, rho(0001)=4 
        """
        bit: int = 1
        count: int = 0
        while value >= bit:
            if value & bit:
                break
            bit <<= 1
            count += 1
        return count


    def add(self, item : str):
        """Adds an item to the estimator
        """
        h: int = hash(item) % (9999999999999)
        bin_num: int = h % self.nmap
        hashval: int = int(h / self.nmap)
        count = rho(hashval)
        self.bitsets[bin_num][count] = 1

if __name__ == "__main__":
    assert(rho(int('01010101'))==1)
    assert(rho(int('00101000'))==4)
    runs = 30
    vals = []
    hll = HLL(16)
    testvalues = np.logspace(0, 6, num=200, dtype=int)
    print(testvalues)
    for run in range(1,runs+1):
        fm85.resetBits()
        avg = 0
        num = 0
        k = 0
        for i in range(1,100000):
            hll.add("item"+str(i)+str(run))
            if i in testvalues:
                if run == 1:
                    vals.append(0)
                num += 1
                res1 = hll.query()
                print(f"{i} {res1} - { res1 / i }")
                vals[k] += res1 / i 
                k += 1
        print("-------")
    globalAvg = 0
    for i in vals:
        print( (i / runs) - 1)
        globalAvg += ((i/runs)-1)
    print("===================")
    print(globalAvg/runs)
