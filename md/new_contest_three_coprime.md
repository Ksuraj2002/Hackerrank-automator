# Three Coprime Numbers

## Three Coprime Numbers

**Difficulty**: Medium

**Problem Statement**
Three integers are coprime if `gcd(a, b, c) == 1`. Given three integers, print `YES` if they are coprime, otherwise print `NO`.

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
The only positive number that divides all three of `2`, `3`, and `4` is `1`. So `gcd(2, 3, 4) = 1`, which means they are coprime. The answer is `YES`.

**Sample Input 1**
```
2 4 8
```

**Sample Output 1**
```
NO
```

**Explanation 1**
`2` divides all three numbers `2`, `4`, and `8`. So `gcd(2, 4, 8) = 2`, which is not `1`. They are not coprime, so the answer is `NO`.

---

