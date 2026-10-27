# DSA-101 Classwork - Part 2 (Days 14 to 33)

Author-ready markdown for `automator.py`. Strict statements (no approach
hints). Each problem has 10 sample I/O pairs computed by reference solvers.
Titles that repeat curriculum content from Part 1 carry a `(Day N)` suffix
so each authored HackerRank challenge stays uniquely addressable.

After uploading:
1. `venv\Scripts\python.exe tools\hr_mark_samples.py --md classwork_part2_days14_33.md --apply`
2. Enable C++14, Java 8, Python 3 in the admin UI on each challenge.
3. `venv\Scripts\python.exe tools\hr_add_to_contest.py --md classwork_part2_days14_33.md --apply`

---


## Classwork: Pyramid of Stars
**Problem Statement**
A single integer `N` is given. Print a centered pyramid of `N` rows made of `*`. Row `i` (1-indexed) has exactly `N - i` leading spaces followed by `2*i - 1` `*` characters and no trailing spaces.

For `N = 4` the pyramid is:
```
   *
  ***
 *****
*******
```

**Input Format**
A single line containing one integer `N`.

**Output Format**
`N` lines forming the pyramid.

**Constraints**
- `1 <= N <= 30`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
*
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
 *
***
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
  *
 ***
*****
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
   *
  ***
 *****
*******
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
    *
   ***
  *****
 *******
*********
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
     *
    ***
   *****
  *******
 *********
***********
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
      *
     ***
    *****
   *******
  *********
 ***********
*************
```

**Sample Input 7**
```
10
```

**Sample Output 7**
```
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
```

**Sample Input 8**
```
12
```

**Sample Output 8**
```
           *
          ***
         *****
        *******
       *********
      ***********
     *************
    ***************
   *****************
  *******************
 *********************
***********************
```

**Sample Input 9**
```
15
```

**Sample Output 9**
```
              *
             ***
            *****
           *******
          *********
         ***********
        *************
       ***************
      *****************
     *******************
    *********************
   ***********************
  *************************
 ***************************
*****************************
```

**Tags**
Patterns, Nested Loops

---

## Classwork: Inverted Pyramid of Stars
**Problem Statement**
A single integer `N` is given. Print a centered inverted pyramid of `N` rows. Row `i` (1-indexed, counted from the top) has exactly `i - 1` leading spaces followed by `2*(N - i + 1) - 1` `*` characters, with no trailing spaces.

For `N = 4` the output is:
```
*******
 *****
  ***
   *
```

**Input Format**
A single line containing one integer `N`.

**Output Format**
`N` lines forming the inverted pyramid.

**Constraints**
- `1 <= N <= 30`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
*
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
***
 *
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
*****
 ***
  *
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
*******
 *****
  ***
   *
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
*********
 *******
  *****
   ***
    *
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
***********
 *********
  *******
   *****
    ***
     *
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
*************
 ***********
  *********
   *******
    *****
     ***
      *
```

**Sample Input 7**
```
10
```

**Sample Output 7**
```
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
```

**Sample Input 8**
```
12
```

**Sample Output 8**
```
***********************
 *********************
  *******************
   *****************
    ***************
     *************
      ***********
       *********
        *******
         *****
          ***
           *
```

**Sample Input 9**
```
15
```

**Sample Output 9**
```
*****************************
 ***************************
  *************************
   ***********************
    *********************
     *******************
      *****************
       ***************
        *************
         ***********
          *********
           *******
            *****
             ***
              *
```

**Tags**
Patterns, Nested Loops

---

## Classwork: Number Pyramid
**Problem Statement**
A single integer `N` is given. Print a centered pyramid of `N` rows built from digits. Row `i` (1-indexed) has exactly `N - i` leading spaces followed by `2*i - 1` copies of the digit character representing `i`.

For `N = 4` the pyramid is:
```
   1
  222
 33333
4444444
```

**Input Format**
A single line containing one integer `N`.

**Output Format**
`N` lines forming the number pyramid.

**Constraints**
- `1 <= N <= 9`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
1
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
 1
222
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
  1
 222
33333
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
   1
  222
 33333
4444444
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
    1
   222
  33333
 4444444
555555555
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
     1
    222
   33333
  4444444
 555555555
66666666666
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
      1
     222
    33333
   4444444
  555555555
 66666666666
7777777777777
```

**Sample Input 7**
```
8
```

**Sample Output 7**
```
       1
      222
     33333
    4444444
   555555555
  66666666666
 7777777777777
888888888888888
```

**Sample Input 8**
```
9
```

**Sample Output 8**
```
        1
       222
      33333
     4444444
    555555555
   66666666666
  7777777777777
 888888888888888
99999999999999999
```

**Sample Input 9**
```
3
```

**Sample Output 9**
```
  1
 222
33333
```

**Tags**
Patterns, Nested Loops

---

## Classwork: Full Diamond of Stars
**Problem Statement**
A single integer `N` is given. Print a centered diamond made of `*` characters that has `2*N - 1` rows in total.

The first `N` rows form a pyramid whose row `i` (1-indexed) has `N - i` leading spaces followed by `2*i - 1` `*` characters. The next `N - 1` rows mirror rows `N-1 .. 1` of the pyramid.

For `N = 4` the diamond is:
```
   *
  ***
 *****
*******
 *****
  ***
   *
```

**Input Format**
A single line containing one integer `N`.

**Output Format**
`2*N - 1` lines forming the diamond, no trailing spaces.

**Constraints**
- `1 <= N <= 20`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
*
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
 *
***
 *
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
  *
 ***
*****
 ***
  *
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
   *
  ***
 *****
*******
 *****
  ***
   *
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
     *
    ***
   *****
  *******
 *********
***********
 *********
  *******
   *****
    ***
     *
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
      *
     ***
    *****
   *******
  *********
 ***********
*************
 ***********
  *********
   *******
    *****
     ***
      *
```

**Sample Input 7**
```
8
```

**Sample Output 7**
```
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
 *************
  ***********
   *********
    *******
     *****
      ***
       *
```

**Sample Input 8**
```
10
```

**Sample Output 8**
```
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *
```

**Sample Input 9**
```
12
```

**Sample Output 9**
```
           *
          ***
         *****
        *******
       *********
      ***********
     *************
    ***************
   *****************
  *******************
 *********************
***********************
 *********************
  *******************
   *****************
    ***************
     *************
      ***********
       *********
        *******
         *****
          ***
           *
```

**Tags**
Patterns, Nested Loops

---

## Classwork: Hollow Right Triangle
**Problem Statement**
A single integer `N` is given. Print a hollow right-angled triangle with `N` rows. Row `i` (1-indexed) has exactly `i` characters:

- Row `1`: a single `*`.
- Row `N`: `N` `*` characters (the solid base).
- Every other row `i` (with `1 < i < N`): starts and ends with `*`, with `i - 2` spaces in between.

For `N = 5`:
```
*
**
* *
*  *
*****
```

**Input Format**
A single line containing one integer `N`.

**Output Format**
`N` lines forming the hollow triangle.

**Constraints**
- `1 <= N <= 30`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
*
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
*
**
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
*
**
***
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
*
**
* *
****
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
*
**
* *
*  *
*****
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
*
**
* *
*  *
*   *
******
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
*
**
* *
*  *
*   *
*    *
*******
```

**Sample Input 7**
```
10
```

**Sample Output 7**
```
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
**********
```

**Sample Input 8**
```
12
```

**Sample Output 8**
```
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
*        *
*         *
************
```

**Sample Input 9**
```
20
```

**Sample Output 9**
```
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
*        *
*         *
*          *
*           *
*            *
*             *
*              *
*               *
*                *
*                 *
********************
```

**Tags**
Patterns, Nested Loops

---

## Classwork: nCr using a Factorial Helper
**Problem Statement**
Two non-negative integers `N` and `R` are given on a single line, separated by a space. Print the value of the binomial coefficient `C(N, R) = N! / (R! * (N-R)!)`.

If `R > N`, print `0`.

**Input Format**
A single line containing two space-separated integers `N` and `R`.

**Output Format**
A single line containing `C(N, R)`.

**Constraints**
- `0 <= N <= 20`
- `0 <= R <= 25`

**Sample Input 0**
```
5 2
```

**Sample Output 0**
```
10
```

**Sample Input 1**
```
10 0
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
10 10
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
20 10
```

**Sample Output 3**
```
184756
```

**Sample Input 4**
```
6 3
```

**Sample Output 4**
```
20
```

**Sample Input 5**
```
7 4
```

**Sample Output 5**
```
35
```

**Sample Input 6**
```
0 0
```

**Sample Output 6**
```
1
```

**Sample Input 7**
```
8 5
```

**Sample Output 7**
```
56
```

**Sample Input 8**
```
12 6
```

**Sample Output 8**
```
924
```

**Sample Input 9**
```
15 3
```

**Sample Output 9**
```
455
```

**Tags**
Functions, Number Theory

---

## Classwork: Areas of Square, Rectangle and Circle
**Problem Statement**
Three shapes are described on three lines:

- Line 1: an integer `S` (the side of a square).
- Line 2: two integers `L W` (length and width of a rectangle).
- Line 3: an integer `R` (the radius of a circle).

Print three lines: the area of the square, the area of the rectangle, and the area of the circle (using `pi = 3.14`). The first two areas are integers, the circle's area is printed with exactly two digits after the decimal point.

**Input Format**
Three lines: `S` on line 1, `L W` on line 2, `R` on line 3.

**Output Format**
Three lines: area of square, area of rectangle, area of circle (two decimal places).

**Constraints**
- `1 <= S, L, W, R <= 10^4`

**Sample Input 0**
```
5
4 3
7
```

**Sample Output 0**
```
25
12
153.86
```

**Sample Input 1**
```
1
1 1
1
```

**Sample Output 1**
```
1
1
3.14
```

**Sample Input 2**
```
10
5 20
3
```

**Sample Output 2**
```
100
100
28.26
```

**Sample Input 3**
```
12
6 8
5
```

**Sample Output 3**
```
144
48
78.50
```

**Sample Input 4**
```
100
50 40
25
```

**Sample Output 4**
```
10000
2000
1962.50
```

**Sample Input 5**
```
3
2 9
4
```

**Sample Output 5**
```
9
18
50.24
```

**Sample Input 6**
```
20
10 10
10
```

**Sample Output 6**
```
400
100
314.00
```

**Sample Input 7**
```
8
7 6
2
```

**Sample Output 7**
```
64
42
12.56
```

**Sample Input 8**
```
15
3 3
6
```

**Sample Output 8**
```
225
9
113.04
```

**Sample Input 9**
```
9
11 4
8
```

**Sample Output 9**
```
81
44
200.96
```

**Tags**
Functions, Geometry

---

## Classwork: GCD using Euclidean Algorithm
**Problem Statement**
Two non-negative integers `A` and `B` are given on a single line. Print their greatest common divisor. By convention, `gcd(0, 0) = 0` and `gcd(0, X) = X` for any positive `X`.

**Input Format**
A single line with two space-separated integers `A` and `B`.

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
Number Theory, Functions

---

## Classwork: Check if Two Numbers are Coprime
**Problem Statement**
Two positive integers `A` and `B` are given on a single line. Print `Yes` if they are coprime (that is, `gcd(A, B) == 1`), otherwise print `No`.

**Input Format**
A single line with two space-separated integers `A` and `B`.

**Output Format**
A single line containing `Yes` or `No`.

**Constraints**
- `1 <= A, B <= 10^9`

**Sample Input 0**
```
8 15
```

**Sample Output 0**
```
Yes
```

**Sample Input 1**
```
12 18
```

**Sample Output 1**
```
No
```

**Sample Input 2**
```
1 1
```

**Sample Output 2**
```
Yes
```

**Sample Input 3**
```
7 13
```

**Sample Output 3**
```
Yes
```

**Sample Input 4**
```
100 75
```

**Sample Output 4**
```
No
```

**Sample Input 5**
```
999999937 1
```

**Sample Output 5**
```
Yes
```

**Sample Input 6**
```
35 49
```

**Sample Output 6**
```
No
```

**Sample Input 7**
```
17 23
```

**Sample Output 7**
```
Yes
```

**Sample Input 8**
```
1000000000 999999999
```

**Sample Output 8**
```
Yes
```

**Sample Input 9**
```
6 25
```

**Sample Output 9**
```
Yes
```

**Tags**
Number Theory, Functions

---

## Classwork: Factorial Recursively
**Problem Statement**
A single non-negative integer `N` is given. Print `N!` (the factorial of `N`).

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing `N!`.

**Constraints**
- `0 <= N <= 20`

**Sample Input 0**
```
0
```

**Sample Output 0**
```
1
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
5
```

**Sample Output 2**
```
120
```

**Sample Input 3**
```
10
```

**Sample Output 3**
```
3628800
```

**Sample Input 4**
```
20
```

**Sample Output 4**
```
2432902008176640000
```

**Sample Input 5**
```
12
```

**Sample Output 5**
```
479001600
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
5040
```

**Sample Input 7**
```
3
```

**Sample Output 7**
```
6
```

**Sample Input 8**
```
15
```

**Sample Output 8**
```
1307674368000
```

**Sample Input 9**
```
18
```

**Sample Output 9**
```
6402373705728000
```

**Tags**
Recursion, Number Theory

---

## Classwork: All Non-Empty Subsequences of a String
**Problem Statement**
A single string `S` of lowercase English letters is given. Print every non-empty subsequence of `S`, one per line.

A subsequence is obtained by deleting zero or more characters from `S` without changing the order of the remaining characters. Duplicates are not removed.

The subsequences must be printed in the following order: for `k = 1, 2, ..., 2^N - 1` (where `N = |S|`) print the subsequence formed by the characters at positions `i` (0-indexed from the left of `S`) for which bit `i` of `k` is set.

**Input Format**
A single line containing the string `S`.

**Output Format**
`2^N - 1` lines, each a non-empty subsequence, in the order described above.

**Constraints**
- `1 <= |S| <= 12`
- `S` contains only lowercase English letters.

**Sample Input 0**
```
a
```

**Sample Output 0**
```
a
```

**Sample Input 1**
```
ab
```

**Sample Output 1**
```
a
b
ab
```

**Sample Input 2**
```
abc
```

**Sample Output 2**
```
a
b
ab
c
ac
bc
abc
```

**Sample Input 3**
```
abcd
```

**Sample Output 3**
```
a
b
ab
c
ac
bc
abc
d
ad
bd
abd
cd
acd
bcd
abcd
```

**Sample Input 4**
```
ba
```

**Sample Output 4**
```
b
a
ba
```

**Sample Input 5**
```
xyz
```

**Sample Output 5**
```
x
y
xy
z
xz
yz
xyz
```

**Sample Input 6**
```
hi
```

**Sample Output 6**
```
h
i
hi
```

**Sample Input 7**
```
abcde
```

**Sample Output 7**
```
a
b
ab
c
ac
bc
abc
d
ad
bd
abd
cd
acd
bcd
abcd
e
ae
be
abe
ce
ace
bce
abce
de
ade
bde
abde
cde
acde
bcde
abcde
```

**Sample Input 8**
```
code
```

**Sample Output 8**
```
c
o
co
d
cd
od
cod
e
ce
oe
coe
de
cde
ode
code
```

**Sample Input 9**
```
test
```

**Sample Output 9**
```
t
e
te
s
ts
es
tes
t
tt
et
tet
st
tst
est
test
```

**Tags**
Recursion, Strings, Bit Manipulation

---

## Classwork: Sum of Array Recursively
**Problem Statement**
An array of `N` integers is given. Print the sum of all its elements.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line containing the sum.

**Constraints**
- `1 <= N <= 10^5`
- `-10^4 <= A[i] <= 10^4`

**Sample Input 0**
```
5
1 2 3 4 5
```

**Sample Output 0**
```
15
```

**Sample Input 1**
```
1
7
```

**Sample Output 1**
```
7
```

**Sample Input 2**
```
3
-1 -2 -3
```

**Sample Output 2**
```
-6
```

**Sample Input 3**
```
4
10 -10 10 -10
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
6
100 200 300 400 500 600
```

**Sample Output 4**
```
2100
```

**Sample Input 5**
```
2
0 0
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
5
1 1 1 1 1
```

**Sample Output 6**
```
5
```

**Sample Input 7**
```
3
10000 -10000 5
```

**Sample Output 7**
```
5
```

**Sample Input 8**
```
8
1 2 3 4 5 6 7 8
```

**Sample Output 8**
```
36
```

**Sample Input 9**
```
10
-1 -2 -3 -4 -5 5 4 3 2 1
```

**Sample Output 9**
```
0
```

**Tags**
Recursion, Arrays

---

## Classwork: Count Elements Above the Average
**Problem Statement**
An array of `N` integers is given. Compute the average of the array as a real number (`sum / N`) and print the number of elements that are strictly greater than this average.

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
1 2 3 4 5
```

**Sample Output 0**
```
2
```

**Sample Input 1**
```
5
5 5 5 5 5
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
6
10 20 30 40 50 60
```

**Sample Output 2**
```
3
```

**Sample Input 3**
```
4
-10 -20 -30 -40
```

**Sample Output 3**
```
2
```

**Sample Input 4**
```
1
7
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
7
1 2 3 4 5 6 100
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
3
-1 0 1
```

**Sample Output 6**
```
1
```

**Sample Input 7**
```
8
1 1 1 1 100 100 100 100
```

**Sample Output 7**
```
4
```

**Sample Input 8**
```
2
0 10
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
5
1000000000 -1000000000 0 500 -500
```

**Sample Output 9**
```
2
```

**Tags**
Arrays, Loops

---

## Classwork: Bubble Sort (Ascending)
**Problem Statement**
An array of `N` integers is given. Print the array sorted in non-decreasing order.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line with the sorted array, elements separated by a single space.

**Constraints**
- `1 <= N <= 10^4`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5
5 4 3 2 1
```

**Sample Output 0**
```
1 2 3 4 5
```

**Sample Input 1**
```
5
1 2 3 4 5
```

**Sample Output 1**
```
1 2 3 4 5
```

**Sample Input 2**
```
1
42
```

**Sample Output 2**
```
42
```

**Sample Input 3**
```
4
3 3 3 3
```

**Sample Output 3**
```
3 3 3 3
```

**Sample Input 4**
```
6
-1 -5 2 8 0 -3
```

**Sample Output 4**
```
-5 -3 -1 0 2 8
```

**Sample Input 5**
```
8
8 1 7 2 6 3 5 4
```

**Sample Output 5**
```
1 2 3 4 5 6 7 8
```

**Sample Input 6**
```
3
1000000000 -1000000000 0
```

**Sample Output 6**
```
-1000000000 0 1000000000
```

**Sample Input 7**
```
5
1 1 2 2 1
```

**Sample Output 7**
```
1 1 1 2 2
```

**Sample Input 8**
```
7
10 20 30 40 50 5 15
```

**Sample Output 8**
```
5 10 15 20 30 40 50
```

**Sample Input 9**
```
10
9 8 7 6 5 4 3 2 1 0
```

**Sample Output 9**
```
0 1 2 3 4 5 6 7 8 9
```

**Tags**
Sorting, Arrays

---

## Classwork: Selection Sort (Ascending)
**Problem Statement**
An array of `N` integers is given. Print the array sorted in non-decreasing order.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single line with the sorted array, elements separated by a single space.

**Constraints**
- `1 <= N <= 10^4`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
5
5 4 3 2 1
```

**Sample Output 0**
```
1 2 3 4 5
```

**Sample Input 1**
```
5
1 2 3 4 5
```

**Sample Output 1**
```
1 2 3 4 5
```

**Sample Input 2**
```
1
42
```

**Sample Output 2**
```
42
```

**Sample Input 3**
```
4
3 3 3 3
```

**Sample Output 3**
```
3 3 3 3
```

**Sample Input 4**
```
6
-1 -5 2 8 0 -3
```

**Sample Output 4**
```
-5 -3 -1 0 2 8
```

**Sample Input 5**
```
8
8 1 7 2 6 3 5 4
```

**Sample Output 5**
```
1 2 3 4 5 6 7 8
```

**Sample Input 6**
```
3
1000000000 -1000000000 0
```

**Sample Output 6**
```
-1000000000 0 1000000000
```

**Sample Input 7**
```
5
1 1 2 2 1
```

**Sample Output 7**
```
1 1 1 2 2
```

**Sample Input 8**
```
7
10 20 30 40 50 5 15
```

**Sample Output 8**
```
5 10 15 20 30 40 50
```

**Sample Input 9**
```
10
9 8 7 6 5 4 3 2 1 0
```

**Sample Output 9**
```
0 1 2 3 4 5 6 7 8 9
```

**Tags**
Sorting, Arrays

---

## Classwork: Sort Pairs by the Second Value
**Problem Statement**
`N` pairs of integers are given, one pair per line. Sort the pairs in non-decreasing order of their second value. If two pairs have the same second value, keep them in their original input order (stable sort).

Print each pair on its own line, the two integers separated by a single space.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: each contains two space-separated integers `A B`.

**Output Format**
`N` lines with the pairs sorted by the second value.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A, B <= 10^9`

**Sample Input 0**
```
3
1 3
2 1
5 2
```

**Sample Output 0**
```
2 1
5 2
1 3
```

**Sample Input 1**
```
1
7 7
```

**Sample Output 1**
```
7 7
```

**Sample Input 2**
```
4
1 2
2 2
3 1
4 1
```

**Sample Output 2**
```
3 1
4 1
1 2
2 2
```

**Sample Input 3**
```
5
10 5
9 4
8 3
7 2
6 1
```

**Sample Output 3**
```
6 1
7 2
8 3
9 4
10 5
```

**Sample Input 4**
```
3
1 -1
2 -2
3 -3
```

**Sample Output 4**
```
3 -3
2 -2
1 -1
```

**Sample Input 5**
```
6
1 100
2 -100
3 0
4 100
5 -100
6 50
```

**Sample Output 5**
```
2 -100
5 -100
3 0
6 50
1 100
4 100
```

**Sample Input 6**
```
2
1 1
2 1
```

**Sample Output 6**
```
1 1
2 1
```

**Sample Input 7**
```
5
5 5
4 4
3 3
2 2
1 1
```

**Sample Output 7**
```
1 1
2 2
3 3
4 4
5 5
```

**Sample Input 8**
```
4
1000000000 1
1 1000000000
999 999
1 1
```

**Sample Output 8**
```
1000000000 1
1 1
999 999
1 1000000000
```

**Sample Input 9**
```
3
1 2
2 2
3 2
```

**Sample Output 9**
```
1 2
2 2
3 2
```

**Tags**
Sorting, STL, Vectors

---
