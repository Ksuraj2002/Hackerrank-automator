# Midterm constraint bumps

## Elements Greater Than Range
**Problem Statement**
Given an array of `n` integers, count how many elements are strictly greater than the difference `max - min` of the array.

**Input Format**
- Line 1: an integer `n`.
- Line 2: `n` space-separated integers.

**Constraints**
- `1 <= n <= 10^5`
- `-10^9 <= element <= 10^9`

**Output Format**
A single integer - the count.

## Sum Of Primes Up To N
**Problem Statement**
Given `n`, compute the sum of all prime numbers `p` with `p <= n`.

**Input Format**
A single integer `n`.

**Constraints**
- `1 <= n <= 10^7`

**Output Format**
A single integer - the sum.

## Range Sum Queries 3
**Problem Statement**
Given an array of `n` integers and `q` queries, each query specifies a 1-indexed inclusive range `[l, r]`. For every query, print the sum of elements in that range on its own line.

**Input Format**
- Line 1: two integers `n` and `q`.
- Line 2: `n` space-separated integers - the array.
- Next `q` lines: two integers `l` and `r` per line.

**Constraints**
- `1 <= n <= 10^5`
- `1 <= q <= 10^5`
- `-10^9 <= element <= 10^9`
- `1 <= l <= r <= n`

**Output Format**
`q` lines, each containing the sum of the queried range.
