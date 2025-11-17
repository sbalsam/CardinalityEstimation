# for hyperlog 
# check https://engineering.fb.com/2018/12/13/data-infrastructure/hyperloglog/
# https://pangaj.github.io/HyperLogLog/
# https://www.youtube.com/watch?v=ty9d7wEVTwc

import sys

phi = 0.77351
nmap =64
bitsets = [[]] * nmap

def resetBits():
    for i in range(0,nmap):
        bitsets[i] = [0] * 32 # 32 bit set

def fm85_query() -> int:
    result = 0
    for i in range(0,nmap):
        r = 0
        for idx, j in enumerate(bitsets[i]):
            if j == 0:
                r = idx
                break
        result += (r)
    return int(nmap / phi * (2 **(result / nmap)))

def fm85_add(run : int, item : str):
    maxsize = sys.maxsize
    item_hash = hash(item+str(run)) 
    # binnum = int(maxsize / nmap);
    positives = item_hash % (9999999999999)
    bin_num = positives % nmap
    div = positives / nmap
    hashval = int(div)
    bit = 1
    count = 0
    # print("----")
    # print(positives)
    # print(div)
    # print(hashval)
    # print(bin_num)
    # print(str(bin(hashval)))
    while hashval >= bit:
        if hashval & bit:
            break
        bit <<= 1
        count += 1
    # print(count)
    bitsets[bin_num][count] = 1

if __name__ == "__main__":
    runs = 40
    vals = []
    for run in range(1,runs+1):
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
        print( (i / runs) - 1)
        globalAvg += ((i/runs)-1)
    print("===================")
    print(globalAvg/runs)
