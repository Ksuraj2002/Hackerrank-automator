# DSA-101 Homework - Part 2 (Days 9 to 34)

Strict rule: titles and statements describe WHAT the problem is, not HOW to
solve it. No mention of any data structure, algorithm or language feature.

Content-duplicates collapsed to the first-occurring day; the sheet's later
copies (Days 12, 13, 14, 15, 16) reuse the earlier HackerRank challenge.
Theory drills (Day 19 HW2, Day 21 HW1) are not authored.

After uploading:
1. `venv\Scripts\python.exe tools\hr_mark_samples.py --md homework_part2_days9_34.md --apply`
2. Enable C++14, Java 8, Python 3 on each challenge in the admin UI.
3. `venv\Scripts\python.exe tools\hr_add_to_contest.py --md homework_part2_days9_34.md --apply`

---


## Homework: Greatest Common Divisor of Two Numbers
**Problem Statement**
Two non-negative integers `A` and `B` are given on a single line. Print their greatest common divisor `gcd(A, B)`.

By convention `gcd(0, 0) = 0` and `gcd(0, X) = X` for any positive `X`.

**Input Format**
A single line with two space-separated integers `A B`.

**Output Format**
A single line containing `gcd(A, B)`.

**Constraints**
- `0 <= A, B <= 10^9`

**Sample Input 0**
```
12 18
```

**Sample Output 0**
```
6
```

**Sample Input 1**
```
0 5
```

**Sample Output 1**
```
5
```

**Sample Input 2**
```
5 0
```

**Sample Output 2**
```
5
```

**Sample Input 3**
```
0 0
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
7 13
```

**Sample Output 4**
```
1
```

**Sample Input 5**
```
100 75
```

**Sample Output 5**
```
25
```

**Sample Input 6**
```
1000000000 999999999
```

**Sample Output 6**
```
1
```

**Sample Input 7**
```
48 36
```

**Sample Output 7**
```
12
```

**Sample Input 8**
```
1 1
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
270 192
```

**Sample Output 9**
```
6
```

**Tags**
Numbers, Basics

---

## Homework: Binary Representation of a Number
**Problem Statement**
A single integer `N` is given. Print its binary representation without any leading zeros.

For `N = 0` the answer is `0`. For a negative `N`, print `-` followed by the binary representation of `|N|`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing the binary representation.

**Constraints**
- `-10^18 <= N <= 10^18`

**Sample Input 0**
```
5
```

**Sample Output 0**
```
101
```

**Sample Input 1**
```
0
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
1
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
8
```

**Sample Output 3**
```
1000
```

**Sample Input 4**
```
255
```

**Sample Output 4**
```
11111111
```

**Sample Input 5**
```
1024
```

**Sample Output 5**
```
10000000000
```

**Sample Input 6**
```
-6
```

**Sample Output 6**
```
-110
```

**Sample Input 7**
```
1000000000
```

**Sample Output 7**
```
111011100110101100101000000000
```

**Sample Input 8**
```
-1
```

**Sample Output 8**
```
-1
```

**Sample Input 9**
```
123456789
```

**Sample Output 9**
```
111010110111100110100010101
```

**Tags**
Numbers, Basics

---

## Homework: List All Ordered Pairs (i, j) with i less than j
**Problem Statement**
A single integer `N` is given. List every ordered pair `(i, j)` of positive integers with `1 <= i < j <= N`.

Print each pair on its own line as two space-separated integers `i j`. List the pairs in increasing order of `i`, and for equal `i` in increasing order of `j`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
One pair per line. If `N < 2`, produce no output.

**Constraints**
- `1 <= N <= 200`

**Sample Input 0**
```
3
```

**Sample Output 0**
```
1 2
1 3
2 3
```

**Sample Input 1**
```
1
```

**Sample Output 1**
```

```

**Sample Input 2**
```
2
```

**Sample Output 2**
```
1 2
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
1 2
1 3
1 4
2 3
2 4
3 4
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
1 2
1 3
1 4
1 5
1 6
2 3
2 4
2 5
2 6
3 4
3 5
3 6
4 5
4 6
5 6
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
1 2
1 3
1 4
1 5
1 6
1 7
2 3
2 4
2 5
2 6
2 7
3 4
3 5
3 6
3 7
4 5
4 6
4 7
5 6
5 7
6 7
```

**Sample Input 7**
```
8
```

**Sample Output 7**
```
1 2
1 3
1 4
1 5
1 6
1 7
1 8
2 3
2 4
2 5
2 6
2 7
2 8
3 4
3 5
3 6
3 7
3 8
4 5
4 6
4 7
4 8
5 6
5 7
5 8
6 7
6 8
7 8
```

**Sample Input 8**
```
10
```

**Sample Output 8**
```
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
2 3
2 4
2 5
2 6
2 7
2 8
2 9
2 10
3 4
3 5
3 6
3 7
3 8
3 9
3 10
4 5
4 6
4 7
4 8
4 9
4 10
5 6
5 7
5 8
5 9
5 10
6 7
6 8
6 9
6 10
7 8
7 9
7 10
8 9
8 10
9 10
```

**Sample Input 9**
```
15
```

**Sample Output 9**
```
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
1 11
1 12
1 13
1 14
1 15
2 3
2 4
2 5
2 6
2 7
2 8
2 9
2 10
2 11
2 12
2 13
2 14
2 15
3 4
3 5
3 6
3 7
3 8
3 9
3 10
3 11
3 12
3 13
3 14
3 15
4 5
4 6
4 7
4 8
4 9
4 10
4 11
4 12
4 13
4 14
4 15
5 6
5 7
5 8
5 9
5 10
5 11
5 12
5 13
5 14
5 15
6 7
6 8
6 9
6 10
6 11
6 12
6 13
6 14
6 15
7 8
7 9
7 10
7 11
7 12
7 13
7 14
7 15
8 9
8 10
8 11
8 12
8 13
8 14
8 15
9 10
9 11
9 12
9 13
9 14
9 15
10 11
10 12
10 13
10 14
10 15
11 12
11 13
11 14
11 15
12 13
12 14
12 15
13 14
13 15
14 15
```

**Tags**
Basics, Numbers

---

## Homework: Print a Coordinate Grid
**Problem Statement**
Two positive integers `R` and `C` are given on a single line. Print an `R x C` grid of coordinate labels.

For every row `i` from `1` to `R` and column `j` from `1` to `C`, print the label `(i,j)` (parentheses, `i`, a comma, `j`, closing parenthesis). Labels within a row are separated by a single space. Rows are on separate lines. No trailing space at the end of any line.

**Input Format**
A single line containing two space-separated integers `R C`.

**Output Format**
`R` lines showing the grid of labels.

**Constraints**
- `1 <= R, C <= 20`

**Sample Input 0**
```
2 3
```

**Sample Output 0**
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
```

**Sample Input 1**
```
1 1
```

**Sample Output 1**
```
(1,1)
```

**Sample Input 2**
```
3 3
```

**Sample Output 2**
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

**Sample Input 3**
```
1 5
```

**Sample Output 3**
```
(1,1) (1,2) (1,3) (1,4) (1,5)
```

**Sample Input 4**
```
5 1
```

**Sample Output 4**
```
(1,1)
(2,1)
(3,1)
(4,1)
(5,1)
```

**Sample Input 5**
```
4 4
```

**Sample Output 5**
```
(1,1) (1,2) (1,3) (1,4)
(2,1) (2,2) (2,3) (2,4)
(3,1) (3,2) (3,3) (3,4)
(4,1) (4,2) (4,3) (4,4)
```

**Sample Input 6**
```
2 2
```

**Sample Output 6**
```
(1,1) (1,2)
(2,1) (2,2)
```

**Sample Input 7**
```
3 5
```

**Sample Output 7**
```
(1,1) (1,2) (1,3) (1,4) (1,5)
(2,1) (2,2) (2,3) (2,4) (2,5)
(3,1) (3,2) (3,3) (3,4) (3,5)
```

**Sample Input 8**
```
5 3
```

**Sample Output 8**
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
(4,1) (4,2) (4,3)
(5,1) (5,2) (5,3)
```

**Sample Input 9**
```
6 6
```

**Sample Output 9**
```
(1,1) (1,2) (1,3) (1,4) (1,5) (1,6)
(2,1) (2,2) (2,3) (2,4) (2,5) (2,6)
(3,1) (3,2) (3,3) (3,4) (3,5) (3,6)
(4,1) (4,2) (4,3) (4,4) (4,5) (4,6)
(5,1) (5,2) (5,3) (5,4) (5,5) (5,6)
(6,1) (6,2) (6,3) (6,4) (6,5) (6,6)
```

**Tags**
Basics, Numbers

---

## Homework: Sum of an Arithmetic Progression
**Problem Statement**
You are given three integers `A`, `D` and `N` on a single line. They describe an arithmetic progression whose first term is `A`, common difference is `D`, and which has `N` terms.

Print the sum of the `N` terms.

**Input Format**
A single line with three space-separated integers `A D N`.

**Output Format**
A single line containing the sum.

**Constraints**
- `-10^6 <= A, D <= 10^6`
- `1 <= N <= 10^4`

**Sample Input 0**
```
1 1 10
```

**Sample Output 0**
```
55
```

**Sample Input 1**
```
5 2 4
```

**Sample Output 1**
```
32
```

**Sample Input 2**
```
10 -1 5
```

**Sample Output 2**
```
40
```

**Sample Input 3**
```
0 0 100
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
-5 3 6
```

**Sample Output 4**
```
15
```

**Sample Input 5**
```
100 100 10
```

**Sample Output 5**
```
5500
```

**Sample Input 6**
```
1 0 1000
```

**Sample Output 6**
```
1000
```

**Sample Input 7**
```
7 -2 8
```

**Sample Output 7**
```
0
```

**Sample Input 8**
```
0 5 20
```

**Sample Output 8**
```
950
```

**Sample Input 9**
```
1000000 1 100
```

**Sample Output 9**
```
100004950
```

**Tags**
Numbers, Basics

---

## Homework: First N Fibonacci Numbers
**Problem Statement**
A single non-negative integer `N` is given. Print the first `N` Fibonacci numbers on a single line, separated by single spaces.

The sequence begins `0, 1, 1, 2, 3, 5, 8, ...` — the first two terms are `0` and `1`, and every later term is the sum of the two before it.

If `N` is `0`, print an empty line.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line with the first `N` Fibonacci numbers, space-separated.

**Constraints**
- `0 <= N <= 45`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
0
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
0 1
```

**Sample Input 2**
```
5
```

**Sample Output 2**
```
0 1 1 2 3
```

**Sample Input 3**
```
10
```

**Sample Output 3**
```
0 1 1 2 3 5 8 13 21 34
```

**Sample Input 4**
```
15
```

**Sample Output 4**
```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

**Sample Input 5**
```
20
```

**Sample Output 5**
```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
```

**Sample Input 6**
```
0
```

**Sample Output 6**
```

```

**Sample Input 7**
```
3
```

**Sample Output 7**
```
0 1 1
```

**Sample Input 8**
```
8
```

**Sample Output 8**
```
0 1 1 2 3 5 8 13
```

**Sample Input 9**
```
45
```

**Sample Output 9**
```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141 267914296 433494437 701408733
```

**Tags**
Numbers, Basics

---

## Homework: Floyd's Number Triangle
**Problem Statement**
A single positive integer `N` is given. Print Floyd's triangle of `N` rows.

Row `i` (1-indexed) contains `i` consecutive positive integers separated by single spaces, continuing the counting started in the previous rows.

For `N = 4` the triangle is:
```
1
2 3
4 5 6
7 8 9 10
```

**Input Format**
A single line containing one integer `N`.

**Output Format**
`N` lines forming Floyd's triangle.

**Constraints**
- `1 <= N <= 30`

**Sample Input 0**
```
4
```

**Sample Output 0**
```
1
2 3
4 5 6
7 8 9 10
```

**Sample Input 1**
```
1
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
2
```

**Sample Output 2**
```
1
2 3
```

**Sample Input 3**
```
3
```

**Sample Output 3**
```
1
2 3
4 5 6
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
```

**Sample Input 7**
```
10
```

**Sample Output 7**
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
```

**Sample Input 8**
```
15
```

**Sample Output 8**
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
67 68 69 70 71 72 73 74 75 76 77 78
79 80 81 82 83 84 85 86 87 88 89 90 91
92 93 94 95 96 97 98 99 100 101 102 103 104 105
106 107 108 109 110 111 112 113 114 115 116 117 118 119 120
```

**Sample Input 9**
```
20
```

**Sample Output 9**
```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31 32 33 34 35 36
37 38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63 64 65 66
67 68 69 70 71 72 73 74 75 76 77 78
79 80 81 82 83 84 85 86 87 88 89 90 91
92 93 94 95 96 97 98 99 100 101 102 103 104 105
106 107 108 109 110 111 112 113 114 115 116 117 118 119 120
121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136
137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153
154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171
172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190
191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210
```

**Tags**
Patterns, Numbers

---

## Homework: Half Diamond Pattern
**Problem Statement**
A single positive integer `N` is given. Print a half diamond of `*` characters with `2*N - 1` rows in total.

Row `i` for `i = 1..N` has exactly `i` `*` characters. Row `i` for `i = N+1..2N-1` has exactly `2N - i` `*` characters. No leading or trailing spaces on any row.

For `N = 3` the output is:
```
*
**
***
**
*
```

**Input Format**
A single line containing one integer `N`.

**Output Format**
`2*N - 1` lines forming the half diamond.

**Constraints**
- `1 <= N <= 30`

**Sample Input 0**
```
3
```

**Sample Output 0**
```
*
**
***
**
*
```

**Sample Input 1**
```
1
```

**Sample Output 1**
```
*
```

**Sample Input 2**
```
2
```

**Sample Output 2**
```
*
**
*
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
*
**
***
****
***
**
*
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
*
**
***
****
*****
****
***
**
*
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
*
**
***
****
*****
******
*****
****
***
**
*
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
*
**
***
****
*****
******
*******
******
*****
****
***
**
*
```

**Sample Input 7**
```
10
```

**Sample Output 7**
```
*
**
***
****
*****
******
*******
********
*********
**********
*********
********
*******
******
*****
****
***
**
*
```

**Sample Input 8**
```
15
```

**Sample Output 8**
```
*
**
***
****
*****
******
*******
********
*********
**********
***********
************
*************
**************
***************
**************
*************
************
***********
**********
*********
********
*******
******
*****
****
***
**
*
```

**Sample Input 9**
```
20
```

**Sample Output 9**
```
*
**
***
****
*****
******
*******
********
*********
**********
***********
************
*************
**************
***************
****************
*****************
******************
*******************
********************
*******************
******************
*****************
****************
***************
**************
*************
************
***********
**********
*********
********
*******
******
*****
****
***
**
*
```

**Tags**
Patterns, Basics

---

## Homework: Is a Year a Leap Year
**Problem Statement**
A single integer `Y` is given, representing a year in the Gregorian calendar. Print `Yes` if `Y` is a leap year, otherwise print `No`.

A year is a leap year when it is divisible by `4`, with the exception that years divisible by `100` are not leap years unless they are also divisible by `400`.

**Input Format**
A single line containing one integer `Y`.

**Output Format**
A single line containing `Yes` or `No`.

**Constraints**
- `1 <= Y <= 10000`

**Sample Input 0**
```
2024
```

**Sample Output 0**
```
Yes
```

**Sample Input 1**
```
2023
```

**Sample Output 1**
```
No
```

**Sample Input 2**
```
1900
```

**Sample Output 2**
```
No
```

**Sample Input 3**
```
2000
```

**Sample Output 3**
```
Yes
```

**Sample Input 4**
```
1600
```

**Sample Output 4**
```
Yes
```

**Sample Input 5**
```
2100
```

**Sample Output 5**
```
No
```

**Sample Input 6**
```
2400
```

**Sample Output 6**
```
Yes
```

**Sample Input 7**
```
1
```

**Sample Output 7**
```
No
```

**Sample Input 8**
```
4
```

**Sample Output 8**
```
Yes
```

**Sample Input 9**
```
100
```

**Sample Output 9**
```
No
```

**Tags**
Basics, Conditionals

---

## Homework: Prime Numbers up to N
**Problem Statement**
A single positive integer `N` is given. Print every prime number that is less than or equal to `N`, on a single line, in increasing order, separated by single spaces.

If there are no primes up to `N` (i.e. `N < 2`), print an empty line.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line with the primes up to `N`, space-separated.

**Constraints**
- `1 <= N <= 10^6`

**Sample Input 0**
```
10
```

**Sample Output 0**
```
2 3 5 7
```

**Sample Input 1**
```
1
```

**Sample Output 1**
```

```

**Sample Input 2**
```
2
```

**Sample Output 2**
```
2
```

**Sample Input 3**
```
20
```

**Sample Output 3**
```
2 3 5 7 11 13 17 19
```

**Sample Input 4**
```
50
```

**Sample Output 4**
```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```

**Sample Input 5**
```
100
```

**Sample Output 5**
```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

**Sample Input 6**
```
3
```

**Sample Output 6**
```
2 3
```

**Sample Input 7**
```
7
```

**Sample Output 7**
```
2 3 5 7
```

**Sample Input 8**
```
30
```

**Sample Output 8**
```
2 3 5 7 11 13 17 19 23 29
```

**Sample Input 9**
```
97
```

**Sample Output 9**
```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

**Tags**
Numbers, Basics

---

## Homework: Reduce a Fraction to Lowest Terms
**Problem Statement**
A fraction is given as two integers `P` (numerator) and `Q` (denominator) on a single line, separated by a space. It is guaranteed that `Q` is not `0`.

Print the fraction in its lowest terms as `p/q` where:

- `q` is positive (any minus sign is placed in front of `p`).
- `gcd(|p|, q) == 1`.

For `P = 0` the output must be `0/1`.

**Input Format**
A single line containing two space-separated integers `P Q`.

**Output Format**
A single line of the form `p/q` in the format described above.

**Constraints**
- `-10^9 <= P <= 10^9`
- `1 <= |Q| <= 10^9`, `Q != 0`

**Sample Input 0**
```
6 8
```

**Sample Output 0**
```
3/4
```

**Sample Input 1**
```
0 5
```

**Sample Output 1**
```
0/1
```

**Sample Input 2**
```
5 -10
```

**Sample Output 2**
```
-1/2
```

**Sample Input 3**
```
-3 -9
```

**Sample Output 3**
```
1/3
```

**Sample Input 4**
```
1 1
```

**Sample Output 4**
```
1/1
```

**Sample Input 5**
```
1000000000 500000000
```

**Sample Output 5**
```
2/1
```

**Sample Input 6**
```
7 13
```

**Sample Output 6**
```
7/13
```

**Sample Input 7**
```
-6 8
```

**Sample Output 7**
```
-3/4
```

**Sample Input 8**
```
0 1
```

**Sample Output 8**
```
0/1
```

**Sample Input 9**
```
12 -18
```

**Sample Output 9**
```
-2/3
```

**Tags**
Numbers, Math

---

## Homework: Count Positive Elements in an Array
**Problem Statement**
You are given an array of `N` integers. Print how many of them are strictly greater than `0`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the count.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5
1 -2 3 -4 5
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
3
0 0 0
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
1
7
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
1
-1
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
6
1 2 3 4 5 6
```

**Sample Output 4**
```
6
```

**Sample Input 5**
```
6
-1 -2 -3 -4 -5 -6
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
5
0 1 -1 2 -2
```

**Sample Output 6**
```
2
```

**Sample Input 7**
```
4
100 -100 100 -100
```

**Sample Output 7**
```
2
```

**Sample Input 8**
```
10
1 2 3 -1 -2 -3 0 0 5 -5
```

**Sample Output 8**
```
4
```

**Sample Input 9**
```
5
-1000000000 0 1 999999999 -1
```

**Sample Output 9**
```
2
```

**Tags**
Arrays, Basics

---

## Homework: Count Even and Odd Elements
**Problem Statement**
You are given an array of `N` integers. Print two counts on a single line, separated by one space: the number of even elements first, then the number of odd elements.

`0` is considered even. For a negative integer, evenness is determined by the absolute value's parity.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line with two integers: even count, odd count.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5
1 2 3 4 5
```

**Sample Output 0**
```
2 3
```

**Sample Input 1**
```
5
2 4 6 8 10
```

**Sample Output 1**
```
5 0
```

**Sample Input 2**
```
5
1 3 5 7 9
```

**Sample Output 2**
```
0 5
```

**Sample Input 3**
```
6
0 -1 -2 -3 -4 -5
```

**Sample Output 3**
```
3 3
```

**Sample Input 4**
```
1
0
```

**Sample Output 4**
```
1 0
```

**Sample Input 5**
```
1
7
```

**Sample Output 5**
```
0 1
```

**Sample Input 6**
```
4
100 -100 101 -101
```

**Sample Output 6**
```
2 2
```

**Sample Input 7**
```
3
0 0 0
```

**Sample Output 7**
```
3 0
```

**Sample Input 8**
```
5
-1 -2 -3 -4 -5
```

**Sample Output 8**
```
2 3
```

**Sample Input 9**
```
6
1 1 2 2 3 3
```

**Sample Output 9**
```
2 4
```

**Tags**
Arrays, Basics

---

## Homework: Number of Adjacent Swaps to Sort
**Problem Statement**
You are given an array of `N` integers. Print the minimum number of swaps of adjacent elements required to rearrange the array into non-decreasing order.

This count equals the number of inversions in the array — the number of index pairs `(i, j)` with `i < j` and `A[i] > A[j]`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the count.

**Constraints**
- `1 <= N <= 3000`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5
5 4 3 2 1
```

**Sample Output 0**
```
10
```

**Sample Input 1**
```
5
1 2 3 4 5
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
1
7
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
4
2 1 4 3
```

**Sample Output 3**
```
2
```

**Sample Input 4**
```
3
3 3 3
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
6
1 3 2 3 1 2
```

**Sample Output 5**
```
6
```

**Sample Input 6**
```
5
-1 -2 -3 -4 -5
```

**Sample Output 6**
```
10
```

**Sample Input 7**
```
8
8 1 7 2 6 3 5 4
```

**Sample Output 7**
```
16
```

**Sample Input 8**
```
5
1 1 2 2 1
```

**Sample Output 8**
```
2
```

**Sample Input 9**
```
7
7 6 5 4 3 2 1
```

**Sample Output 9**
```
21
```

**Tags**
Arrays, Sorting

---

## Homework: Check if a Value Exists in an Array
**Problem Statement**
You are given an array of `N` integers and an integer `X`. Print `Yes` if `X` appears anywhere in the array, otherwise print `No`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.
- Line 3: the integer `X`.

**Output Format**
A single line containing `Yes` or `No`.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i], X <= 10^9`

**Sample Input 0**
```
5
1 2 3 4 5
3
```

**Sample Output 0**
```
Yes
```

**Sample Input 1**
```
5
1 2 3 4 5
6
```

**Sample Output 1**
```
No
```

**Sample Input 2**
```
1
7
7
```

**Sample Output 2**
```
Yes
```

**Sample Input 3**
```
6
5 5 5 5 5 5
5
```

**Sample Output 3**
```
Yes
```

**Sample Input 4**
```
4
-1 -2 -3 -4
-3
```

**Sample Output 4**
```
Yes
```

**Sample Input 5**
```
3
0 0 0
0
```

**Sample Output 5**
```
Yes
```

**Sample Input 6**
```
5
1 2 3 4 5
1
```

**Sample Output 6**
```
Yes
```

**Sample Input 7**
```
5
1 2 3 4 5
5
```

**Sample Output 7**
```
Yes
```

**Sample Input 8**
```
6
10 20 30 40 50 60
35
```

**Sample Output 8**
```
No
```

**Sample Input 9**
```
5
1000000000 -1000000000 0 500 -500
-1000000000
```

**Sample Output 9**
```
Yes
```

**Tags**
Arrays, Basics

---
