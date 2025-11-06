# for hyperlog 
# check https://engineering.fb.com/2018/12/13/data-infrastructure/hyperloglog/
# https://pangaj.github.io/HyperLogLog/
# https://www.youtube.com/watch?v=ty9d7wEVTwc

import sys

num_hashes = 512
bitsets = [[]] * num_hashes

def resetBits():
    for i in range(0,num_hashes):
        bitsets[i] = [0] * 32 # 32 bit set

def fm85_query() -> int:
    result = 0
    for i in range(0,num_hashes):
        r = 0
        for idx, j in enumerate(bitsets[i]):
            if j == 0:
                r = idx
                break
        result += r
    return 2 **(result / num_hashes) / 0.77351
:
def fm85_add(run : int, item : str):
    maxsize = sys.maxsize
    item_hash = hash(item+str(run)) 
    binnum = int(maxsize / num_hashes);
    for i in range(0, num_hashes):
        positives = item_hash % ((maxsize + i) * 2  )
        hashval = (positives % binnum ) + (i * binnum)
        bit = 1
        count = 0
        while hashval >= bit:
            if hashval & bit:
                break
            bit <<= 1
            count += 1
        bitsets[i][count] = 1

if __name__ == "__main__":
    vals = []
    for run in range(1,30):
        resetBits()
        avg = 0
        num = 0
        k = 0
        for i in range(1,10000):
            fm85_add(run, "item"+str(i))
            if i % 1000 == 0:
                if run == 1:
                    vals.append(0)
                num += 1
                res1 = fm85_query()
                print(f"{i} {int(res1)} - { abs(int(res1) / i)  }")
                vals[k] += res1 / i 
                k += 1
        print("-------")
    print(vals)
    globalAvg = 0
    for i in vals:
        print( (i / 30) - 1)
        globalAvg += ((i/30)-1)
    print("===================")
    print(globalAvg/30)
