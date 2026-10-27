## Checkerboard Pattern

**Difficulty**: Medium

**Problem Statement**
Given an integer `n`, print an `n x n` checkerboard using `*` and `#` such that adjacent cells (horizontally and vertically) always have different characters. The top-left cell must be `*`.

**Input Format**
A single integer `n`.

**Output Format**
`n` lines, each with `n` characters.

**Constraints**
- `1 <= n <= 100`

**Sample Input 0**
```
6
```

**Sample Output 0**
```
*#*#*#
#*#*#*
*#*#*#
#*#*#*
*#*#*#
#*#*#*
```

**Explanation 0**
For `n = 6` we print a 6-by-6 grid. The top-left cell is `*`. Any time we move one step left/right or up/down, the character flips to the other one. So odd rows start with `*` and alternate, and even rows start with `#` and alternate. This creates the usual checkerboard pattern.

---

## Elements Greater Than Range

**Difficulty**: Medium

**Problem Statement**
Given an array of `n` integers, count how many elements are strictly greater than the difference `max - min` of the array.

**Input Format**
- Line 1: an integer `n`.
- Line 2: `n` space-separated integers.

**Output Format**
A single integer - the count.

**Constraints**
- `1 <= n <= 10^5`

**Sample Input 0**
```
5
1 2 3 4 5
```

**Sample Output 0**
```
1
```

**Explanation 0**
Max is `5` and min is `1`, so the difference is `5 - 1 = 4`. Only `5` is strictly greater than `4`, so the count is `1`.

**Sample Input 1**
```
5
4 5 6 7 8
```

**Sample Output 1**
```
4
```

**Explanation 1**
Max is `8` and min is `4`, so the difference is `8 - 4 = 4`. The elements strictly greater than `4` are `5, 6, 7, 8`, which is `4` elements, so the answer is `4`.

---



## Nth Prime Number

**Difficulty**: Hard

**Problem Statement**
Given `n`, print the `n`-th prime number (`1`-indexed, so the 1st prime is `2`).

**Input Format**
A single integer `n`.

**Output Format**
The `n`-th prime number.

**Constraints**
- `1 <= n <= 10^5`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
2
```

**Explanation 0**
The list of prime numbers starts `2, 3, 5, 7, 11, ...`. The 1st prime in this list is `2`.

**Sample Input 1**
```
5
```

**Sample Output 1**
```
11
```

**Explanation 1**
Counting primes: `2` (1st), `3` (2nd), `5` (3rd), `7` (4th), `11` (5th). So the 5th prime is `11`.

**Sample Input 2**
```
10000
```

**Sample Output 2**
```
104729
```

**Explanation 2**
If you list the first 10000 prime numbers in order, the last one in that list is `104729`.

---

## Sum Of Primes Up To N

**Difficulty**: Hard

**Problem Statement**
Given `n`, compute the sum of all prime numbers `p` with `p <= n`.

**Input Format**
A single integer `n`.

**Output Format**
A single integer - the sum.

**Constraints**
- `1 <= n <= 10^5`

**Sample Input 0**
```
20
```

**Sample Output 0**
```
77
```

**Explanation 0**
The primes up to `20` are `2, 3, 5, 7, 11, 13, 17, 19`. Adding them gives `2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77`.

**Sample Input 1**
```
2
```

**Sample Output 1**
```
2
```

**Explanation 1**
The only prime up to `2` is `2` itself, so the sum is `2`.

**Sample Input 2**
```
100000
```

**Sample Output 2**
```
454396537
```

**Explanation 2**
Adding every prime number from `2` up to `100000` gives `454396537`.

---

## Range Sum Queries

**Difficulty**: Hard

**Problem Statement**
Given an array of `n` integers and `q` queries, each query specifies a 1-indexed inclusive range `[l, r]`. For every query, print the sum of elements in that range on its own line.

**Input Format**
- Line 1: two integers `n` and `q`.
- Line 2: `n` space-separated integers - the array.
- Next `q` lines: two integers `l` and `r` per line.

**Output Format**
`q` lines, each containing the sum of the queried range.

**Constraints**
- `1 <= n <= 10^4`
- `1 <= q <= 10^4`
- `-10^9 <= element <= 10^9`
- `1 <= l <= r <= n`

**Sample Input 0**
```
5 3
1 2 3 4 5
2 4
1 5
3 5
```

**Sample Output 0**
```
9
15
12
```

**Explanation 0**
Array is `[1, 2, 3, 4, 5]` (1-indexed).
- Query `2 4`: sum of positions 2 to 4 is `2 + 3 + 4 = 9`.
- Query `1 5`: sum of the whole array is `1 + 2 + 3 + 4 + 5 = 15`.
- Query `3 5`: sum of positions 3 to 5 is `3 + 4 + 5 = 12`.

**Sample Input 1**
```
7 5
9 7 5 3 1 2 4
1 3
4 7
2 5
1 4
3 6
```

**Sample Output 1**
```
21
10
16
24
11
```

**Explanation 1**
Array is `[9, 7, 5, 3, 1, 2, 4]` (1-indexed).
- Query `1 3`: `9 + 7 + 5 = 21`.
- Query `4 7`: `3 + 1 + 2 + 4 = 10`.
- Query `2 5`: `7 + 5 + 3 + 1 = 16`.
- Query `1 4`: `9 + 7 + 5 + 3 = 24`.
- Query `3 6`: `5 + 3 + 1 + 2 = 11`.
