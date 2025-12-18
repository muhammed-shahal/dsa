# Trailing Zeros in Factorial – Quick Revision

## Problem
Count number of trailing zeros in `n!`.

Trailing zeros are formed by factors of **10 = 2 × 5**.  
Since there are more `2`s than `5`s, count number of `5`s.

---

## Approach: Count Powers of 5
- Count how many times `5` divides numbers from `1` to `n`