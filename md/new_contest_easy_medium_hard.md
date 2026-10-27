# New Contest Problems (Easy / Medium / Hard)

Ten coding problems grouped by difficulty.

---

## Triangular Pattern

**Difficulty**: Easy

**Problem Statement**
Given an integer `n`, print a right-aligned triangular pattern. Row `i` (1-indexed, from the top) contains `i` characters that alternate ending in `1`. All rows share the same right edge, so row `i` is preceded by `n - i` leading spaces.

**Input Format**
A single integer `n`.

**Output Format**
`n` lines forming the pattern.

**Constraints**
- `1 <= n <= 100`

**Sample Input 0**
```
4
```

**Sample Output 0**
```
   1
  01
 101
0101
```

**Explanation 0**
`n = 4`, so we print 4 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

**Sample Input 1**
```
1
```

**Sample Output 1**
```
1
```

**Explanation 1**
`n = 1`, so there is only one row with one character. That character is `1`.

**Sample Input 2**
```
2
```

**Sample Output 2**
```
 1
01
```

**Explanation 2**
`n = 2`, so we print 2 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

**Sample Input 3**
```
5
```

**Sample Output 3**
```
    1
   01
  101
 0101
10101
```

**Explanation 3**
`n = 5`, so we print 5 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

**Sample Input 4**
```
7
```

**Sample Output 4**
```
      1
     01
    101
   0101
  10101
 010101
1010101
```

**Explanation 4**
`n = 7`, so we print 7 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

**Sample Input 5**
```
3
```

**Sample Output 5**
```
  1
 01
101
```

**Explanation 5**
`n = 3`, so we print 3 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

**Sample Input 6**
```
6
```

**Sample Output 6**
```
     1
    01
   101
  0101
 10101
010101
```

**Explanation 6**
`n = 6`, so we print 6 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

**Sample Input 7**
```
8
```

**Sample Output 7**
```
       1
      01
     101
    0101
   10101
  010101
 1010101
01010101
```

**Explanation 7**
`n = 8`, so we print 8 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

**Sample Input 8**
```
9
```

**Sample Output 8**
```
        1
       01
      101
     0101
    10101
   010101
  1010101
 01010101
101010101
```

**Explanation 8**
`n = 9`, so we print 9 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

**Sample Input 9**
```
10
```

**Sample Output 9**
```
         1
        01
       101
      0101
     10101
    010101
   1010101
  01010101
 101010101
0101010101
```

**Explanation 9**
`n = 10`, so we print 10 rows. Row `i` contains `i` characters that alternate and end in `1`. Every row shares the same right edge, so row above the bottom gets one extra leading space.

---

## Elements At Most Average

**Difficulty**: Easy

**Problem Statement**
Given an array of `n` integers, compute the real-valued average of the array and count how many elements are less than or equal to that average.

**Input Format**
- Line 1: an integer `n`.
- Line 2: `n` space-separated integers.

**Output Format**
A single integer - the count of elements `<= average`.

**Constraints**
- `1 <= n <= 10^5`
- `-10^9 <= element <= 10^9`

**Sample Input 0**
```
6
1 2 3 4 5 6
```

**Sample Output 0**
```
3
```

**Explanation 0**
Sum is 21 and average is 21/6 = 3.5. Elements <= 3.5 are 1, 2, 3 -> count 3.

**Sample Input 1**
```
1
5
```

**Sample Output 1**
```
1
```

**Explanation 1**
Only one element 5. Average is 5. Count of elements <= 5 is 1.

**Sample Input 2**
```
5
1 1 1 1 1
```

**Sample Output 2**
```
5
```

**Explanation 2**
All elements are 1. Average is 1. All 5 elements are <= 1 -> count 5.

**Sample Input 3**
```
4
10 20 30 40
```

**Sample Output 3**
```
2
```

**Explanation 3**
Sum 100, average 25. Elements <= 25 are 10 and 20 -> count 2.

**Sample Input 4**
```
3
-1 0 1
```

**Sample Output 4**
```
2
```

**Explanation 4**
Sum 0, average 0. Elements <= 0 are -1 and 0 -> count 2.

**Sample Input 5**
```
5
1 2 3 4 100
```

**Sample Output 5**
```
4
```

**Explanation 5**
Sum 110, average 22. Elements <= 22 are 1,2,3,4 -> count 4.

**Sample Input 6**
```
7
5 5 5 5 5 5 5
```

**Sample Output 6**
```
7
```

**Explanation 6**
All elements are 5. Average is 5. All 7 are <= 5 -> count 7.

**Sample Input 7**
```
6
1 2 3 4 5 100
```

**Sample Output 7**
```
5
```

**Explanation 7**
Sum 115, average ~19.17. Elements <= 19.17 are 1,2,3,4,5 -> count 5.

**Sample Input 8**
```
4
-10 -5 0 5
```

**Sample Output 8**
```
2
```

**Explanation 8**
Sum -10, average -2.5. Elements <= -2.5 are -10 and -5 -> count 2.

**Sample Input 9**
```
8
1 2 3 4 5 6 7 8
```

**Sample Output 9**
```
4
```

**Explanation 9**
Sum 36, average 4.5. Elements <= 4.5 are 1,2,3,4 -> count 4.

---

## Hollow Diamond

**Difficulty**: Easy

**Problem Statement**
Given an odd integer `n`, print a hollow diamond made of `*` of height `n`. The top and bottom rows contain a single `*`. All other rows contain exactly two `*` characters that form the two slanted edges, with spaces between them.

**Input Format**
A single integer `n`.

**Output Format**
`n` lines forming the hollow diamond.

**Constraints**
- `1 <= n <= 99` and `n` is odd.

**Sample Input 0**
```
5
```

**Sample Output 0**
```
  *
 * *
*   *
 * *
  *
```

**Explanation 0**
For `n = 5` the diamond has 5 rows. The middle row (row 3) is the widest with two `*` separated by 3 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

**Sample Input 1**
```
7
```

**Sample Output 1**
```
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```

**Explanation 1**
For `n = 7` the diamond has 7 rows. The middle row (row 4) is the widest with two `*` separated by 5 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

**Sample Input 2**
```
1
```

**Sample Output 2**
```
*
```

**Explanation 2**
`n = 1`, so the diamond is just a single `*`.

**Sample Input 3**
```
3
```

**Sample Output 3**
```
 *
* *
 *
```

**Explanation 3**
For `n = 3` the diamond has 3 rows. The middle row (row 2) is the widest with two `*` separated by 1 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

**Sample Input 4**
```
9
```

**Sample Output 4**
```
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
```

**Explanation 4**
For `n = 9` the diamond has 9 rows. The middle row (row 5) is the widest with two `*` separated by 7 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

**Sample Input 5**
```
11
```

**Sample Output 5**
```
     *
    * *
   *   *
  *     *
 *       *
*         *
 *       *
  *     *
   *   *
    * *
     *
```

**Explanation 5**
For `n = 11` the diamond has 11 rows. The middle row (row 6) is the widest with two `*` separated by 9 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

**Sample Input 6**
```
13
```

**Sample Output 6**
```
      *
     * *
    *   *
   *     *
  *       *
 *         *
*           *
 *         *
  *       *
   *     *
    *   *
     * *
      *
```

**Explanation 6**
For `n = 13` the diamond has 13 rows. The middle row (row 7) is the widest with two `*` separated by 11 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

**Sample Input 7**
```
15
```

**Sample Output 7**
```
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
```

**Explanation 7**
For `n = 15` the diamond has 15 rows. The middle row (row 8) is the widest with two `*` separated by 13 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

**Sample Input 8**
```
17
```

**Sample Output 8**
```
        *
       * *
      *   *
     *     *
    *       *
   *         *
  *           *
 *             *
*               *
 *             *
  *           *
   *         *
    *       *
     *     *
      *   *
       * *
        *
```

**Explanation 8**
For `n = 17` the diamond has 17 rows. The middle row (row 9) is the widest with two `*` separated by 15 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

**Sample Input 9**
```
19
```

**Sample Output 9**
```
         *
        * *
       *   *
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
*                 *
 *               *
  *             *
   *           *
    *         *
     *       *
      *     *
       *   *
        * *
         *
```

**Explanation 9**
For `n = 19` the diamond has 19 rows. The middle row (row 10) is the widest with two `*` separated by 17 spaces. Rows move inward one space on each side until the top and bottom rows, which each contain a single `*` at the center column.

---

## First Leader From Left

**Difficulty**: Easy

**Problem Statement**
A leader of an array is an element that is strictly greater than every element to its right. The rightmost element is always a leader by default. Print the first (leftmost) leader of the array.

**Input Format**
- Line 1: an integer `n`.
- Line 2: `n` space-separated integers.

**Output Format**
A single integer - the leftmost leader.

**Constraints**
- `1 <= n <= 10^5`
- `-10^9 <= element <= 10^9`

**Sample Input 0**
```
7
2 15 7 9 0 -3 -2
```

**Sample Output 0**
```
15
```

**Explanation 0**
15 is greater than every element to its right (7,9,0,-3,-2), so 15 is the first leader from the left.

**Sample Input 1**
```
1
5
```

**Sample Output 1**
```
5
```

**Explanation 1**
Single element array, so 5 is trivially the leader.

**Sample Input 2**
```
5
1 2 3 4 5
```

**Sample Output 2**
```
5
```

**Explanation 2**
Only 5 has nothing greater to its right. 5 is the first leader from the left.

**Sample Input 3**
```
5
5 4 3 2 1
```

**Sample Output 3**
```
5
```

**Explanation 3**
5 is greater than everything to its right, so 5 is the first leader.

**Sample Input 4**
```
3
10 10 10
```

**Sample Output 4**
```
10
```

**Explanation 4**
No element is strictly greater than every element to its right, but the last element 10 is a leader by vacuous rule.

**Sample Input 5**
```
8
3 1 4 1 5 9 2 6
```

**Sample Output 5**
```
9
```

**Explanation 5**
9 is strictly greater than 2 and 6 (its right), so 9 is the first leader.

**Sample Input 6**
```
4
-1 -2 -3 -4
```

**Sample Output 6**
```
-1
```

**Explanation 6**
-1 is greater than -2,-3,-4 to its right, so -1 is the first leader.

**Sample Input 7**
```
5
100 50 60 20 30
```

**Sample Output 7**
```
100
```

**Explanation 7**
100 > 50,60,20,30 -> leader. 100 is first from left.

**Sample Input 8**
```
5
7 8 7 8 7
```

**Sample Output 8**
```
8
```

**Explanation 8**
The last 7 is a leader by default; moving left, 8 at position 4 > 7, so 8 is a leader; the first such leader from left is the 8 at index 2.

**Sample Input 9**
```
6
1 3 2 4 0 -1
```

**Sample Output 9**
```
4
```

**Explanation 9**
4 at index 4 is strictly greater than 0 and -1 to its right, so 4 is the first leader from left.

---

## Three Coprime Numbers

**Difficulty**: Medium

**Problem Statement**
Three positive integers are coprime if `gcd(a, b, c) == 1`. Given three integers, print `YES` if they are coprime, otherwise print `NO`.

**Input Format**
Three space-separated integers `a`, `b`, `c`.

**Output Format**
`YES` or `NO`.

**Constraints**
- `1 <= a, b, c <= 10^9`

**Sample Input 0**
```
2 3 4
```

**Sample Output 0**
```
YES
```

**Explanation 0**
gcd(2,3,4) = 1 -> coprime -> YES.

**Sample Input 1**
```
2 4 8
```

**Sample Output 1**
```
NO
```

**Explanation 1**
gcd(2,4,8) = 2 (all divisible by 2) -> not coprime -> NO.

**Sample Input 2**
```
1 1 1
```

**Sample Output 2**
```
YES
```

**Explanation 2**
gcd(1,1,1) = 1 -> YES.

**Sample Input 3**
```
7 13 19
```

**Sample Output 3**
```
YES
```

**Explanation 3**
All three are distinct primes -> gcd 1 -> YES.

**Sample Input 4**
```
6 10 15
```

**Sample Output 4**
```
YES
```

**Explanation 4**
gcd(6,10,15) = 1 even though each pair shares a factor -> YES.

**Sample Input 5**
```
9 27 81
```

**Sample Output 5**
```
NO
```

**Explanation 5**
All divisible by 9 -> gcd 9 -> NO.

**Sample Input 6**
```
100 101 102
```

**Sample Output 6**
```
YES
```

**Explanation 6**
Consecutive integers include coprime pair -> overall gcd 1 -> YES.

**Sample Input 7**
```
14 21 35
```

**Sample Output 7**
```
NO
```

**Explanation 7**
All divisible by 7 -> gcd 7 -> NO.

**Sample Input 8**
```
17 34 51
```

**Sample Output 8**
```
NO
```

**Explanation 8**
All divisible by 17 -> gcd 17 -> NO.

**Sample Input 9**
```
5 7 11
```

**Sample Output 9**
```
YES
```

**Explanation 9**
All distinct primes -> gcd 1 -> YES.

---

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
For `n = 6` we print a 6-by-6 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 1**
```
1
```

**Sample Output 1**
```
*
```

**Explanation 1**
For `n = 1` we print a 1-by-1 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 2**
```
2
```

**Sample Output 2**
```
*#
#*
```

**Explanation 2**
For `n = 2` we print a 2-by-2 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 3**
```
3
```

**Sample Output 3**
```
*#*
#*#
*#*
```

**Explanation 3**
For `n = 3` we print a 3-by-3 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 4**
```
4
```

**Sample Output 4**
```
*#*#
#*#*
*#*#
#*#*
```

**Explanation 4**
For `n = 4` we print a 4-by-4 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 5**
```
5
```

**Sample Output 5**
```
*#*#*
#*#*#
*#*#*
#*#*#
*#*#*
```

**Explanation 5**
For `n = 5` we print a 5-by-5 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 6**
```
7
```

**Sample Output 6**
```
*#*#*#*
#*#*#*#
*#*#*#*
#*#*#*#
*#*#*#*
#*#*#*#
*#*#*#*
```

**Explanation 6**
For `n = 7` we print a 7-by-7 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 7**
```
8
```

**Sample Output 7**
```
*#*#*#*#
#*#*#*#*
*#*#*#*#
#*#*#*#*
*#*#*#*#
#*#*#*#*
*#*#*#*#
#*#*#*#*
```

**Explanation 7**
For `n = 8` we print a 8-by-8 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 8**
```
9
```

**Sample Output 8**
```
*#*#*#*#*
#*#*#*#*#
*#*#*#*#*
#*#*#*#*#
*#*#*#*#*
#*#*#*#*#
*#*#*#*#*
#*#*#*#*#
*#*#*#*#*
```

**Explanation 8**
For `n = 9` we print a 9-by-9 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

**Sample Input 9**
```
10
```

**Sample Output 9**
```
*#*#*#*#*#
#*#*#*#*#*
*#*#*#*#*#
#*#*#*#*#*
*#*#*#*#*#
#*#*#*#*#*
*#*#*#*#*#
#*#*#*#*#*
*#*#*#*#*#
#*#*#*#*#*
```

**Explanation 9**
For `n = 10` we print a 10-by-10 grid. Top-left is `*`. Each step right or down flips the character, giving the standard checkerboard pattern.

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
- `-10^9 <= element <= 10^9`

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
max-min = 4. Only 5 > 4 -> count 1.

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
max-min = 4. 5,6,7,8 > 4 -> count 4.

**Sample Input 2**
```
1
10
```

**Sample Output 2**
```
1
```

**Explanation 2**
Single element, max-min = 0. 10 > 0 -> count 1.

**Sample Input 3**
```
4
2 2 2 2
```

**Sample Output 3**
```
4
```

**Explanation 3**
max-min = 0. All 4 are > 0 -> count 4.

**Sample Input 4**
```
5
-5 -4 -3 -2 -1
```

**Sample Output 4**
```
0
```

**Explanation 4**
max-min = 4. Only elements > 4; none -> count 0.

**Sample Input 5**
```
5
100 1 50 25 75
```

**Sample Output 5**
```
1
```

**Explanation 5**
max-min = 99. Only 100 > 99 -> count 1.

**Sample Input 6**
```
4
1 1 1 10
```

**Sample Output 6**
```
1
```

**Explanation 6**
max-min = 9. Only 10 > 9 -> count 1.

**Sample Input 7**
```
5
3 3 3 3 3
```

**Sample Output 7**
```
5
```

**Explanation 7**
max-min = 0. All 5 are > 0 -> count 5.

**Sample Input 8**
```
4
-10 -20 -30 -40
```

**Sample Output 8**
```
0
```

**Explanation 8**
max-min = 30. Elements > 30: none (all negative) -> count 0.

**Sample Input 9**
```
6
5 10 15 20 25 30
```

**Sample Output 9**
```
1
```

**Explanation 9**
max-min = 25. Only 30 > 25 -> count 1.

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
The 1st prime number is 2.

**Sample Input 1**
```
5
```

**Sample Output 1**
```
11
```

**Explanation 1**
The list of primes starts 2, 3, 5, 7, 11, ... The 5-th prime is 11.

**Sample Input 2**
```
10000
```

**Sample Output 2**
```
104729
```

**Explanation 2**
The list of primes starts 2, 3, 5, 7, 11, ... The 10000-th prime is 104729.

**Sample Input 3**
```
2
```

**Sample Output 3**
```
3
```

**Explanation 3**
The list of primes starts 2, 3, 5, 7, 11, ... The 2-th prime is 3.

**Sample Input 4**
```
3
```

**Sample Output 4**
```
5
```

**Explanation 4**
The list of primes starts 2, 3, 5, 7, 11, ... The 3-th prime is 5.

**Sample Input 5**
```
10
```

**Sample Output 5**
```
29
```

**Explanation 5**
The list of primes starts 2, 3, 5, 7, 11, ... The 10-th prime is 29.

**Sample Input 6**
```
100
```

**Sample Output 6**
```
541
```

**Explanation 6**
The list of primes starts 2, 3, 5, 7, 11, ... The 100-th prime is 541.

**Sample Input 7**
```
1000
```

**Sample Output 7**
```
7919
```

**Explanation 7**
The list of primes starts 2, 3, 5, 7, 11, ... The 1000-th prime is 7919.

**Sample Input 8**
```
50000
```

**Sample Output 8**
```
611953
```

**Explanation 8**
The list of primes starts 2, 3, 5, 7, 11, ... The 50000-th prime is 611953.

**Sample Input 9**
```
100000
```

**Sample Output 9**
```
1299709
```

**Explanation 9**
The list of primes starts 2, 3, 5, 7, 11, ... The 100000-th prime is 1299709.

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
Sum of all primes p with p <= 20 is 77.

**Sample Input 1**
```
2
```

**Sample Output 1**
```
2
```

**Explanation 1**
Sum of all primes p with p <= 2 is 2.

**Sample Input 2**
```
100000
```

**Sample Output 2**
```
454396537
```

**Explanation 2**
Sum of all primes p with p <= 100000 is 454396537.

**Sample Input 3**
```
1
```

**Sample Output 3**
```
0
```

**Explanation 3**
There are no primes <= 1, so the sum is 0.

**Sample Input 4**
```
10
```

**Sample Output 4**
```
17
```

**Explanation 4**
Sum of all primes p with p <= 10 is 17.

**Sample Input 5**
```
100
```

**Sample Output 5**
```
1060
```

**Explanation 5**
Sum of all primes p with p <= 100 is 1060.

**Sample Input 6**
```
1000
```

**Sample Output 6**
```
76127
```

**Explanation 6**
Sum of all primes p with p <= 1000 is 76127.

**Sample Input 7**
```
10000
```

**Sample Output 7**
```
5736396
```

**Explanation 7**
Sum of all primes p with p <= 10000 is 5736396.

**Sample Input 8**
```
50000
```

**Sample Output 8**
```
121013308
```

**Explanation 8**
Sum of all primes p with p <= 50000 is 121013308.

**Sample Input 9**
```
5
```

**Sample Output 9**
```
10
```

**Explanation 9**
Sum of all primes p with p <= 5 is 10.

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
Array (1-indexed): [1, 2, 3, 4, 5].
- Query `2 4`: sum of positions 2..4 = 9.
- Query `1 5`: sum of positions 1..5 = 15.
- Query `3 5`: sum of positions 3..5 = 12.

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
Array (1-indexed): [9, 7, 5, 3, 1, 2, 4].
- Query `1 3`: sum of positions 1..3 = 21.
- Query `4 7`: sum of positions 4..7 = 10.
- Query `2 5`: sum of positions 2..5 = 16.
- Query `1 4`: sum of positions 1..4 = 24.
- Query `3 6`: sum of positions 3..6 = 11.

**Sample Input 2**
```
1 1
10
1 1
```

**Sample Output 2**
```
10
```

**Explanation 2**
Array (1-indexed): [10].
- Query `1 1`: sum of positions 1..1 = 10.

**Sample Input 3**
```
5 3
1 1 1 1 1
1 5
2 4
3 3
```

**Sample Output 3**
```
5
3
1
```

**Explanation 3**
Array (1-indexed): [1, 1, 1, 1, 1].
- Query `1 5`: sum of positions 1..5 = 5.
- Query `2 4`: sum of positions 2..4 = 3.
- Query `3 3`: sum of positions 3..3 = 1.

**Sample Input 4**
```
5 3
-1 -2 -3 -4 -5
1 5
2 3
1 1
```

**Sample Output 4**
```
-15
-5
-1
```

**Explanation 4**
Array (1-indexed): [-1, -2, -3, -4, -5].
- Query `1 5`: sum of positions 1..5 = -15.
- Query `2 3`: sum of positions 2..3 = -5.
- Query `1 1`: sum of positions 1..1 = -1.

**Sample Input 5**
```
5 4
100 200 300 400 500
1 5
2 4
3 3
1 2
```

**Sample Output 5**
```
1500
900
300
300
```

**Explanation 5**
Array (1-indexed): [100, 200, 300, 400, 500].
- Query `1 5`: sum of positions 1..5 = 1500.
- Query `2 4`: sum of positions 2..4 = 900.
- Query `3 3`: sum of positions 3..3 = 300.
- Query `1 2`: sum of positions 1..2 = 300.

**Sample Input 6**
```
10 5
1 2 3 4 5 6 7 8 9 10
1 10
3 7
5 5
1 5
6 10
```

**Sample Output 6**
```
55
25
5
15
40
```

**Explanation 6**
Array (1-indexed): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
- Query `1 10`: sum of positions 1..10 = 55.
- Query `3 7`: sum of positions 3..7 = 25.
- Query `5 5`: sum of positions 5..5 = 5.
- Query `1 5`: sum of positions 1..5 = 15.
- Query `6 10`: sum of positions 6..10 = 40.

**Sample Input 7**
```
6 3
5 5 5 5 5 5
1 6
2 5
3 4
```

**Sample Output 7**
```
30
20
10
```

**Explanation 7**
Array (1-indexed): [5, 5, 5, 5, 5, 5].
- Query `1 6`: sum of positions 1..6 = 30.
- Query `2 5`: sum of positions 2..5 = 20.
- Query `3 4`: sum of positions 3..4 = 10.

**Sample Input 8**
```
3 4
1000000000 -1000000000 1000000000
1 3
1 1
2 3
1 2
```

**Sample Output 8**
```
1000000000
1000000000
0
0
```

**Explanation 8**
Array (1-indexed): [1000000000, -1000000000, 1000000000].
- Query `1 3`: sum of positions 1..3 = 1000000000.
- Query `1 1`: sum of positions 1..1 = 1000000000.
- Query `2 3`: sum of positions 2..3 = 0.
- Query `1 2`: sum of positions 1..2 = 0.

**Sample Input 9**
```
9 5
7 3 8 1 9 2 6 4 5
1 9
2 8
3 7
4 6
5 5
```

**Sample Output 9**
```
45
33
26
12
9
```

**Explanation 9**
Array (1-indexed): [7, 3, 8, 1, 9, 2, 6, 4, 5].
- Query `1 9`: sum of positions 1..9 = 45.
- Query `2 8`: sum of positions 2..8 = 33.
- Query `3 7`: sum of positions 3..7 = 26.
- Query `4 6`: sum of positions 4..6 = 12.
- Query `5 5`: sum of positions 5..5 = 9.

---
