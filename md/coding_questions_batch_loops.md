# Coding Questions - If/Else, Digits, Ranges and Loop Tracing

Author-ready markdown for `automator.py`. 11 challenges: 6 coding questions (two adapted
from CodingBat, with the helper-function requirement removed since functions are not
covered yet) and 5 output-based loop-tracing questions.

Every problem carries 10 test cases; run
`tools/hr_mark_samples.py --md coding_questions_batch_loops.md --apply`
afterwards to flag the first two as samples. Enable C++14, Java 8 and Python 3 on each
challenge before publishing.

---

## Round and Sum Three Numbers
**Problem Statement**
A number is rounded to a multiple of 10 using this rule: if its rightmost digit is 5 or more, it is rounded up to the next multiple of 10 (so 15 becomes 20); if its rightmost digit is less than 5, it is rounded down to the previous multiple of 10 (so 12 becomes 10).

You are given three integers `a`, `b` and `c`. Round each of them by the rule above and print the sum of the three rounded values.

**Input Format**
A single line with three space-separated integers `a`, `b` and `c`.

**Output Format**
A single line with one integer: the sum of the three rounded values.

**Constraints**
- `0 <= a, b, c <= 1000`

**Sample Input 0**
```
16 17 18
```

**Sample Output 0**
```
60
```

**Sample Input 1**
```
12 13 14
```

**Sample Output 1**
```
30
```

**Sample Input 2**
```
6 4 4
```

**Sample Output 2**
```
10
```

**Sample Input 3**
```
0 0 0
```

**Sample Output 3**
```
0
```

**Sample Input 4**
```
5 5 5
```

**Sample Output 4**
```
30
```

**Sample Input 5**
```
45 21 30
```

**Sample Output 5**
```
100
```

**Sample Input 6**
```
9 99 999
```

**Sample Output 6**
```
1110
```

**Sample Input 7**
```
1000 1000 1000
```

**Sample Output 7**
```
3000
```

**Sample Input 8**
```
24 25 26
```

**Sample Output 8**
```
80
```

**Sample Input 9**
```
7 13 100
```

**Sample Output 9**
```
120
```

**Tags**
Basics, Conditionals, Arithmetic

## Alphabets Up To a Given Character
**Problem Statement**
You are given a single lowercase English letter.

Print all lowercase English letters starting from `a` and ending at the given letter, in order, separated by single spaces on one line.

For example, if the given letter is `d`, the output is `a b c d`.

**Input Format**
A single line containing one lowercase English letter `c`.

**Output Format**
A single line with the letters from `a` up to `c` inclusive, separated by single spaces. There is no trailing space.

**Constraints**
- `c` is one of `a`, `b`, ..., `z`.

**Sample Input 0**
```
d
```

**Sample Output 0**
```
a b c d
```

**Sample Input 1**
```
h
```

**Sample Output 1**
```
a b c d e f g h
```

**Sample Input 2**
```
a
```

**Sample Output 2**
```
a
```

**Sample Input 3**
```
z
```

**Sample Output 3**
```
a b c d e f g h i j k l m n o p q r s t u v w x y z
```

**Sample Input 4**
```
c
```

**Sample Output 4**
```
a b c
```

**Sample Input 5**
```
m
```

**Sample Output 5**
```
a b c d e f g h i j k l m
```

**Sample Input 6**
```
b
```

**Sample Output 6**
```
a b
```

**Sample Input 7**
```
t
```

**Sample Output 7**
```
a b c d e f g h i j k l m n o p q r s t
```

**Sample Input 8**
```
e
```

**Sample Output 8**
```
a b c d e
```

**Sample Input 9**
```
y
```

**Sample Output 9**
```
a b c d e f g h i j k l m n o p q r s t u v w x y
```

**Tags**
Basics, Loops, Characters

## Sum of Odd Digits and Even Digits
**Problem Statement**
You are given a non-negative integer `N`.

Look at every digit of `N`. Print the sum of the digits that are odd, followed by the sum of the digits that are even.

For example, for `N = 1234` the odd digits are 1 and 3 (sum 4) and the even digits are 2 and 4 (sum 6), so the output is `4 6`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line with two space-separated integers: the sum of the odd digits and the sum of the even digits, in that order.

**Constraints**
- `0 <= N <= 1000000000`

**Sample Input 0**
```
1234
```

**Sample Output 0**
```
4 6
```

**Sample Input 1**
```
888
```

**Sample Output 1**
```
0 24
```

**Sample Input 2**
```
13579
```

**Sample Output 2**
```
25 0
```

**Sample Input 3**
```
7
```

**Sample Output 3**
```
7 0
```

**Sample Input 4**
```
0
```

**Sample Output 4**
```
0 0
```

**Sample Input 5**
```
2468
```

**Sample Output 5**
```
0 20
```

**Sample Input 6**
```
102030
```

**Sample Output 6**
```
4 2
```

**Sample Input 7**
```
999999
```

**Sample Output 7**
```
54 0
```

**Sample Input 8**
```
5040
```

**Sample Output 8**
```
5 4
```

**Sample Input 9**
```
123456789
```

**Sample Output 9**
```
25 20
```

**Tags**
Basics, Loops, Digits

## Sum of Digits at Odd Places and Even Places
**Problem Statement**
You are given a non-negative integer `N`. Number the positions of its digits from right to left, starting at 1: the rightmost digit is at position 1, the next one to its left is at position 2, and so on.

Print the sum of the digits standing at odd positions, followed by the sum of the digits standing at even positions.

For example, for `N = 888` the digits at positions 1 and 3 are 8 and 8 (sum 16) and the digit at position 2 is 8 (sum 8), so the output is `16 8`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line with two space-separated integers: the sum of the digits at odd positions and the sum of the digits at even positions, in that order.

**Constraints**
- `0 <= N <= 1000000000`

**Sample Input 0**
```
888
```

**Sample Output 0**
```
16 8
```

**Sample Input 1**
```
1234
```

**Sample Output 1**
```
6 4
```

**Sample Input 2**
```
5
```

**Sample Output 2**
```
5 0
```

**Sample Input 3**
```
0
```

**Sample Output 3**
```
0 0
```

**Sample Input 4**
```
12345
```

**Sample Output 4**
```
9 6
```

**Sample Input 5**
```
90
```

**Sample Output 5**
```
0 9
```

**Sample Input 6**
```
1010101
```

**Sample Output 6**
```
4 0
```

**Sample Input 7**
```
246813
```

**Sample Output 7**
```
15 9
```

**Sample Input 8**
```
1000000
```

**Sample Output 8**
```
1 0
```

**Sample Input 9**
```
987654321
```

**Sample Output 9**
```
25 20
```

**Tags**
Basics, Loops, Digits

## Numbers From L to Twice R
**Problem Statement**
You are given two integers `L` and `R`.

Print every integer starting from `L` and ending at `2 * R` inclusive, in increasing order, separated by single spaces on one line.

For example, if `L = 1` and `R = 3` then `2 * R` is 6 and the output is `1 2 3 4 5 6`.

**Input Format**
A single line with two space-separated integers `L` and `R`.

**Output Format**
A single line with the integers from `L` to `2 * R` inclusive, separated by single spaces. There is no trailing space.

**Constraints**
- `1 <= L <= R <= 100`

**Sample Input 0**
```
1 3
```

**Sample Output 0**
```
1 2 3 4 5 6
```

**Sample Input 1**
```
2 2
```

**Sample Output 1**
```
2 3 4
```

**Sample Input 2**
```
5 5
```

**Sample Output 2**
```
5 6 7 8 9 10
```

**Sample Input 3**
```
1 1
```

**Sample Output 3**
```
1 2
```

**Sample Input 4**
```
3 7
```

**Sample Output 4**
```
3 4 5 6 7 8 9 10 11 12 13 14
```

**Sample Input 5**
```
10 10
```

**Sample Output 5**
```
10 11 12 13 14 15 16 17 18 19 20
```

**Sample Input 6**
```
4 4
```

**Sample Output 6**
```
4 5 6 7 8
```

**Sample Input 7**
```
7 9
```

**Sample Output 7**
```
7 8 9 10 11 12 13 14 15 16 17 18
```

**Sample Input 8**
```
1 10
```

**Sample Output 8**
```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
```

**Sample Input 9**
```
20 25
```

**Sample Output 9**
```
20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
```

**Tags**
Basics, Loops, Ranges

## Sum Ignoring Teen Values
**Problem Statement**
You are given three integers `a`, `b` and `c`. Print their sum, with one exception: any value that lies in the range 13 to 19 inclusive counts as 0, except the values 15 and 16, which count normally.

**Input Format**
A single line with three space-separated integers `a`, `b` and `c`.

**Output Format**
A single line with one integer: the adjusted sum.

**Constraints**
- `0 <= a, b, c <= 100`

**Sample Input 0**
```
1 2 3
```

**Sample Output 0**
```
6
```

**Sample Input 1**
```
2 13 1
```

**Sample Output 1**
```
3
```

**Sample Input 2**
```
2 1 14
```

**Sample Output 2**
```
3
```

**Sample Input 3**
```
2 1 15
```

**Sample Output 3**
```
18
```

**Sample Input 4**
```
2 1 16
```

**Sample Output 4**
```
19
```

**Sample Input 5**
```
17 18 19
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
13 15 18
```

**Sample Output 6**
```
15
```

**Sample Input 7**
```
0 0 0
```

**Sample Output 7**
```
0
```

**Sample Input 8**
```
19 19 19
```

**Sample Output 8**
```
0
```

**Sample Input 9**
```
20 12 13
```

**Sample Output 9**
```
32
```

**Tags**
Basics, Conditionals, Arithmetic

## Predict the Output - Loops 1
**Problem Statement**
Read the program below carefully and work out, by hand, what it prints. Your task is to print exactly the same output as this program would print for the value read from standard input.

Program:

int n;
cin >> n;
int s = 0;
for (int i = 1; i <= n; i++) {
    if (i % 3 == 0) {
        continue;
    }
    s = s + i;
}
cout << s << endl;

**Input Format**
A single line containing one integer `n`.

**Output Format**
A single line with one integer: exactly what the program prints.

**Constraints**
- `1 <= n <= 100`

**Sample Input 0**
```
5
```

**Sample Output 0**
```
12
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
3
```

**Sample Output 2**
```
3
```

**Sample Input 3**
```
10
```

**Sample Output 3**
```
37
```

**Sample Input 4**
```
2
```

**Sample Output 4**
```
3
```

**Sample Input 5**
```
7
```

**Sample Output 5**
```
19
```

**Sample Input 6**
```
15
```

**Sample Output 6**
```
75
```

**Sample Input 7**
```
20
```

**Sample Output 7**
```
147
```

**Sample Input 8**
```
6
```

**Sample Output 8**
```
12
```

**Sample Input 9**
```
100
```

**Sample Output 9**
```
3367
```

**Tags**
Loops, Output Based, Basics

## Predict the Output - Loops 2
**Problem Statement**
Read the program below carefully and work out, by hand, what it prints. Your task is to print exactly the same output as this program would print for the value read from standard input.

Program:

int n;
cin >> n;
int c = 0;
while (n > 1) {
    n = n / 2;
    c = c + 1;
}
cout << c << endl;

**Input Format**
A single line containing one integer `n`.

**Output Format**
A single line with one integer: exactly what the program prints.

**Constraints**
- `1 <= n <= 100000`

**Sample Input 0**
```
8
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
1
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
2
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
10
```

**Sample Output 3**
```
3
```

**Sample Input 4**
```
100
```

**Sample Output 4**
```
6
```

**Sample Input 5**
```
1000
```

**Sample Output 5**
```
9
```

**Sample Input 6**
```
63
```

**Sample Output 6**
```
5
```

**Sample Input 7**
```
64
```

**Sample Output 7**
```
6
```

**Sample Input 8**
```
7
```

**Sample Output 8**
```
2
```

**Sample Input 9**
```
1024
```

**Sample Output 9**
```
10
```

**Tags**
Loops, Output Based, Basics

## Predict the Output - Loops 3
**Problem Statement**
Read the program below carefully and work out, by hand, what it prints. Your task is to print exactly the same output as this program would print for the value read from standard input.

Program:

int n;
cin >> n;
for (int i = n; i >= 1; i--) {
    if (i % 2 == 0) {
        cout << i << endl;
    }
}

**Input Format**
A single line containing one integer `n`.

**Output Format**
Exactly what the program prints, one value per line.

**Constraints**
- `2 <= n <= 100`

**Sample Input 0**
```
5
```

**Sample Output 0**
```
4
2
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
2
```

**Sample Input 2**
```
6
```

**Sample Output 2**
```
6
4
2
```

**Sample Input 3**
```
10
```

**Sample Output 3**
```
10
8
6
4
2
```

**Sample Input 4**
```
3
```

**Sample Output 4**
```
2
```

**Sample Input 5**
```
7
```

**Sample Output 5**
```
6
4
2
```

**Sample Input 6**
```
9
```

**Sample Output 6**
```
8
6
4
2
```

**Sample Input 7**
```
12
```

**Sample Output 7**
```
12
10
8
6
4
2
```

**Sample Input 8**
```
4
```

**Sample Output 8**
```
4
2
```

**Sample Input 9**
```
15
```

**Sample Output 9**
```
14
12
10
8
6
4
2
```

**Tags**
Loops, Output Based, Basics

## Predict the Output - Loops 4
**Problem Statement**
Read the program below carefully and work out, by hand, what it prints. Your task is to print exactly the same output as this program would print for the value read from standard input.

Program:

int n;
cin >> n;
int i = 1;
while (true) {
    if (i * i > n) {
        break;
    }
    cout << i * i << endl;
    i = i + 1;
}

**Input Format**
A single line containing one integer `n`.

**Output Format**
Exactly what the program prints, one value per line.

**Constraints**
- `1 <= n <= 1000`

**Sample Input 0**
```
10
```

**Sample Output 0**
```
1
4
9
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
3
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
16
```

**Sample Output 3**
```
1
4
9
16
```

**Sample Input 4**
```
25
```

**Sample Output 4**
```
1
4
9
16
25
```

**Sample Input 5**
```
24
```

**Sample Output 5**
```
1
4
9
16
```

**Sample Input 6**
```
50
```

**Sample Output 6**
```
1
4
9
16
25
36
49
```

**Sample Input 7**
```
100
```

**Sample Output 7**
```
1
4
9
16
25
36
49
64
81
100
```

**Sample Input 8**
```
2
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
99
```

**Sample Output 9**
```
1
4
9
16
25
36
49
64
81
```

**Tags**
Loops, Output Based, Basics

## Predict the Output - Loops 5
**Problem Statement**
Read the program below carefully and work out, by hand, what it prints. Your task is to print exactly the same output as this program would print for the value read from standard input.

Program:

int n;
cin >> n;
int a = 0;
int b = 1;
for (int i = 1; i <= n; i++) {
    int t = a + b;
    a = b;
    b = t;
}
cout << a << " " << b << endl;

**Input Format**
A single line containing one integer `n`.

**Output Format**
A single line with exactly what the program prints.

**Constraints**
- `0 <= n <= 40`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
1 1
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
1 2
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
2 3
```

**Sample Input 3**
```
5
```

**Sample Output 3**
```
5 8
```

**Sample Input 4**
```
0
```

**Sample Output 4**
```
0 1
```

**Sample Input 5**
```
7
```

**Sample Output 5**
```
13 21
```

**Sample Input 6**
```
10
```

**Sample Output 6**
```
55 89
```

**Sample Input 7**
```
4
```

**Sample Output 7**
```
3 5
```

**Sample Input 8**
```
15
```

**Sample Output 8**
```
610 987
```

**Sample Input 9**
```
20
```

**Sample Output 9**
```
6765 10946
```

**Tags**
Loops, Output Based, Basics
