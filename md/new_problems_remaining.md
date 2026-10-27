# New Problems to Author

Five coding problems formatted for `automator.py`. Section headers and `Sample Input N` / `Sample Output N` fenced blocks match the parser in `automator.py`.

Run:

```
python automator.py new_problems.md
```

The automator uploads every sample block as a HackerRank test case but does not tick the **Sample** or **Score** checkboxes. After the run, open each challenge and:

1. On test cases 2-9 (0-indexed), untick **Sample test case**. Leave tests 0 and 1 as samples.
2. On every case, tick **Score** and set weight `10` so the total is 100.
3. Publish.

---

## Sum and Count Scores using Map

**Problem Statement**
`N` (name, score) records are given. Aggregate them so that for each unique name you print the total of all scores recorded for that name, and the count of records for that name.

Print the names in alphabetical order. Use `std::map<std::string, int>` so iteration order is naturally sorted.

Note: `ABC` sorts before `abc` because uppercase letters have smaller ASCII values. The problem does not fold case.

**Input Format**
- Line 1: an integer `N`, the number of records.
- Next `N` lines: each contains a name (letters only, no spaces) and an integer score, separated by one space.

**Output Format**
For each distinct name, in alphabetical order, print one line:
```
<name> <total_score> <count>
```

**Constraints**
- `1 <= N <= 10^5`
- Name length is between `1` and `20`.
- `0 <= score <= 100`.

**Sample Input 0**
```
6
Anna 80
Ravi 55
Anna 70
Ravi 95
Ravi 40
Zoe 100
```

**Sample Output 0**
```
Anna 150 2
Ravi 190 3
Zoe 100 1
```

**Sample Input 1**
```
1
Solo 42
```

**Sample Output 1**
```
Solo 42 1
```

**Sample Input 2**
```
3
Bob 10
Bob 20
Bob 30
```

**Sample Output 2**
```
Bob 60 3
```

**Sample Input 3**
```
4
Zack 1
Yara 2
Xena 3
Amy 4
```

**Sample Output 3**
```
Amy 4 1
Xena 3 1
Yara 2 1
Zack 1 1
```

**Sample Input 4**
```
5
Ana 0
Ana 0
Ana 100
Ana 0
Ana 0
```

**Sample Output 4**
```
Ana 100 5
```

**Sample Input 5**
```
4
abc 5
ABC 5
abc 10
ABC 10
```

**Sample Output 5**
```
ABC 15 2
abc 15 2
```

**Sample Input 6**
```
6
Kai 50
Lia 40
Kai 30
Lia 60
Mia 20
Kai 70
```

**Sample Output 6**
```
Kai 150 3
Lia 100 2
Mia 20 1
```

**Sample Input 7**
```
2
Ann 100
Anna 100
```

**Sample Output 7**
```
Ann 100 1
Anna 100 1
```

**Sample Input 8**
```
5
P 1
Q 2
P 3
Q 4
P 5
```

**Sample Output 8**
```
P 9 3
Q 6 2
```

**Sample Input 9**
```
500
Amy 0
Bob 1
Cy 2
Dan 3
Eve 4
Amy 5
Bob 6
Cy 7
Dan 8
Eve 9
Amy 10
Bob 11
Cy 12
Dan 13
Eve 14
Amy 15
Bob 16
Cy 17
Dan 18
Eve 19
Amy 20
Bob 21
Cy 22
Dan 23
Eve 24
Amy 25
Bob 26
Cy 27
Dan 28
Eve 29
Amy 30
Bob 31
Cy 32
Dan 33
Eve 34
Amy 35
Bob 36
Cy 37
Dan 38
Eve 39
Amy 40
Bob 41
Cy 42
Dan 43
Eve 44
Amy 45
Bob 46
Cy 47
Dan 48
Eve 49
Amy 50
Bob 51
Cy 52
Dan 53
Eve 54
Amy 55
Bob 56
Cy 57
Dan 58
Eve 59
Amy 60
Bob 61
Cy 62
Dan 63
Eve 64
Amy 65
Bob 66
Cy 67
Dan 68
Eve 69
Amy 70
Bob 71
Cy 72
Dan 73
Eve 74
Amy 75
Bob 76
Cy 77
Dan 78
Eve 79
Amy 80
Bob 81
Cy 82
Dan 83
Eve 84
Amy 85
Bob 86
Cy 87
Dan 88
Eve 89
Amy 90
Bob 91
Cy 92
Dan 93
Eve 94
Amy 95
Bob 96
Cy 97
Dan 98
Eve 99
Amy 100
Bob 0
Cy 1
Dan 2
Eve 3
Amy 4
Bob 5
Cy 6
Dan 7
Eve 8
Amy 9
Bob 10
Cy 11
Dan 12
Eve 13
Amy 14
Bob 15
Cy 16
Dan 17
Eve 18
Amy 19
Bob 20
Cy 21
Dan 22
Eve 23
Amy 24
Bob 25
Cy 26
Dan 27
Eve 28
Amy 29
Bob 30
Cy 31
Dan 32
Eve 33
Amy 34
Bob 35
Cy 36
Dan 37
Eve 38
Amy 39
Bob 40
Cy 41
Dan 42
Eve 43
Amy 44
Bob 45
Cy 46
Dan 47
Eve 48
Amy 49
Bob 50
Cy 51
Dan 52
Eve 53
Amy 54
Bob 55
Cy 56
Dan 57
Eve 58
Amy 59
Bob 60
Cy 61
Dan 62
Eve 63
Amy 64
Bob 65
Cy 66
Dan 67
Eve 68
Amy 69
Bob 70
Cy 71
Dan 72
Eve 73
Amy 74
Bob 75
Cy 76
Dan 77
Eve 78
Amy 79
Bob 80
Cy 81
Dan 82
Eve 83
Amy 84
Bob 85
Cy 86
Dan 87
Eve 88
Amy 89
Bob 90
Cy 91
Dan 92
Eve 93
Amy 94
Bob 95
Cy 96
Dan 97
Eve 98
Amy 99
Bob 100
Cy 0
Dan 1
Eve 2
Amy 3
Bob 4
Cy 5
Dan 6
Eve 7
Amy 8
Bob 9
Cy 10
Dan 11
Eve 12
Amy 13
Bob 14
Cy 15
Dan 16
Eve 17
Amy 18
Bob 19
Cy 20
Dan 21
Eve 22
Amy 23
Bob 24
Cy 25
Dan 26
Eve 27
Amy 28
Bob 29
Cy 30
Dan 31
Eve 32
Amy 33
Bob 34
Cy 35
Dan 36
Eve 37
Amy 38
Bob 39
Cy 40
Dan 41
Eve 42
Amy 43
Bob 44
Cy 45
Dan 46
Eve 47
Amy 48
Bob 49
Cy 50
Dan 51
Eve 52
Amy 53
Bob 54
Cy 55
Dan 56
Eve 57
Amy 58
Bob 59
Cy 60
Dan 61
Eve 62
Amy 63
Bob 64
Cy 65
Dan 66
Eve 67
Amy 68
Bob 69
Cy 70
Dan 71
Eve 72
Amy 73
Bob 74
Cy 75
Dan 76
Eve 77
Amy 78
Bob 79
Cy 80
Dan 81
Eve 82
Amy 83
Bob 84
Cy 85
Dan 86
Eve 87
Amy 88
Bob 89
Cy 90
Dan 91
Eve 92
Amy 93
Bob 94
Cy 95
Dan 96
Eve 97
Amy 98
Bob 99
Cy 100
Dan 0
Eve 1
Amy 2
Bob 3
Cy 4
Dan 5
Eve 6
Amy 7
Bob 8
Cy 9
Dan 10
Eve 11
Amy 12
Bob 13
Cy 14
Dan 15
Eve 16
Amy 17
Bob 18
Cy 19
Dan 20
Eve 21
Amy 22
Bob 23
Cy 24
Dan 25
Eve 26
Amy 27
Bob 28
Cy 29
Dan 30
Eve 31
Amy 32
Bob 33
Cy 34
Dan 35
Eve 36
Amy 37
Bob 38
Cy 39
Dan 40
Eve 41
Amy 42
Bob 43
Cy 44
Dan 45
Eve 46
Amy 47
Bob 48
Cy 49
Dan 50
Eve 51
Amy 52
Bob 53
Cy 54
Dan 55
Eve 56
Amy 57
Bob 58
Cy 59
Dan 60
Eve 61
Amy 62
Bob 63
Cy 64
Dan 65
Eve 66
Amy 67
Bob 68
Cy 69
Dan 70
Eve 71
Amy 72
Bob 73
Cy 74
Dan 75
Eve 76
Amy 77
Bob 78
Cy 79
Dan 80
Eve 81
Amy 82
Bob 83
Cy 84
Dan 85
Eve 86
Amy 87
Bob 88
Cy 89
Dan 90
Eve 91
Amy 92
Bob 93
Cy 94
Dan 95
Eve 96
Amy 97
Bob 98
Cy 99
Dan 100
Eve 0
Amy 1
Bob 2
Cy 3
Dan 4
Eve 5
Amy 6
Bob 7
Cy 8
Dan 9
Eve 10
Amy 11
Bob 12
Cy 13
Dan 14
Eve 15
Amy 16
Bob 17
Cy 18
Dan 19
Eve 20
Amy 21
Bob 22
Cy 23
Dan 24
Eve 25
Amy 26
Bob 27
Cy 28
Dan 29
Eve 30
Amy 31
Bob 32
Cy 33
Dan 34
Eve 35
Amy 36
Bob 37
Cy 38
Dan 39
Eve 40
Amy 41
Bob 42
Cy 43
Dan 44
Eve 45
Amy 46
Bob 47
Cy 48
Dan 49
Eve 50
Amy 51
Bob 52
Cy 53
Dan 54
Eve 55
Amy 56
Bob 57
Cy 58
Dan 59
Eve 60
Amy 61
Bob 62
Cy 63
Dan 64
Eve 65
Amy 66
Bob 67
Cy 68
Dan 69
Eve 70
Amy 71
Bob 72
Cy 73
Dan 74
Eve 75
Amy 76
Bob 77
Cy 78
Dan 79
Eve 80
Amy 81
Bob 82
Cy 83
Dan 84
Eve 85
Amy 86
Bob 87
Cy 88
Dan 89
Eve 90
Amy 91
Bob 92
Cy 93
Dan 94
Eve 95
```

**Sample Output 9**
```
Amy 4954 100
Bob 4953 100
Cy 4952 100
Dan 4951 100
Eve 4950 100
```

**Tags**
STL, Map

---

## Find the Most Frequent Element using Map

**Problem Statement**
Given an array of `N` integers, find the element that appears most often. If more than one element ties for the highest frequency, print the smallest such element.

Use `std::map<int, int>` to count occurrences, then iterate the map to pick the winner. Because `std::map` iterates in ascending key order, scanning it once with a strict `>` on the current-best count naturally yields the smallest key on ties.

**Input Format**
- Line 1: an integer `N`, the size of the array.
- Line 2: `N` space-separated integers.

**Output Format**
A single integer - the most frequent element (smallest on ties).

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`

**Sample Input 0**
```
7
2 3 2 4 3 5 3
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
6
1 2 2 1 3 3
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
1
7
```

**Sample Output 2**
```
7
```

**Sample Input 3**
```
5
5 5 5 5 5
```

**Sample Output 3**
```
5
```

**Sample Input 4**
```
5
10 20 30 40 50
```

**Sample Output 4**
```
10
```

**Sample Input 5**
```
6
-1 -1 -2 -2 -3 -3
```

**Sample Output 5**
```
-3
```

**Sample Input 6**
```
8
1000000000 -1000000000 1000000000 -1000000000 0 0 0 0
```

**Sample Output 6**
```
0
```

**Sample Input 7**
```
9
4 4 4 2 2 2 1 1 1
```

**Sample Output 7**
```
1
```

**Sample Input 8**
```
7
-5 -5 -5 3 3 7 7
```

**Sample Output 8**
```
-5
```

**Sample Input 9**
```
1000
7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
```

**Sample Output 9**
```
7
```

**Tags**
STL, Map
