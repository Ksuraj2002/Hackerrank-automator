# DSA-101 Classwork - Supplement (Day 33)

A single missing item that slipped through Parts 1-3.

After uploading:
1. `venv\Scripts\python.exe tools\hr_mark_samples.py --md classwork_supplement_day33.md --apply`
2. Enable C++14, Java 8, Python 3 in the admin UI.
3. `venv\Scripts\python.exe tools\hr_add_to_contest.py --md classwork_supplement_day33.md --apply`

---


## Classwork: Sort Strings by Length
**Problem Statement**
You are given `N` strings on `N` separate lines. Print them in non-decreasing order of their length, one string per line.

When two strings have the same length, they must appear in the same relative order as in the input (stable ordering).

**Input Format**
- Line 1: an integer `N`.
- Next `N` lines: each contains one string with no spaces.

**Output Format**
`N` lines, the input strings arranged by non-decreasing length (stable).

**Constraints**
- `1 <= N <= 10^4`
- `1 <= length of each string <= 100`
- Strings contain printable ASCII characters and no whitespace.

**Sample Input 0**
```
5
apple
hi
banana
kiwi
fig
```

**Sample Output 0**
```
hi
fig
kiwi
apple
banana
```

**Sample Input 1**
```
1
solo
```

**Sample Output 1**
```
solo
```

**Sample Input 2**
```
3
aaa
bbb
ccc
```

**Sample Output 2**
```
aaa
bbb
ccc
```

**Sample Input 3**
```
4
ab
cd
ef
gh
```

**Sample Output 3**
```
ab
cd
ef
gh
```

**Sample Input 4**
```
5
a
ab
abc
abcd
abcde
```

**Sample Output 4**
```
a
ab
abc
abcd
abcde
```

**Sample Input 5**
```
5
abcde
abcd
abc
ab
a
```

**Sample Output 5**
```
a
ab
abc
abcd
abcde
```

**Sample Input 6**
```
6
cat
dog
fish
frog
owl
pig
```

**Sample Output 6**
```
cat
dog
owl
pig
fish
frog
```

**Sample Input 7**
```
4
longer
small
tinyy
hi
```

**Sample Output 7**
```
hi
small
tinyy
longer
```

**Sample Input 8**
```
3
zebra
apple
mango
```

**Sample Output 8**
```
zebra
apple
mango
```

**Sample Input 9**
```
7
red
yellow
green
blue
cyan
teal
pink
```

**Sample Output 9**
```
red
blue
cyan
teal
pink
green
yellow
```

**Tags**
Sorting, STL, Strings

---
