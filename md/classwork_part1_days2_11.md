# DSA-101 Classwork - Part 1 (Days 2 to 11)

Author-ready markdown for `automator.py`. Statements are strictly
descriptive: no hints on approach or solution. Each problem has 10 sample
I/O pairs whose outputs come from reference solvers.

After uploading:
1. Flag the first two test cases per challenge as samples:
   `venv\Scripts\python.exe tools\hr_mark_samples.py --md classwork_part1_days2_11.md --apply`
2. Enable C++14, Java 8 and Python 3:
   `venv\Scripts\python.exe tools\hr_enable_languages.py --md classwork_part1_days2_11.md --apply`
3. Attach to the classwork contest:
   `venv\Scripts\python.exe tools\hr_add_to_contest.py --md classwork_part1_days2_11.md --apply`

**Skipped as drills (not authored):**
- Day 2 Classwork 7 - "Store these expressions inside a Boolean variable ans"
  is a fixed-answer classroom drill with no varying input, not a gradable
  HackerRank challenge.

---


## Classwork: Sum of Digits of a 3-Digit Number
**Problem Statement**
You are given a single 3-digit integer `N`. Print the sum of its three digits.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing the sum of the digits of `N`.

**Constraints**
- `100 <= N <= 999`

**Sample Input 0**
```
123
```

**Sample Output 0**
```
6
```

**Sample Input 1**
```
999
```

**Sample Output 1**
```
27
```

**Sample Input 2**
```
100
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
456
```

**Sample Output 3**
```
15
```

**Sample Input 4**
```
500
```

**Sample Output 4**
```
5
```

**Sample Input 5**
```
321
```

**Sample Output 5**
```
6
```

**Sample Input 6**
```
808
```

**Sample Output 6**
```
16
```

**Sample Input 7**
```
111
```

**Sample Output 7**
```
3
```

**Sample Input 8**
```
747
```

**Sample Output 8**
```
18
```

**Sample Input 9**
```
902
```

**Sample Output 9**
```
11
```

**Tags**
Basics, Loops, Number Theory

---

## Classwork: Evaluate a Mixed Expression
**Problem Statement**
Five integers `A`, `B`, `C`, `D` and `E` are given on a single line, separated by spaces. Print the value of the expression

```
A + B * C - D / E
```

where every operation is applied in the standard C++ operator precedence order and `/` is integer division that truncates toward zero.

**Input Format**
A single line containing five space-separated integers `A B C D E`.

**Output Format**
A single line containing the value of `A + B * C - D / E` evaluated with C++ integer semantics.

**Constraints**
- `-1000 <= A, B, C, D <= 1000`
- `1 <= E <= 1000`

**Sample Input 0**
```
1 2 3 4 5
```

**Sample Output 0**
```
7
```

**Sample Input 1**
```
10 20 30 40 50
```

**Sample Output 1**
```
610
```

**Sample Input 2**
```
0 0 0 0 1
```

**Sample Output 2**
```
0
```

**Sample Input 3**
```
5 5 5 5 5
```

**Sample Output 3**
```
29
```

**Sample Input 4**
```
100 2 3 50 10
```

**Sample Output 4**
```
101
```

**Sample Input 5**
```
-3 4 5 6 2
```

**Sample Output 5**
```
14
```

**Sample Input 6**
```
1000 1000 1000 1000 1
```

**Sample Output 6**
```
1000000
```

**Sample Input 7**
```
1 1 1 1 1
```

**Sample Output 7**
```
1
```

**Sample Input 8**
```
7 -2 3 9 4
```

**Sample Output 8**
```
-1
```

**Sample Input 9**
```
-10 -10 -10 -10 3
```

**Sample Output 9**
```
94
```

**Tags**
Operators, Basics

---

## Classwork: Total and Percentage of Five Subjects
**Problem Statement**
The marks obtained by a student in five subjects are given on a single line, separated by spaces. Each mark is a real number.

Print the total marks and the percentage of the student on the same line, separated by a single space. Both values must be printed with exactly two digits after the decimal point. The percentage is `total / 5`.

**Input Format**
A single line containing five space-separated real numbers - the marks in the five subjects.

**Output Format**
A single line containing the total and the percentage, in that order, separated by one space, each with exactly two decimal places.

**Constraints**
- Each mark is a real number in `[0, 100]`.

**Sample Input 0**
```
80 70 90 85 95
```

**Sample Output 0**
```
420.00 84.00
```

**Sample Input 1**
```
0 0 0 0 0
```

**Sample Output 1**
```
0.00 0.00
```

**Sample Input 2**
```
100 100 100 100 100
```

**Sample Output 2**
```
500.00 100.00
```

**Sample Input 3**
```
50 60 70 80 90
```

**Sample Output 3**
```
350.00 70.00
```

**Sample Input 4**
```
45.5 60.5 55.5 70.5 80.5
```

**Sample Output 4**
```
312.50 62.50
```

**Sample Input 5**
```
88 92 76 84 91
```

**Sample Output 5**
```
431.00 86.20
```

**Sample Input 6**
```
10.25 20.75 30.5 40 50
```

**Sample Output 6**
```
151.50 30.30
```

**Sample Input 7**
```
99 100 98 97 95
```

**Sample Output 7**
```
489.00 97.80
```

**Sample Input 8**
```
33 44 55 66 77
```

**Sample Output 8**
```
275.00 55.00
```

**Sample Input 9**
```
1 2 3 4 5
```

**Sample Output 9**
```
15.00 3.00
```

**Tags**
Operators, Basics

---

## Classwork: Product of Four Integers Greater than 1000
**Problem Statement**
Four integers are given on a single line, separated by spaces. Print `true` if their product is strictly greater than `1000` and `false` otherwise. The words must be printed in lowercase.

**Input Format**
A single line containing four space-separated integers `A B C D`.

**Output Format**
A single line containing `true` or `false` (lowercase).

**Constraints**
- `-100 <= A, B, C, D <= 100`

**Sample Input 0**
```
5 6 7 8
```

**Sample Output 0**
```
true
```

**Sample Input 1**
```
10 10 10 10
```

**Sample Output 1**
```
true
```

**Sample Input 2**
```
1 1 1 1
```

**Sample Output 2**
```
false
```

**Sample Input 3**
```
-5 -5 -5 -5
```

**Sample Output 3**
```
false
```

**Sample Input 4**
```
100 100 1 1
```

**Sample Output 4**
```
true
```

**Sample Input 5**
```
50 4 3 2
```

**Sample Output 5**
```
true
```

**Sample Input 6**
```
0 100 100 100
```

**Sample Output 6**
```
false
```

**Sample Input 7**
```
-10 -10 5 5
```

**Sample Output 7**
```
true
```

**Sample Input 8**
```
20 20 20 20
```

**Sample Output 8**
```
true
```

**Sample Input 9**
```
3 4 5 6
```

**Sample Output 9**
```
false
```

**Tags**
Operators, Basics

---

## Classwork: Check Divisibility by 7
**Problem Statement**
You are given a single integer `N`. Print `true` if `N` is divisible by `7`, otherwise print `false`. The words must be printed in lowercase.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing `true` or `false`.

**Constraints**
- `-10^9 <= N <= 10^9`

**Sample Input 0**
```
14
```

**Sample Output 0**
```
true
```

**Sample Input 1**
```
15
```

**Sample Output 1**
```
false
```

**Sample Input 2**
```
0
```

**Sample Output 2**
```
true
```

**Sample Input 3**
```
-49
```

**Sample Output 3**
```
true
```

**Sample Input 4**
```
1000000000
```

**Sample Output 4**
```
false
```

**Sample Input 5**
```
7
```

**Sample Output 5**
```
true
```

**Sample Input 6**
```
8
```

**Sample Output 6**
```
false
```

**Sample Input 7**
```
-7
```

**Sample Output 7**
```
true
```

**Sample Input 8**
```
999999998
```

**Sample Output 8**
```
false
```

**Sample Input 9**
```
77
```

**Sample Output 9**
```
true
```

**Tags**
Operators, Basics

---

## Classwork: Adult or Below Age
**Problem Statement**
You are given the age of a person as an integer `A`. Print `Adult` if `A` is greater than or equal to `18`, otherwise print `Below age`.

**Input Format**
A single line containing one integer `A`.

**Output Format**
A single line containing `Adult` or `Below age`.

**Constraints**
- `0 <= A <= 150`

**Sample Input 0**
```
18
```

**Sample Output 0**
```
Adult
```

**Sample Input 1**
```
17
```

**Sample Output 1**
```
Below age
```

**Sample Input 2**
```
0
```

**Sample Output 2**
```
Below age
```

**Sample Input 3**
```
150
```

**Sample Output 3**
```
Adult
```

**Sample Input 4**
```
25
```

**Sample Output 4**
```
Adult
```

**Sample Input 5**
```
12
```

**Sample Output 5**
```
Below age
```

**Sample Input 6**
```
19
```

**Sample Output 6**
```
Adult
```

**Sample Input 7**
```
100
```

**Sample Output 7**
```
Adult
```

**Sample Input 8**
```
1
```

**Sample Output 8**
```
Below age
```

**Sample Input 9**
```
60
```

**Sample Output 9**
```
Adult
```

**Tags**
Conditionals, Basics

---

## Classwork: Maximum of Two Numbers
**Problem Statement**
Two integers `A` and `B` are given on a single line, separated by a single space. Print the larger of the two. If both are equal, print that value.

**Input Format**
A single line containing two space-separated integers `A B`.

**Output Format**
A single line containing the maximum of `A` and `B`.

**Constraints**
- `-10^9 <= A, B <= 10^9`

**Sample Input 0**
```
3 7
```

**Sample Output 0**
```
7
```

**Sample Input 1**
```
10 4
```

**Sample Output 1**
```
10
```

**Sample Input 2**
```
5 5
```

**Sample Output 2**
```
5
```

**Sample Input 3**
```
-1 -2
```

**Sample Output 3**
```
-1
```

**Sample Input 4**
```
1000000000 -1000000000
```

**Sample Output 4**
```
1000000000
```

**Sample Input 5**
```
0 0
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
-5 5
```

**Sample Output 6**
```
5
```

**Sample Input 7**
```
42 42
```

**Sample Output 7**
```
42
```

**Sample Input 8**
```
999 1000
```

**Sample Output 8**
```
1000
```

**Sample Input 9**
```
-100 -50
```

**Sample Output 9**
```
-50
```

**Tags**
Conditionals, Basics

---

## Classwork: High Sum or Low Sum
**Problem Statement**
Two integers `X` and `Y` are given on a single line. Print `High Sum` if the sum `X + Y` is greater than or equal to `100`, otherwise print `Low Sum`.

**Input Format**
A single line containing two space-separated integers `X Y`.

**Output Format**
A single line containing `High Sum` or `Low Sum`.

**Constraints**
- `-10000 <= X, Y <= 10000`

**Sample Input 0**
```
40 60
```

**Sample Output 0**
```
High Sum
```

**Sample Input 1**
```
10 20
```

**Sample Output 1**
```
Low Sum
```

**Sample Input 2**
```
50 50
```

**Sample Output 2**
```
High Sum
```

**Sample Input 3**
```
99 1
```

**Sample Output 3**
```
High Sum
```

**Sample Input 4**
```
100 0
```

**Sample Output 4**
```
High Sum
```

**Sample Input 5**
```
-50 200
```

**Sample Output 5**
```
High Sum
```

**Sample Input 6**
```
0 0
```

**Sample Output 6**
```
Low Sum
```

**Sample Input 7**
```
150 150
```

**Sample Output 7**
```
High Sum
```

**Sample Input 8**
```
45 54
```

**Sample Output 8**
```
Low Sum
```

**Sample Input 9**
```
100 -1
```

**Sample Output 9**
```
Low Sum
```

**Tags**
Conditionals, Basics

---

## Classwork: Shopping Discount Calculator
**Problem Statement**
A shop sells one unit for `100` rupees. A customer buys `Q` units, so the total cost before discount is `Q * 100`.

If the total cost before discount is strictly greater than `1000`, the shop applies a `10%` discount and charges `total * 0.9` (truncated to an integer). Otherwise the total is charged as is.

Print the amount the customer must pay as an integer.

**Input Format**
A single line containing one integer `Q` (quantity).

**Output Format**
A single line containing the final amount as an integer.

**Constraints**
- `1 <= Q <= 100000`

**Sample Input 0**
```
5
```

**Sample Output 0**
```
500
```

**Sample Input 1**
```
10
```

**Sample Output 1**
```
1000
```

**Sample Input 2**
```
11
```

**Sample Output 2**
```
990
```

**Sample Input 3**
```
100
```

**Sample Output 3**
```
9000
```

**Sample Input 4**
```
1
```

**Sample Output 4**
```
100
```

**Sample Input 5**
```
15
```

**Sample Output 5**
```
1350
```

**Sample Input 6**
```
20
```

**Sample Output 6**
```
1800
```

**Sample Input 7**
```
50
```

**Sample Output 7**
```
4500
```

**Sample Input 8**
```
9
```

**Sample Output 8**
```
900
```

**Sample Input 9**
```
12
```

**Sample Output 9**
```
1080
```

**Tags**
Conditionals, Basics

---

## Classwork: Employee Bonus Calculation
**Problem Statement**
The bonus paid by a company is `Bonus = Salary * 5 / 100`. A company pays this bonus only to employees whose years of service are strictly greater than `5`. All other employees get a bonus of `0`.

You are given the employee's `Salary` (a real number) and the employee's years of service `Years` (an integer) on a single line, separated by a space. Print the bonus with exactly two digits after the decimal point.

**Input Format**
A single line containing a real number `Salary` and an integer `Years`, separated by one space.

**Output Format**
A single line containing the bonus amount with exactly two decimal places.

**Constraints**
- `0 <= Salary <= 10^7`
- `0 <= Years <= 60`

**Sample Input 0**
```
50000 6
```

**Sample Output 0**
```
2500.00
```

**Sample Input 1**
```
50000 5
```

**Sample Output 1**
```
0.00
```

**Sample Input 2**
```
100000 10
```

**Sample Output 2**
```
5000.00
```

**Sample Input 3**
```
80000 4
```

**Sample Output 3**
```
0.00
```

**Sample Input 4**
```
25000 20
```

**Sample Output 4**
```
1250.00
```

**Sample Input 5**
```
0 30
```

**Sample Output 5**
```
0.00
```

**Sample Input 6**
```
60000 5
```

**Sample Output 6**
```
0.00
```

**Sample Input 7**
```
60000 6
```

**Sample Output 7**
```
3000.00
```

**Sample Input 8**
```
1234.5 8
```

**Sample Output 8**
```
61.73
```

**Sample Input 9**
```
999999.99 7
```

**Sample Output 9**
```
50000.00
```

**Tags**
Conditionals, Basics

---

## Classwork: Maximum of Three Numbers
**Problem Statement**
Three integers `A`, `B` and `C` are given on a single line. Print the largest of the three. If two or three of them tie for the largest, print that value once.

**Input Format**
A single line containing three space-separated integers `A B C`.

**Output Format**
A single line containing the maximum value.

**Constraints**
- `-10^9 <= A, B, C <= 10^9`

**Sample Input 0**
```
1 2 3
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
5 5 5
```

**Sample Output 1**
```
5
```

**Sample Input 2**
```
-1 -2 -3
```

**Sample Output 2**
```
-1
```

**Sample Input 3**
```
10 9 10
```

**Sample Output 3**
```
10
```

**Sample Input 4**
```
0 0 0
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
100 -100 50
```

**Sample Output 5**
```
100
```

**Sample Input 6**
```
999999999 -999999999 0
```

**Sample Output 6**
```
999999999
```

**Sample Input 7**
```
7 3 5
```

**Sample Output 7**
```
7
```

**Sample Input 8**
```
-5 -5 -6
```

**Sample Output 8**
```
-5
```

**Sample Input 9**
```
42 42 41
```

**Sample Output 9**
```
42
```

**Tags**
Conditionals, Basics

---

## Classwork: Grade from Marks (A/B/C/F)
**Problem Statement**
The marks obtained by a student are given as a single integer `M`. Print the grade of the student according to these rules:

- `M >= 80`: `A`
- `60 <= M < 80`: `B`
- `40 <= M < 60`: `C`
- `M < 40`: `F`

**Input Format**
A single line containing one integer `M`.

**Output Format**
A single line containing the grade letter.

**Constraints**
- `0 <= M <= 100`

**Sample Input 0**
```
85
```

**Sample Output 0**
```
A
```

**Sample Input 1**
```
60
```

**Sample Output 1**
```
B
```

**Sample Input 2**
```
40
```

**Sample Output 2**
```
C
```

**Sample Input 3**
```
39
```

**Sample Output 3**
```
F
```

**Sample Input 4**
```
0
```

**Sample Output 4**
```
F
```

**Sample Input 5**
```
79
```

**Sample Output 5**
```
B
```

**Sample Input 6**
```
80
```

**Sample Output 6**
```
A
```

**Sample Input 7**
```
100
```

**Sample Output 7**
```
A
```

**Sample Input 8**
```
59
```

**Sample Output 8**
```
C
```

**Sample Input 9**
```
45
```

**Sample Output 9**
```
C
```

**Tags**
Conditionals, Basics

---

## Classwork: Triangle Type from Its Sides
**Problem Statement**
Three positive integers `A`, `B` and `C` are given on a single line, representing the side lengths of a triangle. Print one of the following:

- `Not a triangle` if the three lengths cannot form a valid triangle (any side is greater than or equal to the sum of the other two).
- `Equilateral` if all three sides are equal.
- `Isosceles` if exactly two sides are equal.
- `Scalene` if all three sides are different.

Only one of these labels is printed.

**Input Format**
A single line containing three space-separated integers `A B C`.

**Output Format**
A single line containing one of `Not a triangle`, `Equilateral`, `Isosceles`, `Scalene`.

**Constraints**
- `1 <= A, B, C <= 10^9`

**Sample Input 0**
```
3 4 5
```

**Sample Output 0**
```
Scalene
```

**Sample Input 1**
```
5 5 5
```

**Sample Output 1**
```
Equilateral
```

**Sample Input 2**
```
3 3 4
```

**Sample Output 2**
```
Isosceles
```

**Sample Input 3**
```
1 1 3
```

**Sample Output 3**
```
Not a triangle
```

**Sample Input 4**
```
10 10 10
```

**Sample Output 4**
```
Equilateral
```

**Sample Input 5**
```
6 6 8
```

**Sample Output 5**
```
Isosceles
```

**Sample Input 6**
```
7 8 9
```

**Sample Output 6**
```
Scalene
```

**Sample Input 7**
```
2 2 2
```

**Sample Output 7**
```
Equilateral
```

**Sample Input 8**
```
1 2 3
```

**Sample Output 8**
```
Not a triangle
```

**Sample Input 9**
```
100 100 199
```

**Sample Output 9**
```
Isosceles
```

**Tags**
Conditionals, Geometry

---

## Classwork: Coding Bat - Make Chocolates
**Problem Statement**
You have `small` bars of `1` kilogram of chocolate and `big` bars of `5` kilograms of chocolate. You must build a package weighing exactly `goal` kilograms, using the big bars first.

If it is possible, print the number of small bars used. If it is not possible, print `-1`.

**Input Format**
A single line containing three space-separated integers `small big goal`.

**Output Format**
A single line containing the number of small bars used, or `-1` if the goal cannot be reached.

**Constraints**
- `0 <= small, big <= 10^6`
- `0 <= goal <= 10^9`

**Sample Input 0**
```
4 1 9
```

**Sample Output 0**
```
4
```

**Sample Input 1**
```
4 1 10
```

**Sample Output 1**
```
-1
```

**Sample Input 2**
```
4 1 8
```

**Sample Output 2**
```
3
```

**Sample Input 3**
```
2 1 7
```

**Sample Output 3**
```
2
```

**Sample Input 4**
```
2 1 12
```

**Sample Output 4**
```
-1
```

**Sample Input 5**
```
3 2 10
```

**Sample Output 5**
```
0
```

**Sample Input 6**
```
3 2 13
```

**Sample Output 6**
```
3
```

**Sample Input 7**
```
0 3 15
```

**Sample Output 7**
```
0
```

**Sample Input 8**
```
0 3 14
```

**Sample Output 8**
```
-1
```

**Sample Input 9**
```
5 0 4
```

**Sample Output 9**
```
4
```

**Tags**
Conditionals, Greedy

---

## Classwork: Is a Point Inside a Rectangle
**Problem Statement**
A rectangle is described by two opposite corners `(X1, Y1)` and `(X2, Y2)` with sides parallel to the axes. A point `(PX, PY)` is also given. All six values are integers.

Print `Yes` if the point lies inside the rectangle or on its boundary, otherwise print `No`.

**Input Format**
A single line with six space-separated integers `X1 Y1 X2 Y2 PX PY`.

**Output Format**
A single line containing `Yes` or `No`.

**Constraints**
- `-10^6 <= X1, Y1, X2, Y2, PX, PY <= 10^6`

**Sample Input 0**
```
0 0 10 10 5 5
```

**Sample Output 0**
```
Yes
```

**Sample Input 1**
```
0 0 10 10 0 0
```

**Sample Output 1**
```
Yes
```

**Sample Input 2**
```
0 0 10 10 10 10
```

**Sample Output 2**
```
Yes
```

**Sample Input 3**
```
0 0 10 10 -1 5
```

**Sample Output 3**
```
No
```

**Sample Input 4**
```
0 0 10 10 5 11
```

**Sample Output 4**
```
No
```

**Sample Input 5**
```
10 10 0 0 3 4
```

**Sample Output 5**
```
Yes
```

**Sample Input 6**
```
-5 -5 5 5 0 0
```

**Sample Output 6**
```
Yes
```

**Sample Input 7**
```
-5 -5 5 5 -6 0
```

**Sample Output 7**
```
No
```

**Sample Input 8**
```
1 2 3 4 2 3
```

**Sample Output 8**
```
Yes
```

**Sample Input 9**
```
-100 -100 100 100 100 -100
```

**Sample Output 9**
```
Yes
```

**Tags**
Conditionals, Geometry

---

## Classwork: Day of the Week from a Number
**Problem Statement**
You are given an integer `D`. If `D` is between `1` and `7` (inclusive), print the corresponding day of the week using these labels: `1 -> Monday`, `2 -> Tuesday`, `3 -> Wednesday`, `4 -> Thursday`, `5 -> Friday`, `6 -> Saturday`, `7 -> Sunday`. For any other value of `D`, print `Invalid`.

**Input Format**
A single line containing one integer `D`.

**Output Format**
A single line containing the day name, or `Invalid`.

**Constraints**
- `-100 <= D <= 100`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
Monday
```

**Sample Input 1**
```
7
```

**Sample Output 1**
```
Sunday
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
Wednesday
```

**Sample Input 3**
```
0
```

**Sample Output 3**
```
Invalid
```

**Sample Input 4**
```
8
```

**Sample Output 4**
```
Invalid
```

**Sample Input 5**
```
5
```

**Sample Output 5**
```
Friday
```

**Sample Input 6**
```
2
```

**Sample Output 6**
```
Tuesday
```

**Sample Input 7**
```
-1
```

**Sample Output 7**
```
Invalid
```

**Sample Input 8**
```
4
```

**Sample Output 8**
```
Thursday
```

**Sample Input 9**
```
6
```

**Sample Output 9**
```
Saturday
```

**Tags**
switch-case, Conditionals

---

## Classwork: Vowel Check using Switch
**Problem Statement**
A single non-whitespace character `C` is given on standard input. Print `Vowel` if `C` is one of the English vowels (`a`, `e`, `i`, `o`, `u`, either uppercase or lowercase). Otherwise print `Not a vowel`.

**Input Format**
A single line containing one character `C`.

**Output Format**
A single line containing `Vowel` or `Not a vowel`.

**Constraints**
- `C` is a printable non-whitespace ASCII character.

**Sample Input 0**
```
a
```

**Sample Output 0**
```
Vowel
```

**Sample Input 1**
```
b
```

**Sample Output 1**
```
Not a vowel
```

**Sample Input 2**
```
E
```

**Sample Output 2**
```
Vowel
```

**Sample Input 3**
```
z
```

**Sample Output 3**
```
Not a vowel
```

**Sample Input 4**
```
I
```

**Sample Output 4**
```
Vowel
```

**Sample Input 5**
```
9
```

**Sample Output 5**
```
Not a vowel
```

**Sample Input 6**
```
O
```

**Sample Output 6**
```
Vowel
```

**Sample Input 7**
```
y
```

**Sample Output 7**
```
Not a vowel
```

**Sample Input 8**
```
u
```

**Sample Output 8**
```
Vowel
```

**Sample Input 9**
```
!
```

**Sample Output 9**
```
Not a vowel
```

**Tags**
switch-case, Conditionals

---

## Classwork: Multiplication Tables 1..N with Nested Loops
**Problem Statement**
You are given a single integer `N`. Print the multiplication tables of the numbers `1, 2, 3, ..., N`, one table after another. Each table lists ten lines in the format

```
i x 1 = i
i x 2 = 2*i
...
i x 10 = 10*i
```

There is exactly one blank line between consecutive tables, and no blank line after the last table.

**Input Format**
A single line containing one integer `N`.

**Output Format**
The `N` tables printed in the format described above.

**Constraints**
- `1 <= N <= 10`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

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

**Sample Input 3**
```
4
```

**Sample Output 3**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

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

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

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

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

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

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

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

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

**Sample Input 7**
```
8
```

**Sample Output 7**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

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

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
```

**Sample Input 8**
```
9
```

**Sample Output 8**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

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

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80

9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
```

**Sample Input 9**
```
10
```

**Sample Output 9**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

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

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70

8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80

9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90

10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100
```

**Tags**
Nested Loops, Basics

---

## Classwork: Count All Pairs (i, j) with i less than j
**Problem Statement**
You are given a single integer `N`. Consider all pairs of integers `(i, j)` such that `1 <= i < j <= N`.

Print the total number of such pairs.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing the count of pairs.

**Constraints**
- `1 <= N <= 10^6`

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
4
```

**Sample Output 3**
```
6
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
10
```

**Sample Input 5**
```
10
```

**Sample Output 5**
```
45
```

**Sample Input 6**
```
100
```

**Sample Output 6**
```
4950
```

**Sample Input 7**
```
1000
```

**Sample Output 7**
```
499500
```

**Sample Input 8**
```
999
```

**Sample Output 8**
```
498501
```

**Sample Input 9**
```
1000000
```

**Sample Output 9**
```
499999500000
```

**Tags**
Nested Loops, Number Theory

---

## Classwork: Check if a Number is Prime (Without Sieve)
**Problem Statement**
You are given a single integer `N`. Print `Yes` if `N` is a prime number, otherwise print `No`.

A prime number is an integer greater than `1` whose only positive divisors are `1` and itself.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing `Yes` or `No`.

**Constraints**
- `1 <= N <= 10^9`

**Sample Input 0**
```
2
```

**Sample Output 0**
```
Yes
```

**Sample Input 1**
```
1
```

**Sample Output 1**
```
No
```

**Sample Input 2**
```
9
```

**Sample Output 2**
```
No
```

**Sample Input 3**
```
17
```

**Sample Output 3**
```
Yes
```

**Sample Input 4**
```
1000000007
```

**Sample Output 4**
```
Yes
```

**Sample Input 5**
```
4
```

**Sample Output 5**
```
No
```

**Sample Input 6**
```
1000000000
```

**Sample Output 6**
```
No
```

**Sample Input 7**
```
97
```

**Sample Output 7**
```
Yes
```

**Sample Input 8**
```
49
```

**Sample Output 8**
```
No
```

**Sample Input 9**
```
23
```

**Sample Output 9**
```
Yes
```

**Tags**
Loops, Number Theory

---

## Classwork: Count Multiples of K in a Range
**Problem Statement**
You are given three integers `L`, `R` and `K` on a single line. Print the number of integers `X` in the closed range `[L, R]` such that `X` is a multiple of `K` (that is, `X % K == 0`).

`0` is considered a multiple of every non-zero `K`.

**Input Format**
A single line containing three space-separated integers `L R K` with `L <= R` and `K >= 1`.

**Output Format**
A single line containing the count.

**Constraints**
- `-10^9 <= L <= R <= 10^9`
- `1 <= K <= 10^9`

**Sample Input 0**
```
1 10 2
```

**Sample Output 0**
```
5
```

**Sample Input 1**
```
1 100 5
```

**Sample Output 1**
```
20
```

**Sample Input 2**
```
0 0 7
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
-10 10 3
```

**Sample Output 3**
```
7
```

**Sample Input 4**
```
1 1 1
```

**Sample Output 4**
```
1
```

**Sample Input 5**
```
5 5 5
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
1 1000000000 1
```

**Sample Output 6**
```
1000000000
```

**Sample Input 7**
```
-100 100 25
```

**Sample Output 7**
```
9
```

**Sample Input 8**
```
1 1000000000 999999937
```

**Sample Output 8**
```
1
```

**Sample Input 9**
```
13 89 4
```

**Sample Output 9**
```
19
```

**Tags**
Loops, Number Theory

---

## Classwork: Solid Square of Stars
**Problem Statement**
You are given a single integer `N`. Print an `N x N` solid square built from the character `*`. Every row contains exactly `N` `*` characters, and there is no trailing space.

**Input Format**
A single line containing one integer `N`.

**Output Format**
`N` lines, each containing exactly `N` `*` characters.

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
**
**
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
***
***
***
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
****
****
****
****
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
*****
*****
*****
*****
*****
```

**Sample Input 5**
```
6
```

**Sample Output 5**
```
******
******
******
******
******
******
```

**Sample Input 6**
```
7
```

**Sample Output 6**
```
*******
*******
*******
*******
*******
*******
*******
```

**Sample Input 7**
```
10
```

**Sample Output 7**
```
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
```

**Sample Input 8**
```
15
```

**Sample Output 8**
```
***************
***************
***************
***************
***************
***************
***************
***************
***************
***************
***************
***************
***************
***************
***************
```

**Sample Input 9**
```
20
```

**Sample Output 9**
```
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
```

**Tags**
Patterns, Loops

---
