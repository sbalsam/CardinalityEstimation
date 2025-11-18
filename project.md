Implementation of extended HHL (https://arxiv.org/pdf/2106.06525) mentioned in Better Cardinality Estimators for HyperLogLog, PCSA, and Beyond - 2023

An analysis of cpu usage is missing for this method.



# Introduction

# Literature

## History of HyperLogLog

# Methods

## HyperLogLog++

## LogLogBeta

# Experiments

# Conclusion



## Flajolet–Martin (Probabilistic counting with stocahstic averaging - PCSA)

- [Probabilistic Counting Algorithms for Data Base Applications - Flajolet, 1985](https://algo.inria.fr/flajolet/Publications/FlMa85.pdf)

## HyperLogLog (HLL)

- [HyperLogLog: the analysis of a near-optimal cardinality estimation algorithm -  Flajolet et al. 2007](https://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf)

- [Why Go Logarithmic if We Can Go Linear? Towards Effective Distinct Counting of Search Trafﬁc , 2008](https://dl.acm.org/doi/epdf/10.1145/1353343.1353418)

- [An Optimal Algorithm for the Distinct Elements Problem, Kane et al. 2010 ](https://www.cs.cmu.edu/afs/cs/user/dwoodruf/www/knw11.pdf)
- [New cardinality estimation algorithms for HyperLogLog sketches, Ertl 2017](https://oertl.github.io/hyperloglog-sketch-estimation-paper/paper/paper.pdf)
- [Better with Fewer Bits: Improving the Performance of Cardinality Estimation of Large Data Streams - Xiao et al. 2017](https://www.cise.ufl.edu/~sgchen/Publications/XZC17.pdf)
- [LogLog-Beta and More: A New Algorithm for Cardinality Estimation Based on LogLog Counting - Qin et al. 2016](https://arxiv.org/pdf/1612.02284)

- [Hyperloglog++, Heule et al. 2013](https://static.googleusercontent.com/media/research.google.com/no//pubs/archive/40671.pdf)
- [Better Cardinality Estimators for HyperLogLog, PCSA, and Beyond - 2023](https://dl.acm.org/doi/pdf/10.1145/3584372.3588680)



http://content.research.neustar.biz/blog/pcsa.html
https://arxiv.org/pdf/0801.3552


https://github.com/axiomhq/hyperloglog implementation is based on LogLog-Beta algorithm (https://arxiv.org/pdf/1612.02284)
instead of tailcut method [Better with Fewer Bits: Improving the Performance of Cardinality Estimation of Large Data Streams - Xiao et al. 2017](https://www.cise.ufl.edu/~sgchen/Publications/XZC17.pdf)

- [Near-Optimal Compression of Probabilistic Counting Sketches for Networking Applications , Scheuermann, 2007](https://publications.cs.hhu.de/library/Scheuermann2007b.pdf)
- [Back to the Future: an Even More Nearly Optimal Cardinality Estimation Algorithm, Lang 2017](https://arxiv.org/pdf/1708.06839)
- [All-Distances Sketches, Revisited: HIP Estimators for Massive Graphs Analysis, Cohen 2014](https://arxiv.org/abs/1306.3284)
- [Streamed Approximate Counting of Distinct Elements, Ting, 2014](https://research.facebook.com/publications/streamed-approximate-counting-of-distinct-elements/)
- Sliding window: https://arxiv.org/abs/1810.13132, https://hal.science/hal-00465313/file/sliding_HyperLogLog.pdf

- implementations:
	- python Hyperloglog : https://github.com/svpcom/hyperloglog

TimeLine:

- 1985 Flajolet & Martin
- 2007 HyperLogLog (Flajolet)
- 2007 Compressed FM85 (Scheuermann)
- 2013 Hyperloglog++ (Heule) (HyperLogLog in Practice: Algorithmic Engineering of a State of The Art Cardinality Estimation Algorithm (2013))
- 2014 Martingale Estimators (Ting)
- 2015 Historic Inverse Probability (Cohen)
- 2016 LogLogBeta (Qin)
- 2017 - Review: New cardinality estimation algorithms (Ertl)
- 2017 Back to the Future (Lang)
- 2023 ExtendedHyperLogLog (Ohayon)
- 2023 HLL-tailcut - Better with Fewer Bits (Xiao)
- 2023 Better Cardinality Estimators (Wang)
