# DSA 101 - Classwork

Generated from `DSA_101_Curriculum.xlsx`, sheet `DSA_101`, column `Classwork`.
This file is the source of truth for `create_contests.py` - edit it here, not in
the spreadsheet, once you start filling in slugs.

- **Contest name:** DSA 101 - Classwork
- **Contest slug:** `dsa-101-classwork`
- **Counts:** 179 problems total - 164 codeable, 15 theory.

## How to fill this in

Every problem needs a **Slug** before it can be added to the contest. The slug is
the last path segment of the challenge URL on HackerRank:

```
https://www.hackerrank.com/challenges/simple-array-sum/problem
                                      ^^^^^^^^^^^^^^^^ this part
```

- Put the bare slug in the Slug column. No full URL, no backticks needed.
- Leave Slug empty for anything not mapped yet. Those are reported as unmapped
  and skipped; everything else still gets added.
- Rows with Type `theory` are paper or reading exercises with no judge problem.
  They are always skipped, whatever the Slug column says.
- `python resolve_slugs.py --classwork` uses HackerRank's own search to propose
  candidate slugs and writes them into this file. Review them before trusting
  them - a keyword search will happily return the wrong problem.
- Order matters: challenges are added to the contest in the order they appear
  below, so Day 1 problems land first.

---


## Week 1

### Day 1 - Getting started & Output

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D01-1 | Print "Hello, World!" | print-hello-world-36 | code |
| CW-D01-2 | Print your name, class and roll on separate lines |  | code |
| CW-D01-3 | Print a small ASCII box |  | code |

### Day 2 - Variables & data types

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D02-1 | Declare and print a variable of each type |  | code |
| CW-D02-2 | Area and perimeter of a rectangle | area-and-perimeter-5 | code |
| CW-D02-3 | Swap two numbers using a third variable | swap-the-numbers-without-using-a-third-variable | code |

### Day 3 - Operators

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D03-1 | Last digit and first digit of a number | first-and-last-digit-2 | code |
| CW-D03-2 | Sum of digits of a 3-digit number | sum-of-digits-of-a-five-digit-number | code |
| CW-D03-3 | Evaluate a mixed expression, then verify |  | theory |
| CW-D03-4 | Find the last digit of a given number. Say 45983 | classwork-last-digit-of-a-number | code |

| CW-D03-5 | Take input of p, r, t and calculate simple interest | classwork-simple-interest | code |
### Day 4 - Input with cin

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D04-1 | Read two numbers, print sum/diff/product | find-product-of-the-two-numbers-using-function | code |
| CW-D04-2 | Read radius, print circle area | area-of-a-circle-6-2 | code |
| CW-D04-3 | Read 3 marks, print total and average |  | code |

### Day 5 - Comparison & logical operators

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D05-1 | Print whether a > b | detect-whether-a-linked-list-contains-a-cycle | code |
| CW-D05-2 | Leap year as a boolean expression | is-leap-year-1 | code |
| CW-D05-3 | Is a character a vowel? print the bool | character-is-vowel-or-consonant-1 | code |


## Week 2

### Day 6 - if / if-else

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D06-1 | Odd or even | odd-even-pattern | code |
| CW-D06-2 | Eligible to vote |  | code |
| CW-D06-3 | Maximum of two numbers | two-numbers-6 | code |

### Day 7 - Nested if-else & else-if ladder

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D07-1 | Maximum of three | three-month-preparation-kit-maximum-perimeter-triangle | code |
| CW-D07-2 | Grade from marks (A/B/C/F) |  | code |
| CW-D07-3 | Triangle type from its sides | what-type-of-triangle | code |
| CW-D07-4 | Grading System - print a message band from marks | classwork-grading-system-marks-to-message | code |

### Day 8 - if + logical operators

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D08-1 | Leap year with branching | is-leap-year-1 | code |
| CW-D08-2 | Classify a character (vowel/consonant/digit) | print-character-1 | code |
| CW-D08-3 | Is a point inside a rectangle? |  | code |
| CW-D08-4 | Coding Bat - Make Chocolate | classwork-make-chocolate-codingbat | code |

| CW-D08-5 | Coding Bat - Make Bricks | classwork-make-bricks-codingbat | code |
### Day 9 - switch-case

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D09-1 | Calculator using switch | switch-calculator-1-1 | code |
| CW-D09-2 | Day of the week from a number |  | code |
| CW-D09-3 | Vowel check using switch | vowel-checker-1 | code |

### Day 10 - char & String

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D10-1 | Print the ASCII of a character | print-character-1 | code |
| CW-D10-2 | Convert case using ASCII |  | code |
| CW-D10-3 | Count vowels in a string | count-vowels-8-1 | code |


## Week 3

### Day 11 - for loop

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D11-1 | Print 1..N and even numbers to N | print-even-numbers-4-1 | code |
| CW-D11-2 | Sum of first N numbers | sum-of-even-numbers-till-n-1 | code |
| CW-D11-3 | Multiplication table | multiplication-table-36 | code |

### Day 12 - for loop - number problems

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D12-1 | Print all factors of N | print-all-factors-of-a-number | code |
| CW-D12-2 | Count digits | count-number-of-digits-1-2 | code |
| CW-D12-3 | Reverse a number | reverse-of-a-number-8 | code |

### Day 13 - while & do-while

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D13-1 | Sum of digits with while | sum-of-digits-81-3 | code |
| CW-D13-2 | Reverse a number with while | reverse-of-a-number-8 | code |
| CW-D13-3 | Count digits with while | count-number-of-digits-1-2 | code |

### Day 14 - Nested loops

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D14-1 | Print a grid of numbers | print-the-numbers-to-n- | code |
| CW-D14-2 | Tables 1..10 with nested loops |  | code |
| CW-D14-3 | Count all pairs (i, j) | count-the-pairs-of-tracks | code |

### Day 15 - Loop practice

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D15-1 | Sum of a series | sum-of-fibonacci-series-4 | code |
| CW-D15-2 | Count multiples in a range | count-the-number-of-vowel-strings-in-range-1 | code |
| CW-D15-3 | Print a simple triangle | right-angled-triangle-6 | code |


## Week 4

### Day 16 - Patterns I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D16-1 | Solid square of stars |  | code |
| CW-D16-2 | Right-angled triangle | right-angled-triangle-6 | code |
| CW-D16-3 | Inverted right-angled triangle | print-the-pattern-31-3 | code |

### Day 17 - Patterns II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D17-1 | Pyramid of stars |  | code |
| CW-D17-2 | Inverted pyramid |  | code |
| CW-D17-3 | Number pyramid | number-finding | code |

### Day 18 - Patterns III

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D18-1 | Full diamond of stars |  | code |
| CW-D18-2 | Hollow triangle |  | code |
| CW-D18-3 | Alphabet pattern | print-n-1-1 | code |

### Day 19 - Time Complexity I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D19-1 | Calculate TC of a standard for loop |  | theory |
| CW-D19-2 | Calculate TC of a while loop halving N |  | theory |
| CW-D19-3 | Differentiate O(1) ops from O(N) ops |  | theory |

### Day 20 - Time Complexity II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D20-1 | TC of nested loop (1 to N, 1 to N) |  | theory |
| CW-D20-2 | TC of dependent loop (i from 1 to N, j from 1 to i) |  | theory |
| CW-D20-3 | TC of i *= 2 loop (Log N) |  | theory |


## Week 5

### Day 21 - Time & Space Complexity

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D21-1 | Space complexity of creating an array of size N |  | theory |
| CW-D21-2 | Space complexity of basic recursion |  | theory |
| CW-D21-3 | Time-Space trade-off examples |  | theory |

### Day 22 - Functions - basics

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D22-1 | isPrime(n) |  | code |
| CW-D22-2 | factorial(n) | n-factorial-2-1 | code |
| CW-D22-3 | max(a, b) | max-vowels | code |

### Day 23 - Multi-parameter functions

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D23-1 | nCr using a factorial helper |  | code |
| CW-D23-2 | power(base, exp) | power-of-4 | code |
| CW-D23-3 | Area functions for shapes |  | code |

### Day 24 - Digit problems

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D24-1 | Reverse a number | reverse-of-a-number-8 | code |
| CW-D24-2 | Sum of digits | sum-of-digits-81-3 | code |
| CW-D24-3 | Count digits | count-number-of-digits-1-2 | code |

### Day 25 - Primes & factors

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D25-1 | isPrime optimized |  | code |
| CW-D25-2 | Print primes 1..N | print-primes-1-1 | code |
| CW-D25-3 | Count factors of N | print-factors-of-number | code |


## Week 6

### Day 26 - GCD, LCM & number basics

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D26-1 | GCD using Euclid |  | code |
| CW-D26-2 | LCM of two numbers | lcm-of-two-numbers-8-1 | code |
| CW-D26-3 | Check if two numbers are coprime | two-numbers-6 | code |

### Day 27 - Recursion - intro

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D27-1 | Factorial recursively | n-factorial-2-1 | code |
| CW-D27-2 | Print 1..N and N..1 recursively |  | code |
| CW-D27-3 | Sum of digits recursively | sum-of-digits-81-3 | code |

### Day 28 - Recursion - practice

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D28-1 | Nth Fibonacci number | nth-fibonacci-number-7 | code |
| CW-D28-2 | All subsequences of a string | toggle-all-characters-in-a-string | code |
| CW-D28-3 | Sum of an array recursively | simple-array-sum | code |

### Day 29 - Arrays - intro

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D29-1 | Read N values and print them |  | code |
| CW-D29-2 | Print in reverse order by index |  | code |
| CW-D29-3 | Print elements at even indices | array-basic-iv | code |

### Day 30 - Array traversal

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D30-1 | Max and min in one pass | max-and-min-5 | code |
| CW-D30-2 | Average of the array | average-it | code |
| CW-D30-3 | Count elements above the average |  | code |


## Week 7

### Day 31 - Sorting basics I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D31-1 | Bubble sort implementation | gkstr44-bubble-sort | code |
| CW-D31-2 | Selection sort implementation | gkstr45-selection-sort | code |
| CW-D31-3 | Trace selection sort on paper |  | theory |

### Day 32 - Sorting basics II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D32-1 | Insertion sort implementation | insertion-sort-28-5 | code |
| CW-D32-2 | Trace insertion sort shifts |  | theory |
| CW-D32-3 | Compare stability of Bubble vs Selection |  | theory |

### Day 33 - std::sort & comparators

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D33-1 | Sort a vector ascending / descending | cc03-half-ascending-half-descending | code |
| CW-D33-2 | Sort vector of pairs by the second value |  | code |
| CW-D33-3 | Sort strings by length |  | code |

### Day 34 - Linear search

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D34-1 | Linear search - return the index |  | code |
| CW-D34-2 | Count occurrences of x | count-the-occurrences | code |
| CW-D34-3 | First and last index of x | first-and-last-digit-2 | code |

### Day 35 - Binary search

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D35-1 | LC704 Binary Search | search-in-array-2 | code |
| CW-D35-2 | LC35 Search Insert Position | search-insert-position-2-1 | code |
| CW-D35-3 | First occurrence using binary search | search-an-element-in-array-using-binary-search | code |


## Week 8

### Day 36 - Reverse & rearrange

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D36-1 | Reverse an array in place | gkstr32-reverse-array | code |
| CW-D36-2 | Swap first and last | first-and-last-digit-2 | code |
| CW-D36-3 | Reverse a sub-range | reverse-in-range | code |

### Day 37 - Rotation

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D37-1 | Rotate right by 1 | rotate-right-1 | code |
| CW-D37-2 | Rotate by k using reversal | tuple-reversal | code |
| CW-D37-3 | Left rotate by k | array-left-rotation | code |

### Day 38 - Array practice

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D38-1 | Check if the array is sorted and rotated (LC1752) | check-if-array-is-sorted-and-rotated-1 | code |
| CW-D38-2 | Sum of a given range | sum-finding | code |
| CW-D38-3 | Merge two sorted arrays | merge-two-sorted-arrays-7 | code |

### Day 39 - Prefix sums & range queries

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D39-1 | Build a prefix-sum array | positive-prefix | code |
| CW-D39-2 | LC303 Range Sum Query - Immutable | range-minimum-query | code |
| CW-D39-3 | Equilibrium index via prefix sum | print-prefix-sum | code |

### Day 40 - Maximum subarray (Kadane)

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D40-1 | LC53 Maximum Subarray | maximum-subarray-sum | code |
| CW-D40-2 | Track the start and end indices of max sum |  | code |
| CW-D40-3 | Subarray with largest sum (all negatives case) | subarray-with-given-sum-8 | code |


## Week 9

### Day 41 - Count / frequency arrays

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D41-1 | Frequency of each element | sort-the-array-according-to-their-cubes-of-each-element | code |
| CW-D41-2 | Most frequent element | most-occurred-character-1 | code |
| CW-D41-3 | Count of distinct elements | bash-tutorials-count-the-number-of-elements-in-an-array | code |

### Day 42 - Count-array problems

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D42-1 | LC242 Valid Anagram | valid-anagram-5 | code |
| CW-D42-2 | LC387 First Unique Character in a String | first-unique-character-in-a-string-4 | code |
| CW-D42-3 | Counting sort a small-range array |  | code |

### Day 43 - Two pointers - intro

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D43-1 | Reverse using two pointers |  | code |
| CW-D43-2 | LC167 Two Sum II - Input Array Is Sorted | merge-two-unsorted-array-in-sorted-form- | code |
| CW-D43-3 | String palindrome check | string-is-a-palindrome | code |

### Day 44 - Two pointers II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D44-1 | LC283 Move Zeroes | shift-zeroes | code |
| CW-D44-2 | Partition around a pivot | partition-array-according-to-given-pivot | code |
| CW-D44-3 | Move negatives to the left |  | code |

### Day 45 - Two pointers III

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D45-1 | LC15 3Sum |  | code |
| CW-D45-2 | LC26 Remove Duplicates from Sorted Array | remove-duplicates | code |
| CW-D45-3 | Count pairs with difference k | count-the-pairs-of-tracks | code |


## Week 10

### Day 46 - Sliding window

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D46-1 | Maximum sum window of size k (GfG) | maximum-element-in-window-of-size-k | code |
| CW-D46-2 | LC643 Maximum Average Subarray I | maximum-product-subarray-2 | code |
| CW-D46-3 | First negative in each window (GfG) | first-negative-integer-2 | code |

### Day 47 - Sliding window (Variable)

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D47-1 | LC209 Minimum Size Subarray Sum | max-subarray-sum-5 | code |
| CW-D47-2 | Longest subarray with sum <= k | subarray-with-given-sum-8 | code |
| CW-D47-3 | LC3 Longest Substring Without Repeating Characters (Intro) | longest-substring-without-repeating-characters-6-1 | code |

### Day 48 - Strings - deeper

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D48-1 | LC151 Reverse Words in a String | reverse-words-in-a-string-8 | code |
| CW-D48-2 | Count the words using stringstream | count-words-11 | code |
| CW-D48-3 | LC125 Valid Palindrome | cc01-is-palindrome | code |

### Day 49 - Strings & frequency

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D49-1 | LC242 Valid Anagram | valid-anagram-5 | code |
| CW-D49-2 | LC387 First Unique Character in a String | first-unique-character-in-a-string-4 | code |
| CW-D49-3 | Frequency of each character | character-by-frequency | code |

### Day 50 - 2-D arrays I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D50-1 | Read and print a matrix | ayush-and-his-matrix | code |
| CW-D50-2 | Sum of each row and column | largest-row-or-column-1 | code |
| CW-D50-3 | Sum of both diagonals |  | code |


## Week 11

### Day 51 - 2-D Arrays II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D51-1 | Transpose a matrix in place | transpose-of-matrix-4-1 | code |
| CW-D51-2 | LC48 Rotate Image | rotate-matrix- | code |
| CW-D51-3 | LC54 Spiral Matrix | spiral-matrix-44 | code |

### Day 52 - Bit Manipulation I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D52-1 | Print binary representation of N | print-binary-1 | code |
| CW-D52-2 | Check if a number is odd/even using Bitwise AND |  | code |
| CW-D52-3 | Swap two numbers using XOR | swap-2-numbers-3-1 | code |

### Day 53 - Bit Manipulation II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D53-1 | Check if k-th bit is set (GfG) | set-kth-bit-2 | code |
| CW-D53-2 | LC191 Number of 1 Bits | number-finding | code |
| CW-D53-3 | LC136 Single Number | single-number-3 | code |

### Day 54 - Bit Manipulation III

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D54-1 | LC231 Power of Two | power-of-two-number | code |
| CW-D54-2 | Clear rightmost set bit (N & (N-1)) | rightmost-set-bit-of-number | code |
| CW-D54-3 | Generate all subsets using bit manipulation (GfG) |  | code |

### Day 55 - Subarrays Deep Dive

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D55-1 | Print all subarrays of an array | print-subsets-1 | code |
| CW-D55-2 | Find max subarray sum using O(N^2) | max-subarray-sum-5 | code |
| CW-D55-3 | Check if any subarray has sum 0 (GfG) |  | code |


## Week 12

### Day 56 - Subarray Optimization

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D56-1 | LC53 Maximum Subarray (Review) | maximum-subarray-sum | code |
| CW-D56-2 | LC918 Maximum Sum Circular Subarray | maximum-sum-circular-subarray-2 | code |
| CW-D56-3 | LC560 Subarray Sum Equals K (Using prefix sums/hashmap intro) | max-subarray-sum-5 | code |

### Day 57 - Advanced String Manipulations

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D57-1 | LC14 Longest Common Prefix | common-prefix-1 | code |
| CW-D57-2 | LC28 Find the Index of the First Occurrence in a String | find-the-first-index | code |
| CW-D57-3 | LC415 Add Strings | find-strings | code |

### Day 58 - 2-D Matrix Searches

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D58-1 | LC74 Search a 2D Matrix | search-an-element-in-2-d-matrix | code |
| CW-D58-2 | LC240 Search a 2D Matrix II | search-an-element-in-2-d-matrix | code |
| CW-D58-3 | Find row with max 1s (GfG) |  | code |

### Day 59 - Mixed Problem Solving I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D59-1 | LC238 Product of Array Except Self | product-of-array-except-that-idx | code |
| CW-D59-2 | LC31 Next Permutation | find-the-permutation | code |
| CW-D59-3 | LC128 Longest Consecutive Sequence (Sorting approach) | longest-consecutive-sequence-2-2 | code |

### Day 60 - Wrap-up & Roadmap to Sem 3

| ID | Problem | Slug | Type |
|----|---------|------|------|
| CW-D60-1 | Mock Test: 3 standard problems (Easy, Med, Med) across Arrays/Strings/Bits |  | theory |
| CW-D60-2 | Dry run space/time analysis of your solutions |  | theory |

