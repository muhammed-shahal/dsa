# PRIME NUMBER CHECK – REVISION NOTES

## Problem Statement
Given a number n, check whether it is a prime number.
A prime number is a number greater than 1 that is divisible only by 1 and itself.

## Examples
11 → Prime
10 → Not Prime
2 → Prime
1 → Not Prime
9 → Not Prime

## Approach 1: Basic Prime Check

Check divisibility from 2 up to square root of n

If any number divides n, it is not prime

Simple and easy to understand

Works well for small numbers

## Approach 2: Efficient Prime Check

Handle special cases like 1, 2, and 3 first

Remove even numbers and multiples of 3

Check only numbers of the form 6k ± 1

Reduces unnecessary checks

Faster for large numbers

## Time Complexity
Basic approach: O(√n)
Efficient approach: O(√n) but with fewer checks, so faster in practice