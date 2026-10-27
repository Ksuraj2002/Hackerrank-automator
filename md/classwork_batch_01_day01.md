# DSA-101 Classwork - Batch 1 (Day 1)

Author-ready markdown for `automator.py`. Statements are strictly descriptive: no hints on approach or solution. Each problem carries 10 sample I/O pairs; run `tools/hr_mark_samples.py --md classwork_batch_01_day01.md --apply` afterwards to flag the first two as samples. Ensure C++14, Java 8 and Python 3 are enabled on each challenge before publishing.

---

## Classwork: Print Name Class and Roll
**Problem Statement**
You are given three lines of input: a student's name (one word, no spaces), the student's class as an integer, and the student's roll number as an integer.

Print the name on the first line, the class on the second line, and the roll number on the third line.

**Input Format**
- Line 1: a single word `name` (letters only, no spaces).
- Line 2: an integer `class_number`.
- Line 3: an integer `roll_number`.

**Output Format**
Three lines: the name, the class number, and the roll number, each on its own line, in that order.

**Constraints**
- `1 <= length of name <= 30`
- `1 <= class_number <= 12`
- `1 <= roll_number <= 100000`

**Sample Input 0**
```
Anna
10
42
```

**Sample Output 0**
```
Anna
10
42
```

**Sample Input 1**
```
Ravi
7
1
```

**Sample Output 1**
```
Ravi
7
1
```

**Sample Input 2**
```
Zoe
12
99999
```

**Sample Output 2**
```
Zoe
12
99999
```

**Sample Input 3**
```
Kai
1
5
```

**Sample Output 3**
```
Kai
1
5
```

**Sample Input 4**
```
Lia
5
123
```

**Sample Output 4**
```
Lia
5
123
```

**Sample Input 5**
```
Bob
9
256
```

**Sample Output 5**
```
Bob
9
256
```

**Sample Input 6**
```
Solo
8
1000
```

**Sample Output 6**
```
Solo
8
1000
```

**Sample Input 7**
```
Neha
11
77
```

**Sample Output 7**
```
Neha
11
77
```

**Sample Input 8**
```
Mia
6
45
```

**Sample Output 8**
```
Mia
6
45
```

**Sample Input 9**
```
Amy
2
99
```

**Sample Output 9**
```
Amy
2
99
```

**Tags**
Basics, IO

---

## Classwork: Print a Small ASCII Box
**Problem Statement**
You are given a single integer `N`. Print an `N x N` box drawn with the character `*`.

- The top row and the bottom row contain exactly `N` `*` characters.
- Every row in between (if any) starts with a `*`, ends with a `*`, and has spaces between them so that the row is `N` characters wide in total.
- For `N = 1` the box is a single `*`.
- For `N = 2` the box is two rows, each containing `**`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
`N` lines forming the `N x N` box.

**Constraints**
- `1 <= N <= 30`
- Each interior row must contain exactly `N - 2` spaces between the two `*` characters.

**Sample Input 0**
```
3
```

**Sample Output 0**
```
***
* *
***
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
**
**
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
****
*  *
*  *
****
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
*****
*   *
*   *
*   *
*****
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
******
*    *
*    *
*    *
*    *
******
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
*******
*     *
*     *
*     *
*     *
*     *
*******
```

**Sample Input 7**
```
10
```

**Sample Output 7**
```
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********
```

**Sample Input 8**
```
15
```

**Sample Output 8**
```
***************
*             *
*             *
*             *
*             *
*             *
*             *
*             *
*             *
*             *
*             *
*             *
*             *
*             *
***************
```

**Sample Input 9**
```
20
```

**Sample Output 9**
```
********************
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
*                  *
********************
```

**Tags**
Patterns, Loops

---

## Classwork: Declare and Print a Variable of Each Type
**Problem Statement**
Four values are given on four separate lines: an integer, a real number, a single character, and a word.

Print them on four separate lines in the same order. The real number must be printed with exactly two digits after the decimal point. Everything else must be printed as it was read.

**Input Format**
- Line 1: an integer `N`.
- Line 2: a real number `D`.
- Line 3: a single non-whitespace character `C`.
- Line 4: a word `W` (letters, digits or symbols, no spaces).

**Output Format**
Four lines: `N` as an integer, `D` with exactly two decimal places, `C`, and `W`, each on its own line, in that order.

**Constraints**
- `-10^9 <= N <= 10^9`
- `-10^6 <= D <= 10^6`
- `C` is a single printable non-whitespace character.
- `1 <= length of W <= 30`

**Sample Input 0**
```
42
3.14
x
hello
```

**Sample Output 0**
```
42
3.14
x
hello
```

**Sample Input 1**
```
0
0
A
apple
```

**Sample Output 1**
```
0
0.00
A
apple
```

**Sample Input 2**
```
-5
-2.5
z
xyz
```

**Sample Output 2**
```
-5
-2.50
z
xyz
```

**Sample Input 3**
```
1000
100.99
M
Machine
```

**Sample Output 3**
```
1000
100.99
M
Machine
```

**Sample Input 4**
```
-100
-0.01
.
dot
```

**Sample Output 4**
```
-100
-0.01
.
dot
```

**Sample Input 5**
```
999
1000.5
!
exclaim
```

**Sample Output 5**
```
999
1000.50
!
exclaim
```

**Sample Input 6**
```
7
7.7
7
seven
```

**Sample Output 6**
```
7
7.70
7
seven
```

**Sample Input 7**
```
-1
-1.0
-
minus
```

**Sample Output 7**
```
-1
-1.00
-
minus
```

**Sample Input 8**
```
65
3.14159
Z
curriculum
```

**Sample Output 8**
```
65
3.14
Z
curriculum
```

**Sample Input 9**
```
12345
0.5
+
plus
```

**Sample Output 9**
```
12345
0.50
+
plus
```

**Tags**
Basics, IO, Data Types

---

## Classwork: Take Input of a Number and Print It
**Problem Statement**
A single integer `N` is given on standard input. Print the same integer on standard output.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing the integer `N`.

**Constraints**
- `-10^9 <= N <= 10^9`

**Sample Input 0**
```
7
```

**Sample Output 0**
```
7
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
-1
```

**Sample Output 2**
```
-1
```

**Sample Input 3**
```
1000000000
```

**Sample Output 3**
```
1000000000
```

**Sample Input 4**
```
-1000000000
```

**Sample Output 4**
```
-1000000000
```

**Sample Input 5**
```
12345
```

**Sample Output 5**
```
12345
```

**Sample Input 6**
```
-987654321
```

**Sample Output 6**
```
-987654321
```

**Sample Input 7**
```
1
```

**Sample Output 7**
```
1
```

**Sample Input 8**
```
42
```

**Sample Output 8**
```
42
```

**Sample Input 9**
```
999999999
```

**Sample Output 9**
```
999999999
```

**Tags**
Basics, IO

---
