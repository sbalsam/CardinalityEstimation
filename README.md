# Cardinality Estimation

This project consists of three parts:

- A review paper describing the techniques
- Python implementations for FM85, HLL, LogLogBeta
- Jupyter notebook using the implementations

## Review paper

The review paper with a detailed description of all methods can be 
read [here](review/cardinalityEstimation.pdf).

## Python implementations

Some simplifications have been made in these implementations, that would not be
desirable in real world applications, but Python being a slow language would
not be used in these cases anyway. Here I am only interested in the efficiency
of the algorithm, not in the efficiency of the implementation. 

[fm85.py](fm85.py) is the implementation of the original Flajolet & Martin...

[hll.py](hll.py) is an implementation of Flajolet... As python does not use a
fixed length for integers, I skipped over the representation in memory with 5
Bits as used in the original paper. Instead, an array of integers of size m is
used. These integers can be bigger than 32 Bit. Since I was not interested in
the memory consumption and only looked at the results concerning the quality of
the estimation, this is a valid tradeoff.

Another difference to the original paper is, that I count the rightmost '1's
instead of the leftmost. This is again due to the way integers are stored in
Python. As we don't have a fixed length, an integer always starts with a '1'.
There are never 0-paddings on the left. This should also not be a problem, as
the probabilites of having consecutive '0's on the left or on the right of the
binary representation of integers should be the same, as long as the hash
function distributes uniformly. For simplicity, I used Python's build in hash()
function. The results indicate, that it should be good enough for my purpose.

[llBeta](llBeta.py) an implementation of the LogLog-Beta algorithm presented in
[LogLog-Beta and More: A New Algorithm for Cardinality Estimation Based on LogLog 
Counting](https://arxiv.org/pdf/1612.02284) by Jason Qin, Denys Kim, and Yumei 
Tung (2016). Again, the register is an array of integers instead of a 6 bit
or sparse representation, as I am not concerned with the memory efficiency here.

[hllTailCut.py](hllTailCut.py)
("Better with fewer bits: Improving the performance of cardinality estimation 
of large data streams - Qingjun Xiao, You Zhou, Shigang 
Chen")[https://www.cise.ufl.edu/~sgchen/Publications/XZC17.pdf]

[ehll.py](ehll.py) an implementation of the Extended HyperLogLog algorithm
(ExtendedHyperLogLog: Analysis of a new Cardinality Estimator - Tal Ohayon, 2021)[https://arxiv.org/pdf/2106.06525]

## Jupyter Notebook

The Jupyter notebook can be read [here](Cardinality.ipynb). It uses all of the
implemented methods to visualize their qualities and problems. I also used
the notebook to prepare the figures for the paper.

