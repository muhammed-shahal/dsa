# GCD AND LCM (EUCLIDEAN METHOD) – REVISION NOTES

## Problem Statement
Given two numbers a and b:

Find the GCD (Greatest Common Divisor)

Find the LCM (Least Common Multiple)

GCD is the largest number that divides both numbers exactly.
LCM is the smallest number that is a multiple of both numbers.

## Examples

GCD Examples
GCD of 4 and 6 → 2
GCD of 100 and 200 → 100
GCD of 7 and 13 → 1

LCM Examples
LCM of 4 and 6 → 12
LCM of 12 and 15 → 60
LCM of 2 and 8 → 8

## Approach for GCD (Euclidean Algorithm – Modulus)

If b is 0, a is the GCD

Otherwise, replace (a, b) with (b, a mod b)

Repeat until remainder becomes 0

Final non-zero value is the GCD

**Key Idea**
GCD(a, b) = GCD(b, a % b)

## Approach for LCM

First compute GCD of the two numbers

Use the formula:
LCM = (a × b) / GCD