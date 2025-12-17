# Factorial – Quick Revision

## Problem
Find factorial of a number `n`.


Example:
- `5! = 120`

---

## Approach 1: Iterative
- Multiply numbers from `2` to `n`

Time: O(n)

Space: O(1)

## Approach 2: Recursive

Base case: 1! = 1

Recursive case: n! = n × (n−1)!

Time: O(n)

Space: O(n) (call stack)