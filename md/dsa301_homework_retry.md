# DSA-301 Homework - retry batch (2 problems that failed to upload)

Author-ready markdown for automator.py. After upload, run tools/hr_mark_samples.py --md dsa301_homework_retry.md --apply.

---

## Homework: Print Vector Elements
**Problem Statement**
You are given `N` integers. Print each integer on its own line, in the order they were given.

**Input Format**
- Line 1: an integer `N`.
- Line 2: `N` space-separated integers `a_1, ..., a_N`.

**Output Format**
`N` lines. The i-th line contains `a_i`.

**Constraints**
- `1 <= N <= 100000`
- `-10^9 <= a_i <= 10^9`

**Sample Input 0**
```
3
1 2 3
```

**Sample Output 0**
```
1
2
3
```

**Sample Input 1**
```
1
42
```

**Sample Output 1**
```
42
```

**Sample Input 2**
```
5
5 4 3 2 1
```

**Sample Output 2**
```
5
4
3
2
1
```

**Sample Input 3**
```
4
-1 0 1 -2
```

**Sample Output 3**
```
-1
0
1
-2
```

**Sample Input 4**
```
6
100 200 300 400 500 600
```

**Sample Output 4**
```
100
200
300
400
500
600
```

**Sample Input 5**
```
2
-1000000000 1000000000
```

**Sample Output 5**
```
-1000000000
1000000000
```

**Sample Input 6**
```
5
0 0 0 0 0
```

**Sample Output 6**
```
0
0
0
0
0
```

**Sample Input 7**
```
3
7 7 7
```

**Sample Output 7**
```
7
7
7
```

**Sample Input 8**
```
4
10 -10 10 -10
```

**Sample Output 8**
```
10
-10
10
-10
```

**Sample Input 9**
```
5
1 -2 3 -4 5
```

**Sample Output 9**
```
1
-2
3
-4
5
```

**Tags**
Basics, IO, Arrays

---

## Homework: Sort Strings in Reverse Alphabetical Order
**Problem Statement**
You are given `N` strings, each consisting of lowercase English letters. Print the strings in reverse alphabetical (lexicographic) order, one per line.

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: one string per line.

**Output Format**
`N` lines: the input strings sorted in reverse alphabetical order.

**Constraints**
- `1 <= N <= 100000`
- Each string has length between 1 and 50; only lowercase English letters.

**Sample Input 0**
```
3
apple
banana
cherry
```

**Sample Output 0**
```
cherry
banana
apple
```

**Sample Input 1**
```
1
hello
```

**Sample Output 1**
```
hello
```

**Sample Input 2**
```
4
dog
cat
bird
ant
```

**Sample Output 2**
```
dog
cat
bird
ant
```

**Sample Input 3**
```
3
zzz
aaa
mmm
```

**Sample Output 3**
```
zzz
mmm
aaa
```

**Sample Input 4**
```
5
one
two
three
four
five
```

**Sample Output 4**
```
two
three
one
four
five
```

**Sample Input 5**
```
3
abc
ab
abcd
```

**Sample Output 5**
```
abcd
abc
ab
```

**Sample Input 6**
```
4
xyz
xy
x
xyzw
```

**Sample Output 6**
```
xyzw
xyz
xy
x
```

**Sample Input 7**
```
2
a
b
```

**Sample Output 7**
```
b
a
```

**Sample Input 8**
```
5
red
blue
green
yellow
orange
```

**Sample Output 8**
```
yellow
red
orange
green
blue
```

**Sample Input 9**
```
6
z
y
x
w
v
u
```

**Sample Output 9**
```
z
y
x
w
v
u
```

**Tags**
Sorting, Strings
