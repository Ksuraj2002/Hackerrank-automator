# DSA-101 Homework - Part 1 (Days 1 to 8)

Titles and statements strictly describe the task only. No mention of any
data structure, algorithm or language feature - students choose the
approach themselves.

Skipped from this range:
- Day 1 HW3 "Print sizeof of each type": C++-specific; sizeof values differ
  across languages and can't be judged uniformly. Not authored.

After uploading:
1. `venv\Scripts\python.exe tools\hr_mark_samples.py --md homework_part1_days1_8.md --apply`
2. Enable C++14, Java 8, Python 3 on each challenge in the admin UI.
3. `venv\Scripts\python.exe tools\hr_add_to_contest.py --md homework_part1_days1_8.md --apply`

---


## Homework: Print Your Daily Timetable
**Problem Statement**
A daily timetable has `N` entries. Each entry is a time (in `HH:MM` 24-hour format) and an activity description on the same line, separated by a single space.

Print each entry on its own line in the format `HH:MM - <activity>` (time, one space, a `-`, one space, activity). Preserve the input order.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: each contains a time `HH:MM`, one space, then the activity description (may contain letters, digits and spaces).

**Output Format**
`N` lines, each showing the entry as `HH:MM - <activity>`.

**Constraints**
- `1 <= N <= 50`
- Every time is `HH:MM` with `HH` in `00-23` and `MM` in `00-59`.
- Each activity description is between `1` and `40` characters.

**Sample Input 0**
```
3
08:00 Wake up
09:00 Breakfast
10:00 Study
```

**Sample Output 0**
```
08:00 - Wake up
09:00 - Breakfast
10:00 - Study
```

**Sample Input 1**
```
1
07:30 Morning walk
```

**Sample Output 1**
```
07:30 - Morning walk
```

**Sample Input 2**
```
4
06:00 Yoga
07:00 Shower
08:00 Breakfast
09:00 Class
```

**Sample Output 2**
```
06:00 - Yoga
07:00 - Shower
08:00 - Breakfast
09:00 - Class
```

**Sample Input 3**
```
2
12:00 Lunch
13:00 Nap
```

**Sample Output 3**
```
12:00 - Lunch
13:00 - Nap
```

**Sample Input 4**
```
5
05:30 Running
06:00 Meditation
07:00 Breakfast
08:00 School
20:00 Dinner
```

**Sample Output 4**
```
05:30 - Running
06:00 - Meditation
07:00 - Breakfast
08:00 - School
20:00 - Dinner
```

**Sample Input 5**
```
3
21:00 Read
22:00 Journal
23:00 Sleep
```

**Sample Output 5**
```
21:00 - Read
22:00 - Journal
23:00 - Sleep
```

**Sample Input 6**
```
1
00:00 Midnight snack
```

**Sample Output 6**
```
00:00 - Midnight snack
```

**Sample Input 7**
```
2
15:00 Homework
17:00 Play
```

**Sample Output 7**
```
15:00 - Homework
17:00 - Play
```

**Sample Input 8**
```
3
11:15 Break
11:45 Class
12:30 Lunch
```

**Sample Output 8**
```
11:15 - Break
11:45 - Class
12:30 - Lunch
```

**Sample Input 9**
```
6
06:00 Wake up
07:00 Breakfast
09:00 Class
13:00 Lunch
18:00 Sports
22:00 Sleep
```

**Sample Output 9**
```
06:00 - Wake up
07:00 - Breakfast
09:00 - Class
13:00 - Lunch
18:00 - Sports
22:00 - Sleep
```

**Tags**
Basics, IO

---

## Homework: Print a 4-Line House
**Problem Statement**
Print exactly the following 4-line figure. The figure is the same for every test case; the input is ignored beyond being read.

```
 /\
/__\
|  |
|__|
```

There are no trailing spaces on any line.

**Input Format**
A single line containing one integer `N`. Its value does not change the required output.

**Output Format**
Exactly four lines showing the figure above.

**Constraints**
- `1 <= N <= 100`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
 /\
/__\
|  |
|__|
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
 /\
/__\
|  |
|__|
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
 /\
/__\
|  |
|__|
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
 /\
/__\
|  |
|__|
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
 /\
/__\
|  |
|__|
```

**Sample Input 5**
```
10
```

**Sample Output 5**
```
 /\
/__\
|  |
|__|
```

**Sample Input 6**
```
42
```

**Sample Output 6**
```
 /\
/__\
|  |
|__|
```

**Sample Input 7**
```
77
```

**Sample Output 7**
```
 /\
/__\
|  |
|__|
```

**Sample Input 8**
```
100
```

**Sample Output 8**
```
 /\
/__\
|  |
|__|
```

**Sample Input 9**
```
50
```

**Sample Output 9**
```
 /\
/__\
|  |
|__|
```

**Tags**
Basics, IO

---

## Homework: Remove the Last Digit of a Number
**Problem Statement**
You are given a single non-negative integer `N`. Print the integer that is left after removing its rightmost digit. For example, when `N = 45983` the answer is `4598`. When `N` has only one digit, the answer is `0`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing `N` with its last digit removed.

**Constraints**
- `0 <= N <= 10^9`

**Sample Input 0**
```
45983
```

**Sample Output 0**
```
4598
```

**Sample Input 1**
```
7
```

**Sample Output 1**
```
0
```

**Sample Input 2**
```
10
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
100
```

**Sample Output 3**
```
10
```

**Sample Input 4**
```
0
```

**Sample Output 4**
```
0
```

**Sample Input 5**
```
999999999
```

**Sample Output 5**
```
99999999
```

**Sample Input 6**
```
1
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
50
```

**Sample Output 7**
```
5
```

**Sample Input 8**
```
12345
```

**Sample Output 8**
```
1234
```

**Sample Input 9**
```
999
```

**Sample Output 9**
```
99
```

**Tags**
Basics, Numbers

---

## Homework: Larger of Two Numbers
**Problem Statement**
Two integers `A` and `B` are given on a single line, separated by a space. Print the larger of the two. If they are equal, print that value.

**Input Format**
A single line containing two space-separated integers `A B`.

**Output Format**
A single line containing the larger value.

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
Basics, Conditionals

---

## Homework: Even or Odd
**Problem Statement**
A single integer `N` is given. Print `Even` if `N` is an even number, otherwise print `Odd`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing `Even` or `Odd`.

**Constraints**
- `-10^9 <= N <= 10^9`

**Sample Input 0**
```
4
```

**Sample Output 0**
```
Even
```

**Sample Input 1**
```
7
```

**Sample Output 1**
```
Odd
```

**Sample Input 2**
```
0
```

**Sample Output 2**
```
Even
```

**Sample Input 3**
```
-3
```

**Sample Output 3**
```
Odd
```

**Sample Input 4**
```
-8
```

**Sample Output 4**
```
Even
```

**Sample Input 5**
```
1
```

**Sample Output 5**
```
Odd
```

**Sample Input 6**
```
1000000000
```

**Sample Output 6**
```
Even
```

**Sample Input 7**
```
999999999
```

**Sample Output 7**
```
Odd
```

**Sample Input 8**
```
-1000000000
```

**Sample Output 8**
```
Even
```

**Sample Input 9**
```
42
```

**Sample Output 9**
```
Even
```

**Tags**
Basics, Conditionals

---

## Homework: Income Tax Check
**Problem Statement**
The annual income of a person `I` is given as a single integer. Print `No tax to be paid` if the income is strictly less than `500000`. Otherwise print `Tax to be paid`.

**Input Format**
A single line containing one integer `I`.

**Output Format**
A single line containing `No tax to be paid` or `Tax to be paid`.

**Constraints**
- `0 <= I <= 10^9`

**Sample Input 0**
```
400000
```

**Sample Output 0**
```
No tax to be paid
```

**Sample Input 1**
```
500000
```

**Sample Output 1**
```
Tax to be paid
```

**Sample Input 2**
```
499999
```

**Sample Output 2**
```
No tax to be paid
```

**Sample Input 3**
```
1000000
```

**Sample Output 3**
```
Tax to be paid
```

**Sample Input 4**
```
0
```

**Sample Output 4**
```
No tax to be paid
```

**Sample Input 5**
```
250000
```

**Sample Output 5**
```
No tax to be paid
```

**Sample Input 6**
```
750000
```

**Sample Output 6**
```
Tax to be paid
```

**Sample Input 7**
```
500001
```

**Sample Output 7**
```
Tax to be paid
```

**Sample Input 8**
```
50000
```

**Sample Output 8**
```
No tax to be paid
```

**Sample Input 9**
```
999999
```

**Sample Output 9**
```
Tax to be paid
```

**Tags**
Basics, Conditionals

---

## Homework: Grace Marks
**Problem Statement**
A teacher awards `4` grace marks to a student only if the student's marks are strictly less than `33`. Otherwise the marks are left unchanged.

You are given a student's marks `M`. Print the final marks after the grace policy is applied.

**Input Format**
A single line containing one integer `M`.

**Output Format**
A single line containing the final marks.

**Constraints**
- `0 <= M <= 100`

**Sample Input 0**
```
30
```

**Sample Output 0**
```
34
```

**Sample Input 1**
```
33
```

**Sample Output 1**
```
33
```

**Sample Input 2**
```
32
```

**Sample Output 2**
```
36
```

**Sample Input 3**
```
40
```

**Sample Output 3**
```
40
```

**Sample Input 4**
```
0
```

**Sample Output 4**
```
4
```

**Sample Input 5**
```
100
```

**Sample Output 5**
```
100
```

**Sample Input 6**
```
29
```

**Sample Output 6**
```
33
```

**Sample Input 7**
```
50
```

**Sample Output 7**
```
50
```

**Sample Input 8**
```
31
```

**Sample Output 8**
```
35
```

**Sample Input 9**
```
34
```

**Sample Output 9**
```
34
```

**Tags**
Basics, Conditionals

---

## Homework: Age Category
**Problem Statement**
A single non-negative integer `A` representing an age is given. Print the category the age belongs to according to the following rules:

- `A > 70`: print `Super Senior Citizen`.
- `59 <= A <= 70`: print `Senior Citizen`.
- `18 <= A < 59`: print `Adult`.
- `1 < A < 18`: print `Underage`.
- Any other `A` (i.e. `A <= 1`): print `New Born`.

**Input Format**
A single line containing one integer `A`.

**Output Format**
A single line containing the category name.

**Constraints**
- `0 <= A <= 150`

**Sample Input 0**
```
75
```

**Sample Output 0**
```
Super Senior Citizen
```

**Sample Input 1**
```
70
```

**Sample Output 1**
```
Senior Citizen
```

**Sample Input 2**
```
60
```

**Sample Output 2**
```
Senior Citizen
```

**Sample Input 3**
```
59
```

**Sample Output 3**
```
Senior Citizen
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
18
```

**Sample Output 5**
```
Adult
```

**Sample Input 6**
```
10
```

**Sample Output 6**
```
Underage
```

**Sample Input 7**
```
1
```

**Sample Output 7**
```
New Born
```

**Sample Input 8**
```
0
```

**Sample Output 8**
```
New Born
```

**Sample Input 9**
```
17
```

**Sample Output 9**
```
Underage
```

**Tags**
Basics, Conditionals

---

## Homework: Age-Based Government Bonus
**Problem Statement**
The government adds money to a person's income according to their age:

- `A > 60`: add `1000`.
- `40 < A <= 60`: add `500`.
- Otherwise: add `0`.

You are given the person's age `A` and current salary `S` on a single line. Print the final income.

**Input Format**
A single line containing two space-separated integers `A S`.

**Output Format**
A single line containing the final income.

**Constraints**
- `0 <= A <= 150`
- `0 <= S <= 10^9`

**Sample Input 0**
```
65 50000
```

**Sample Output 0**
```
51000
```

**Sample Input 1**
```
60 50000
```

**Sample Output 1**
```
50500
```

**Sample Input 2**
```
45 40000
```

**Sample Output 2**
```
40500
```

**Sample Input 3**
```
40 40000
```

**Sample Output 3**
```
40000
```

**Sample Input 4**
```
70 100000
```

**Sample Output 4**
```
101000
```

**Sample Input 5**
```
30 30000
```

**Sample Output 5**
```
30000
```

**Sample Input 6**
```
80 25000
```

**Sample Output 6**
```
26000
```

**Sample Input 7**
```
50 60000
```

**Sample Output 7**
```
60500
```

**Sample Input 8**
```
41 20000
```

**Sample Output 8**
```
20500
```

**Sample Input 9**
```
18 0
```

**Sample Output 9**
```
0
```

**Tags**
Basics, Conditionals

---

## Homework: Largest of Three Distinct Numbers
**Problem Statement**
Three integers `A`, `B` and `C` are given on a single line. You are guaranteed that no two of them are equal. Print the largest of the three.

**Input Format**
A single line containing three space-separated integers `A B C`, with `A`, `B`, `C` pairwise distinct.

**Output Format**
A single line containing the largest value.

**Constraints**
- `-10^9 <= A, B, C <= 10^9`
- All three values are distinct.

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
10 5 8
```

**Sample Output 1**
```
10
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
100 200 300
```

**Sample Output 3**
```
300
```

**Sample Input 4**
```
7 3 5
```

**Sample Output 4**
```
7
```

**Sample Input 5**
```
999999999 -999999999 0
```

**Sample Output 5**
```
999999999
```

**Sample Input 6**
```
50 40 45
```

**Sample Output 6**
```
50
```

**Sample Input 7**
```
12 15 10
```

**Sample Output 7**
```
15
```

**Sample Input 8**
```
-5 -10 -1
```

**Sample Output 8**
```
-1
```

**Sample Input 9**
```
42 41 40
```

**Sample Output 9**
```
42
```

**Tags**
Basics, Conditionals

---

## Homework: Simple Calculator
**Problem Statement**
You are given an integer `A`, an operator character `OP` and another integer `B` on a single line, separated by spaces. `OP` is one of `+`, `-`, `*`, `/`.

Print the result of applying the operator to `A` and `B`:

- `+`: the sum `A + B`.
- `-`: the difference `A - B`.
- `*`: the product `A * B`.
- `/`: the quotient `A / B` using integer division that truncates toward zero. If `B` is `0`, print `Division by zero` instead.

**Input Format**
A single line containing `A`, `OP`, `B` separated by spaces.

**Output Format**
A single line containing the result, or `Division by zero`.

**Constraints**
- `-10^6 <= A, B <= 10^6`
- `OP` is one of `+`, `-`, `*`, `/`.

**Sample Input 0**
```
10 + 5
```

**Sample Output 0**
```
15
```

**Sample Input 1**
```
10 - 5
```

**Sample Output 1**
```
5
```

**Sample Input 2**
```
10 * 5
```

**Sample Output 2**
```
50
```

**Sample Input 3**
```
10 / 5
```

**Sample Output 3**
```
2
```

**Sample Input 4**
```
10 / 0
```

**Sample Output 4**
```
Division by zero
```

**Sample Input 5**
```
-7 / 2
```

**Sample Output 5**
```
-3
```

**Sample Input 6**
```
7 / -2
```

**Sample Output 6**
```
-3
```

**Sample Input 7**
```
0 * 100
```

**Sample Output 7**
```
0
```

**Sample Input 8**
```
1000000 * 1000000
```

**Sample Output 8**
```
1000000000000
```

**Sample Input 9**
```
-5 - -5
```

**Sample Output 9**
```
0
```

**Tags**
Basics, Conditionals

---

## Homework: Ticket Price by Age
**Problem Statement**
A ticket counter charges according to the customer's age:

- `A <= 12`: `50` rupees.
- `A >= 60`: `70` rupees.
- Any other `A` (13 to 59): `100` rupees.

You are given a single non-negative integer `A`, the age of the customer. Print the ticket price.

**Input Format**
A single line containing one integer `A`.

**Output Format**
A single line containing the price.

**Constraints**
- `0 <= A <= 150`

**Sample Input 0**
```
10
```

**Sample Output 0**
```
50
```

**Sample Input 1**
```
12
```

**Sample Output 1**
```
50
```

**Sample Input 2**
```
13
```

**Sample Output 2**
```
100
```

**Sample Input 3**
```
25
```

**Sample Output 3**
```
100
```

**Sample Input 4**
```
59
```

**Sample Output 4**
```
100
```

**Sample Input 5**
```
60
```

**Sample Output 5**
```
70
```

**Sample Input 6**
```
70
```

**Sample Output 6**
```
70
```

**Sample Input 7**
```
0
```

**Sample Output 7**
```
50
```

**Sample Input 8**
```
18
```

**Sample Output 8**
```
100
```

**Sample Input 9**
```
45
```

**Sample Output 9**
```
100
```

**Tags**
Basics, Conditionals

---

## Homework: Menu Selection
**Problem Statement**
A program presents four menu options:

```
1. Add
2. Subtract
3. Multiply
4. Divide
```

You are given a single integer `C` representing the user's choice. Print the menu label for that choice on a single line: `Add`, `Subtract`, `Multiply`, or `Divide`. For any value of `C` that is not `1`, `2`, `3` or `4`, print `Invalid choice`.

**Input Format**
A single line containing one integer `C`.

**Output Format**
A single line containing the menu label or `Invalid choice`.

**Constraints**
- `-100 <= C <= 100`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
Add
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
Subtract
```

**Sample Input 2**
```
3
```

**Sample Output 2**
```
Multiply
```

**Sample Input 3**
```
4
```

**Sample Output 3**
```
Divide
```

**Sample Input 4**
```
5
```

**Sample Output 4**
```
Invalid choice
```

**Sample Input 5**
```
0
```

**Sample Output 5**
```
Invalid choice
```

**Sample Input 6**
```
-1
```

**Sample Output 6**
```
Invalid choice
```

**Sample Input 7**
```
10
```

**Sample Output 7**
```
Invalid choice
```

**Sample Input 8**
```
100
```

**Sample Output 8**
```
Invalid choice
```

**Sample Input 9**
```
6
```

**Sample Output 9**
```
Invalid choice
```

**Tags**
Basics, Conditionals

---

## Homework: Number of Days in a Month
**Problem Statement**
You are given an integer `M` representing a month number in a non-leap year (so February has `28` days). Print the number of days in month `M`.

If `M` is not between `1` and `12` inclusive, print `Invalid month`.

**Input Format**
A single line containing one integer `M`.

**Output Format**
A single line containing the number of days or `Invalid month`.

**Constraints**
- `-100 <= M <= 100`

**Sample Input 0**
```
1
```

**Sample Output 0**
```
31
```

**Sample Input 1**
```
2
```

**Sample Output 1**
```
28
```

**Sample Input 2**
```
4
```

**Sample Output 2**
```
30
```

**Sample Input 3**
```
12
```

**Sample Output 3**
```
31
```

**Sample Input 4**
```
6
```

**Sample Output 4**
```
30
```

**Sample Input 5**
```
7
```

**Sample Output 5**
```
31
```

**Sample Input 6**
```
0
```

**Sample Output 6**
```
Invalid month
```

**Sample Input 7**
```
13
```

**Sample Output 7**
```
Invalid month
```

**Sample Input 8**
```
-1
```

**Sample Output 8**
```
Invalid month
```

**Sample Input 9**
```
11
```

**Sample Output 9**
```
30
```

**Tags**
Basics, Conditionals

---

## Homework: Factorial of a Number
**Problem Statement**
You are given a single non-negative integer `N`. Print the value of `N!` (`N` factorial). By convention `0! = 1`.

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
Basics, Numbers

---

## Homework: Digital Root of a Number
**Problem Statement**
You are given a single non-negative integer `N`. Repeatedly replace `N` by the sum of its digits until it becomes a single-digit number, then print that single digit.

For example, if `N = 493` the digit sum is `4 + 9 + 3 = 16`, and then `1 + 6 = 7`, so the answer is `7`.

**Input Format**
A single line containing one integer `N`.

**Output Format**
A single line containing the single-digit result.

**Constraints**
- `0 <= N <= 10^18`

**Sample Input 0**
```
493
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
9
```

**Sample Output 2**
```
9
```

**Sample Input 3**
```
10
```

**Sample Output 3**
```
1
```

**Sample Input 4**
```
999999999
```

**Sample Output 4**
```
9
```

**Sample Input 5**
```
38
```

**Sample Output 5**
```
2
```

**Sample Input 6**
```
1
```

**Sample Output 6**
```
1
```

**Sample Input 7**
```
100
```

**Sample Output 7**
```
1
```

**Sample Input 8**
```
12345
```

**Sample Output 8**
```
6
```

**Sample Input 9**
```
1000000000000000000
```

**Sample Output 9**
```
1
```

**Tags**
Basics, Numbers

---
