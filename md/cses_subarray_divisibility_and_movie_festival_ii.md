# CSES — Subarray Divisibility & Movie Festival II

Two CSES problems packaged for the Automator pipeline.

---

## Subarray Divisibility
**Difficulty**: Medium

**Problem Statement**
Given an array of `n` integers, your task is to count the number of subarrays where the sum of values is divisible by `n`.

A subarray is a contiguous slice `a[l..r]` with `1 <= l <= r <= n`.

**Input Format**
- Line 1: a single integer `n` — the size of the array.
- Line 2: `n` space-separated integers `a_1, a_2, …, a_n` — the contents of the array.

**Output Format**
A single integer — the number of subarrays whose sum is divisible by `n`.

**Constraints**
- `1 <= n <= 3 * 10^5`
- `-10^9 <= a_i <= 10^9`
- The answer fits in a signed 64-bit integer.

**Sample Input 0**
```
5
3 1 2 7 4
```

**Sample Output 0**
```
1
```

**Sample Explanation 0**
We check every contiguous subarray of `[3, 1, 2, 7, 4]` and keep the ones whose sum is divisible by `n = 5`:
- Length 1: `3, 1, 2, 7, 4` → none divisible by 5.
- Length 2: `4, 3, 9, 11` → none divisible by 5.
- Length 3: `6, 10, 13` → `[1, 2, 7]` sums to `10` ✓.
- Length 4: `13, 14` → none.
- Length 5: `17` → not divisible.

Only one subarray qualifies, so the answer is `1`.

**Sample Input 1**
```
1
5
```

**Sample Output 1**
```
1
```

**Sample Explanation 1**
`n = 1` and every integer is divisible by `1`. The only subarray `[5]` has sum `5`, which is divisible by `1`, so the count is `1`.

**Sample Input 2**
```
3
1 2 3
```

**Sample Output 2**
```
3
```

**Sample Explanation 2**
Subarray sums are `1, 2, 3, 3, 5, 6`. The ones divisible by `n = 3` are `3` (from `[3]`), `3` (from `[1, 2]`), and `6` (from `[1, 2, 3]`) — three in total.

**Sample Input 3**
```
5
5 5 5 5 5
```

**Sample Output 3**
```
15
```

**Sample Explanation 3**
Every element is a multiple of `n = 5`, so every one of the `n*(n+1)/2 = 15` contiguous subarrays has a sum divisible by `5`.

**Sample Input 4**
```
4
-1 -2 -3 -4
```

**Sample Output 4**
```
1
```

**Sample Explanation 4**
Only the subarray `[-1, -2, -3, -4]` sums to `-10`… wait, `-10` is not divisible by `4`. Let us list every sum: `-1, -2, -3, -4, -3, -5, -7, -6, -9, -10`. The only one divisible by `4` is `-4` (from `[-4]`). The answer is `1`. This case verifies correct handling of negative values and the modulo convention `((x % n) + n) % n`.

**Sample Input 5**
```
6
2 -4 1 3 -2 6
```

**Sample Output 5**
```
4
```

**Sample Explanation 5**
Prefix sums (with a leading `0`) are `P = [0, 2, -2, -1, 2, 0, 6]`. Taken modulo `n = 6` (normalised to `[0, 5]`) they become `[0, 2, 4, 5, 2, 0, 0]`. Residue counts: `0`→`3`, `2`→`2`, `4`→`1`, `5`→`1`. The number of divisible subarrays is `C(3,2) + C(2,2) = 3 + 1 = 4`. Direct enumeration confirms the four qualifying subarrays: `[6]`, `[-4, 1, 3]`, `[2, -4, 1, 3, -2]`, and `[2, -4, 1, 3, -2, 6]`.

**Sample Input 6**
```
7
7 3 -1 4 2 -5 8
```

**Sample Output 6**
```
2
```

**Sample Explanation 6**
Prefix sums `0, 7, 10, 9, 13, 15, 10, 18`; residues mod `7`: `0, 0, 3, 2, 6, 1, 3, 4`. Residue `0` twice → `1` subarray (`a[1..1] = [7]`), residue `3` twice (indices `2` and `6`) → `1` subarray (`a[3..6] = [-1, 4, 2, -5]` sum `0`). Total `2`.

**Tags**
Prefix Sums, Modular Arithmetic, Hashing, Counting

---

## Movie Festival II
**Difficulty**: Medium-Hard

**Problem Statement**
In a movie festival, `n` movies will be shown. Syrjälä's movie club consists of `k` members, who will all be attending the festival. You know the starting and ending time of each movie. What is the maximum total number of movies the club members can watch entirely if they act optimally?

A member may watch any number of movies, but cannot watch two movies whose times overlap. A movie that starts exactly when another one ends is allowed (end-exclusive).

**Input Format**
- Line 1: two space-separated integers `n` and `k` — the number of movies and the number of club members.
- Next `n` lines: two space-separated integers `a` and `b` per line — the start and end time of a movie.

**Output Format**
A single integer — the maximum total number of movies the `k` members can watch end-to-end.

**Constraints**
- `1 <= k <= n <= 2 * 10^5`
- `1 <= a < b <= 10^9`

**Sample Input 0**
```
5 2
1 5
8 10
3 6
2 5
6 9
```

**Sample Output 0**
```
4
```

**Sample Explanation 0**
Sort movies by end time: `[1,5], [2,5], [3,6], [6,9], [8,10]`.
- Member A watches `[1, 5]`, finishing at `5`.
- Member B watches `[2, 5]`, finishing at `5`.
- `[3, 6]` starts at `3`; both members are still busy until `5`, so it is skipped.
- `[6, 9]` starts at `6`; member A became free at `5` → assign to A, A now finishes at `9`.
- `[8, 10]` starts at `8`; member B became free at `5` → assign to B, B now finishes at `10`.

Four movies are watched in total.

**Sample Input 1**
```
1 1
1 2
```

**Sample Output 1**
```
1
```

**Sample Explanation 1**
A single member, a single movie — trivially watched. Covers the smallest valid input.

**Sample Input 2**
```
3 1
1 10
2 3
4 5
```

**Sample Output 2**
```
2
```

**Sample Explanation 2**
With one member, this reduces to the classic activity-selection problem. Sorted by end time: `[2,3], [4,5], [1,10]`. Take `[2,3]`, then `[4,5]` (start `4` ≥ previous end `3`), skip `[1,10]` because `1 < 5`. Answer: `2`.

**Sample Input 3**
```
4 2
1 3
2 4
3 5
4 6
```

**Sample Output 3**
```
4
```

**Sample Explanation 3**
Two chains of non-overlapping movies: `[1,3] → [3,5]` for member A, `[2,4] → [4,6]` for member B. All four movies are watched, confirming that movies touching at endpoints are compatible.

**Sample Input 4**
```
4 1
1 5
2 6
3 7
4 8
```

**Sample Output 4**
```
1
```

**Sample Explanation 4**
Every pair of movies overlaps, so a single member can watch only one of them.

**Sample Input 5**
```
6 3
1 4
1 4
1 4
4 7
4 7
4 7
```

**Sample Output 5**
```
6
```

**Sample Explanation 5**
Three members each watch one `[1, 4]` movie, then each watches one `[4, 7]` movie. The matching must assign a *distinct* member to each simultaneous movie — this case exercises correct greedy assignment via a multiset of "member available-at" times.

**Sample Input 6**
```
7 2
1 3
2 5
4 7
6 9
8 10
3 4
5 6
```

**Sample Output 6**
```
6
```

**Sample Explanation 6**
Sorted by end time: `[1,3], [3,4], [2,5], [5,6], [4,7], [6,9], [8,10]`.
- A takes `[1,3]`.
- B takes `[3,4]` *(or A — the greedy picks the member with the latest end-time ≤ start, which is A at `3`)*. After this A ends at `4`.
- `[2,5]`: start `2` — neither member is free (A at `4`, B still at nothing… actually B is still at `0`, hence free). Assign to B, B ends at `5`.
  (The precise assignment depends on the multiset tie-breaks, but the *total count* is deterministic.)
- Continuing greedily yields `6` watched movies.

The point of this case: wrong tie-breaks between members still give the correct count when you always assign to the member with the greatest end-time `≤` current start.

**Tags**
Greedy, Sorting, Interval Scheduling, Multiset / Balanced BST

---

<!--
### Stress-case generation notes (author-only; not a challenge)

Put the large inputs under `tests/<slug>/large_XX.in` and their expected outputs under `tests/<slug>/large_XX.out`. Suggested generators:

### Subarray Divisibility — defeat `O(n^2)`
- `n = 200000`
- `a_i` uniformly random in `[-10^9, 10^9]`
- Include at least one test where every `a_i = n` (answer `n*(n+1)/2`) and one where every `a_i = 1` (answer = number of prefix-sum collisions).

### Movie Festival II — defeat `O(n·k)` and `O(n^2)`
- `n = 200000`, `k = 50000`
- Mix of (a) many short non-overlapping movies, (b) many fully overlapping movies, (c) nested movies.
- Include a case with `k = 1` to verify fallback to classic activity selection.
- Include a case with `k >= n` so that the answer equals `n`.

A naive solution must fail at least one of these within the `1.00 s` limit; the reference `O(n log n)` solution should finish comfortably under `300 ms`.
-->

