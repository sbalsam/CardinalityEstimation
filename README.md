# Cardinality Estimation

This project consists of three parts:

- Python implementations for FM85, HLL
- Jupyter notebook using the implementations
- A review paper describing the techniques

## Python implementations

Some simplifications have been made in these implementations that 
would not be desirable in real world applications, but Python being
a slow language would not be used in these cases anyway.

[FM85.py](FM85.py) is the implementation of Flajolet & Martin...

[HLL.py](HLL.py) is an implementation of Flajolet... As python does 
not use a fixed length for integers, I skipped over the representation
in memory with 5 Bits as used in the original paper. Instead, an 
array of integers of size m is used. These integers can be bigger
than 32 Bit. Since I was not interested in the memory consumption and
only looked at the results concerning the quality of the estimation,
this is a valid tradeoff.

## Jupyter Notebook

The Jupyter notebook ran be read [here](Cardinality.ipynb).

## Review paper

The review paper can be read [here](review/review.pdf).
