# New Practice Challenges — Batch 1

Author-ready markdown for `automator.py`. Statements are strictly descriptive: no hints on approach or solution. Each problem carries 10 sample I/O pairs (numbered 1-10); the first two of each are marked as **Sample** test cases and carry a **Sample Explanation**, matching the convention used in `DSA301_homework_shells_todo.md`. Run `tools/hr_mark_samples.py --md new_batch_odd_even_diamond_etc.md --apply` afterwards to flag the first two as samples. Ensure C++14, Java 8 and Python 3 are enabled on each challenge before publishing.

---

## Sum of Digits at Odd and Even Places (Left-Indexed)

**Problem Statement**
You are given an integer `N`. Read its digits from left to right and number their positions starting at 1 (so the leftmost digit is position 1, the next digit is position 2, and so on).

Find the sum of all digits sitting at odd positions (1st, 3rd, 5th, ...) and the sum of all digits sitting at even positions (2nd, 4th, 6th, ...).

Print the odd-position sum followed by the even-position sum, separated by a single space.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing two integers separated by a space: the sum of digits at odd positions, then the sum of digits at even positions.

**Constraints**
- `1 <= N <= 10^18`

**Sample Input 1**
```
67524
```
**Sample Output 1**
```
15 9
```
**Sample Explanation 1**
The digits from left to right are `6, 7, 5, 2, 4` at positions `1, 2, 3, 4, 5`. The odd positions (1, 3, 5) hold `6, 5, 4`, which sum to `15`. The even positions (2, 4) hold `7, 2`, which sum to `9`.

**Sample Input 2**
```
8976
```
**Sample Output 2**
```
15 15
```
**Sample Explanation 2**
The digits from left to right are `8, 9, 7, 6` at positions `1, 2, 3, 4`. The odd positions (1, 3) hold `8, 7`, which sum to `15`. The even positions (2, 4) hold `9, 6`, which sum to `15`.

**Sample Input 3**
```
5
```
**Sample Output 3**
```
5 0
```

**Sample Input 4**
```
12
```
**Sample Output 4**
```
1 2
```

**Sample Input 5**
```
100
```
**Sample Output 5**
```
1 0
```

**Sample Input 6**
```
999999
```
**Sample Output 6**
```
27 27
```

**Sample Input 7**
```
1000000000
```
**Sample Output 7**
```
1 0
```

**Sample Input 8**
```
9081726354
```
**Sample Output 8**
```
35 10
```

**Sample Input 9**
```
123456789
```
**Sample Output 9**
```
25 20
```

**Sample Input 10**
```
40506070
```
**Sample Output 10**
```
22 0
```

**Tags**
Basics, Digits, Math

---

## Hollow Diamond

**Problem Statement**
You are given an integer `N`. Print a hollow diamond made of `*` characters and spaces, with `2*N - 1` lines in total.

- The diamond is symmetric top-to-bottom: the middle line is the widest, and the pattern narrows by one step per line as you move away from the middle in either direction, ending with a single `*` on the very first and very last line.
- The diamond is hollow: every line that is not the very first or very last line contains exactly two `*` characters — one at the left edge of the shape on that line, and one at the right edge — with only spaces in between.
- Every line ends immediately after its rightmost `*` character (no trailing spaces).

For example, for `N = 4` the output is:
```
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```

**Input Format**
A single line containing one integer `N`.

**Output Format**
`2*N - 1` lines forming the hollow diamond, as described above.

**Constraints**
- `1 <= N <= 30`

**Sample Input 1**
```
3
```
**Sample Output 1**
```
  *
 * *
*   *
 * *
  *
```
**Sample Explanation 1**
With `N = 3` the diamond has `2*3 - 1 = 5` lines. The widest line (the 3rd) has its two `*` characters at the very left and right edges with a 3-space gap between them; the lines above and below narrow by one step until only a single `*` remains on the first and last lines.

**Sample Input 2**
```
1
```
**Sample Output 2**
```
*
```
**Sample Explanation 2**
With `N = 1` the diamond has only `2*1 - 1 = 1` line, which is a single `*` character.

**Sample Input 3**
```
2
```
**Sample Output 3**
```
 *
* *
 *
```

**Sample Input 4**
```
4
```
**Sample Output 4**
```
   *
  * *
 *   *
*     *
 *   *
  * *
   *
```

**Sample Input 5**
```
5
```
**Sample Output 5**
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

**Sample Input 6**
```
6
```
**Sample Output 6**
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

**Sample Input 7**
```
7
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
 *         *
  *       *
   *     *
    *   *
     * *
      *
```

**Sample Input 8**
```
8
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
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *
```

**Sample Input 9**
```
10
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

**Sample Input 10**
```
15
```
**Sample Output 10**
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
    *                   *
   *                     *
  *                       *
 *                         *
*                           *
 *                         *
  *                       *
   *                     *
    *                   *
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

**Tags**
Patterns, Loops

---

## Triangle of Alphabets

**Problem Statement**
You are given an integer `N` (`1 <= N <= 26`). Print `N` lines. The `i`-th line (counting from 1) must contain the `i`-th uppercase letter of the English alphabet (`A` is the 1st letter, `B` is the 2nd, and so on) repeated `i` times, with no spaces in between.

**Input Format**
A single line containing one integer `N`.

**Output Format**
`N` lines: line `i` contains the `i`-th uppercase letter repeated `i` times.

**Constraints**
- `1 <= N <= 26`

**Sample Input 1**
```
4
```
**Sample Output 1**
```
A
BB
CCC
DDDD
```
**Sample Explanation 1**
Line 1 prints the 1st letter `A` once, line 2 prints the 2nd letter `B` twice, line 3 prints the 3rd letter `C` three times, and line 4 prints the 4th letter `D` four times.

**Sample Input 2**
```
1
```
**Sample Output 2**
```
A
```
**Sample Explanation 2**
With `N = 1` there is only one line, printing the 1st letter `A` once.

**Sample Input 3**
```
2
```
**Sample Output 3**
```
A
BB
```

**Sample Input 4**
```
3
```
**Sample Output 4**
```
A
BB
CCC
```

**Sample Input 5**
```
5
```
**Sample Output 5**
```
A
BB
CCC
DDDD
EEEEE
```

**Sample Input 6**
```
6
```
**Sample Output 6**
```
A
BB
CCC
DDDD
EEEEE
FFFFFF
```

**Sample Input 7**
```
10
```
**Sample Output 7**
```
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
JJJJJJJJJJ
```

**Sample Input 8**
```
15
```
**Sample Output 8**
```
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
JJJJJJJJJJ
KKKKKKKKKKK
LLLLLLLLLLLL
MMMMMMMMMMMMM
NNNNNNNNNNNNNN
OOOOOOOOOOOOOOO
```

**Sample Input 9**
```
20
```
**Sample Output 9**
```
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
JJJJJJJJJJ
KKKKKKKKKKK
LLLLLLLLLLLL
MMMMMMMMMMMMM
NNNNNNNNNNNNNN
OOOOOOOOOOOOOOO
PPPPPPPPPPPPPPPP
QQQQQQQQQQQQQQQQQ
RRRRRRRRRRRRRRRRRR
SSSSSSSSSSSSSSSSSSS
TTTTTTTTTTTTTTTTTTTT
```

**Sample Input 10**
```
26
```
**Sample Output 10**
```
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
JJJJJJJJJJ
KKKKKKKKKKK
LLLLLLLLLLLL
MMMMMMMMMMMMM
NNNNNNNNNNNNNN
OOOOOOOOOOOOOOO
PPPPPPPPPPPPPPPP
QQQQQQQQQQQQQQQQQ
RRRRRRRRRRRRRRRRRR
SSSSSSSSSSSSSSSSSSS
TTTTTTTTTTTTTTTTTTTT
UUUUUUUUUUUUUUUUUUUUU
VVVVVVVVVVVVVVVVVVVVVV
WWWWWWWWWWWWWWWWWWWWWWW
XXXXXXXXXXXXXXXXXXXXXXXX
YYYYYYYYYYYYYYYYYYYYYYYYY
ZZZZZZZZZZZZZZZZZZZZZZZZZZ
```

**Tags**
Patterns, Loops

---

## Digit Sum Divisible by 5 or 7

**Problem Statement**
You are given an integer `N`. Compute `S`, the sum of the digits of `N`.

- If `S` is divisible by both 5 and 7, print `-1`.
- Otherwise, if `S` is divisible by 5 or by 7 (but not both), print `1`.
- Otherwise (`S` is divisible by neither 5 nor 7), print `0`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing one integer: `1`, `-1`, or `0`, as described above.

**Constraints**
- `1 <= N <= 10^10`

**Sample Input 1**
```
374
```
**Sample Output 1**
```
1
```
**Sample Explanation 1**
The digit sum is `3 + 7 + 4 = 14`, which is divisible by 7 but not by 5, so the answer is `1`.

**Sample Input 2**
```
98972
```
**Sample Output 2**
```
-1
```
**Sample Explanation 2**
The digit sum is `9 + 8 + 9 + 7 + 2 = 35`, which is divisible by both 5 and 7, so the answer is `-1`.

**Sample Input 3**
```
55
```
**Sample Output 3**
```
1
```

**Sample Input 4**
```
8
```
**Sample Output 4**
```
0
```

**Sample Input 5**
```
16
```
**Sample Output 5**
```
1
```

**Sample Input 6**
```
35
```
**Sample Output 6**
```
0
```

**Sample Input 7**
```
10000000000
```
**Sample Output 7**
```
0
```

**Sample Input 8**
```
9999999999
```
**Sample Output 8**
```
1
```

**Sample Input 9**
```
123456789
```
**Sample Output 9**
```
1
```

**Sample Input 10**
```
7
```
**Sample Output 10**
```
1
```

**Tags**
Basics, Digits, Math

---

## First N Multiples of X

**Problem Statement**
You are given two integers `N` and `X`. Print the first `N` multiples of `X`, one per line, in the exact format:

```
X x i = X*i
```

where `i` runs from `1` to `N` and `X*i` is the actual product value.

**Input Format**
A single line containing two integers `N` and `X`, separated by a space.

**Output Format**
`N` lines, the `i`-th of which reads `X x i = X*i` (with `X`, `i`, and the product substituted in), for `i` from `1` to `N`.

**Constraints**
- `1 <= N <= 50`
- `1 <= X <= 10000`

**Sample Input 1**
```
4 12
```
**Sample Output 1**
```
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
```
**Sample Explanation 1**
`N = 4` and `X = 12`, so the first 4 multiples of 12 are printed: `12, 24, 36, 48`, each on its own line in the required format.

**Sample Input 2**
```
7 5
```
**Sample Output 2**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
```
**Sample Explanation 2**
`N = 7` and `X = 5`, so the first 7 multiples of 5 are printed: `5, 10, 15, 20, 25, 30, 35`, each on its own line in the required format.

**Sample Input 3**
```
1 9
```
**Sample Output 3**
```
9 x 1 = 9
```

**Sample Input 4**
```
10 3
```
**Sample Output 4**
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

**Sample Input 5**
```
5 100
```
**Sample Output 5**
```
100 x 1 = 100
100 x 2 = 200
100 x 3 = 300
100 x 4 = 400
100 x 5 = 500
```

**Sample Input 6**
```
3 7
```
**Sample Output 6**
```
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
```

**Sample Input 7**
```
6 25
```
**Sample Output 7**
```
25 x 1 = 25
25 x 2 = 50
25 x 3 = 75
25 x 4 = 100
25 x 5 = 125
25 x 6 = 150
```

**Sample Input 8**
```
8 2
```
**Sample Output 8**
```
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
```

**Sample Input 9**
```
2 999
```
**Sample Output 9**
```
999 x 1 = 999
999 x 2 = 1998
```

**Sample Input 10**
```
9 15
```
**Sample Output 10**
```
15 x 1 = 15
15 x 2 = 30
15 x 3 = 45
15 x 4 = 60
15 x 5 = 75
15 x 6 = 90
15 x 7 = 105
15 x 8 = 120
15 x 9 = 135
```

**Tags**
Basics, Loops

---

## Sum of N Numbers, Reversed

**Problem Statement**
You are given `N` integers. Compute their sum, and then print the reverse of that sum.

The reverse of a number is obtained by reversing the order of its digits. If reversing produces leading zeros, they are dropped — for example, the reverse of `100` is `1`, and the reverse of `600` is `6`.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers.

**Output Format**
A single integer: the reverse of the sum of the given `N` numbers.

**Constraints**
- `1 <= N <= 1000`
- `0 <= each number <= 10^6`

**Sample Input 1**
```
5
13 2 7 6 25
```
**Sample Output 1**
```
35
```
**Sample Explanation 1**
The sum of `13, 2, 7, 6, 25` is `53`. Reversing the digits of `53` gives `35`.

**Sample Input 2**
```
19
1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4 17 18 19
```
**Sample Output 2**
```
49
```
**Sample Explanation 2**
The sum of the 19 numbers is `94`. Reversing the digits of `94` gives `49`.

**Sample Input 3**
```
1
5
```
**Sample Output 3**
```
5
```

**Sample Input 4**
```
3
10 20 30
```
**Sample Output 4**
```
6
```

**Sample Input 5**
```
3
100 200 300
```
**Sample Output 5**
```
6
```

**Sample Input 6**
```
10
1 2 3 4 5 6 7 8 9 10
```
**Sample Output 6**
```
55
```

**Sample Input 7**
```
2
999 1
```
**Sample Output 7**
```
1
```

**Sample Input 8**
```
4
0 0 0 5
```
**Sample Output 8**
```
5
```

**Sample Input 9**
```
2
50 50
```
**Sample Output 9**
```
1
```

**Sample Input 10**
```
3
123 456 789
```
**Sample Output 10**
```
8631
```

**Tags**
Basics, Math

---
