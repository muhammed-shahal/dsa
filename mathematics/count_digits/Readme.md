# Count Digits in a Number – Quick Revision

## Problem
Find number of digits in a positive integer `n`.

---

## Approach 1: Loop (Safe)
- Repeatedly divide by `10`
- Count divisions until number > 0


Time: O(digits)

## Approach 2: Logarithm (Fast)

Formula: digits = int(log10(n)) + 1

Time: O(1)