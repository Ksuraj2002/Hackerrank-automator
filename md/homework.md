# DSA 101 - Homework

Generated from `DSA_101_Curriculum.xlsx`, sheet `DSA_101`, column `Homework`.
This file is the source of truth for `create_contests.py` - edit it here, not in
the spreadsheet, once you start filling in slugs.

- **Contest name:** DSA 101 - Homework
- **Contest slug:** `dsa-101-homework`
- **Counts:** 120 problems total - 111 codeable, 9 theory.

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
- `python resolve_slugs.py --homework` uses HackerRank's own search to propose
  candidate slugs and writes them into this file. Review them before trusting
  them - a keyword search will happily return the wrong problem.
- Order matters: challenges are added to the contest in the order they appear
  below, so Day 1 problems land first.

---


## Week 1

### Day 1 - Getting started & Output

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D01-1 | Print your daily timetable as text |  | code |
| HW-D01-2 | Print a 4-line ASCII figure |  | code |

### Day 2 - Variables & data types

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D02-1 | Print sizeof of each type |  | code |
| HW-D02-2 | Celsius to Fahrenheit converter | fahrenheit-and-celsius | code |

### Day 3 - Operators

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D03-1 | Total seconds to h:m:s |  | code |
| HW-D03-2 | Simple interest calculator | power-calculator | code |
| HW-D03-3 | Remove the last digit of a given number. Say 45983 | homework-drop-the-last-digit | code |

### Day 4 - Input with cin

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D04-1 | Bill = price x quantity (2 decimals) |  | code |
| HW-D04-2 | Read a 3-digit number, print sum of digits | sum-of-digits-of-a-five-digit-number | code |

### Day 5 - Comparison & logical operators

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D05-1 | Voting eligibility as a boolean |  | code |
| HW-D05-2 | Print the truth tables of && and \|\| |  | theory |


## Week 2

### Day 6 - if / if-else

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D06-1 | Positive, negative or zero | classifying-feedbacks-into-positive-or-negative | code |
| HW-D06-2 | Divisible by 5? | divisible-by-7-or-not | code |

### Day 7 - Nested if-else & else-if ladder

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D07-1 | Largest of three distinct numbers |  | code |
| HW-D07-2 | Calculator using if-else | pos-neg-if-else | code |

### Day 8 - if + logical operators

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D08-1 | Ticket price by age group |  | code |
| HW-D08-2 | Valid triangle and its type | what-type-of-triangle | code |
| HW-D08-3 | Take age as input and print the age category | homework-age-category-ladder | code |

### Day 9 - switch-case

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D09-1 | Menu-driven program | menu-driven-calculator-1 | code |
| HW-D09-2 | Number of days in a month |  | code |

### Day 10 - char & String

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D10-1 | Reverse a string | reverse-a-string-1-4 | code |
| HW-D10-2 | Check a one-word palindrome | one-month-preparation-kit-richie-rich | code |


## Week 3

### Day 11 - for loop

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D11-1 | Print N down to 1 | down-with-abstractions | code |
| HW-D11-2 | Factorial with a loop | n-factorial-2-1 | code |

### Day 12 - for loop - number problems

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D12-1 | Repeated digit sum to one digit | one-month-preparation-kit-recursive-digit-sum | code |
| HW-D12-2 | Check Armstrong number | armstrong-number-138 | code |

### Day 13 - while & do-while

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D13-1 | GCD by repeated subtraction |  | code |
| HW-D13-2 | Binary form of a number using while | form-the-largest-number | code |

### Day 14 - Nested loops

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D14-1 | Print all pairs with i < j | print-all-substrings | code |
| HW-D14-2 | Print a coordinate grid |  | code |

### Day 15 - Loop practice

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D15-1 | Arithmetic-progression sum |  | code |
| HW-D15-2 | Fibonacci series with a loop | sum-of-fibonacci-series-4 | code |


## Week 4

### Day 16 - Patterns I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D16-1 | Floyd's number triangle |  | code |
| HW-D16-2 | Hollow square | pattern-8-print-a-hollow-square-without-top | code |

### Day 17 - Patterns II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D17-1 | Half-diamond | half-it | code |
| HW-D17-2 | Right-aligned triangle | right-angled-triangle-6 | code |

### Day 18 - Patterns III

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D18-1 | Butterfly pattern | print-the-pattern-1-9 | code |
| HW-D18-2 | Pascal-style number pattern | print-the-number-pattern-2 | code |

### Day 19 - Time Complexity I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D19-1 | Read up on Omega and Theta notation |  | theory |
| HW-D19-2 | Determine TC of finding max element in array |  | theory |

### Day 20 - Time Complexity II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D20-1 | TC of three nested loops (O(N^3)) |  | theory |
| HW-D20-2 | TC of loop jumping by i+=2 vs i*=2 |  | theory |


## Week 5

### Day 21 - Time & Space Complexity

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D21-1 | Calculate SC of nested arrays (matrices) |  | theory |
| HW-D21-2 | Find O(1) space solutions vs O(N) solutions |  | theory |

### Day 22 - Functions - basics

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D22-1 | sumOfDigits(n) |  | code |
| HW-D22-2 | isPalindromeNumber(n) |  | code |

### Day 23 - Multi-parameter functions

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D23-1 | min/max of three via a function | three-month-preparation-kit-angry-children | code |
| HW-D23-2 | isLeapYear(y) returning bool |  | code |

### Day 24 - Digit problems

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D24-1 | Palindrome number | palindrome-number-48-1 | code |
| HW-D24-2 | Armstrong number; largest digit | armstrong-number-138 | code |

### Day 25 - Primes & factors

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D25-1 | Sieve of Eratosthenes |  | code |
| HW-D25-2 | Sum of divisors of N | sum-finding | code |


## Week 6

### Day 26 - GCD, LCM & number basics

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D26-1 | GCD of an array | find-gcd-of-array | code |
| HW-D26-2 | Reduce a fraction to lowest terms |  | code |

### Day 27 - Recursion - intro

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D27-1 | Fast power a^b | find-the-power-1 | code |
| HW-D27-2 | Recursive palindrome check | palindrome-checking-1 | code |

### Day 28 - Recursion - practice

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D28-1 | Count vowels recursively | count-vowels-8-1 | code |
| HW-D28-2 | Reverse a string recursively | reverse-a-string-1-4 | code |

### Day 29 - Arrays - intro

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D29-1 | Sum of an array | simple-array-sum | code |
| HW-D29-2 | Count positive elements | bash-tutorials-count-the-number-of-elements-in-an-array | code |

### Day 30 - Array traversal

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D30-1 | Second largest element | second-largest-number-16-2 | code |
| HW-D30-2 | Count even and odd | sum-of-even-odd-2 | code |


## Week 7

### Day 31 - Sorting basics I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D31-1 | Count total swaps in bubble sort |  | code |
| HW-D31-2 | Sort an array in descending order | sort-array-in-decreasing-order-using-custom-sort | code |

### Day 32 - Sorting basics II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D32-1 | Sort an array of strings by first letter |  | code |
| HW-D32-2 | Find median after sorting | find-target-indices-after-sorting-array | code |

### Day 33 - std::sort & comparators

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D33-1 | LC56 Merge Intervals (Intro - sort by start time) | merge-intervals-3 | code |
| HW-D33-2 | Sort array elements by frequency (Intro) | sort-array-by-increasing-frequency | code |

### Day 34 - Linear search

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D34-1 | Check if a value exists (boolean) |  | code |
| HW-D34-2 | Return index of the maximum element | index-of-element-1 | code |

### Day 35 - Binary search

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D35-1 | LC34 Find First and Last Position of Element in Sorted Array | hw-single-element-in-a-sorted-array | code |
| HW-D35-2 | Find Ceil of x in sorted array (GfG) | squares-of-a-sorted-array-2 | code |


## Week 8

### Day 36 - Reverse & rearrange

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D36-1 | Move all zeros to the end | push-all-zeros-to-end | code |
| HW-D36-2 | Check if the array is a palindrome | check-if-array-is-sorted-and-rotated-1 | code |

### Day 37 - Rotation

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D37-1 | Check if one array is a rotation of another | check-array-rotation-6 | code |
| HW-D37-2 | Rotate a matrix row | print-the-matrix-row-wise | code |

### Day 38 - Array practice

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D38-1 | Leaders in an array (GfG) | leaders-in-array-4 | code |
| HW-D38-2 | Rearrange positives and negatives alternately |  | code |

### Day 39 - Prefix sums & range queries

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D39-1 | LC724 Find Pivot Index | find-pivot-index-1 | code |
| HW-D39-2 | Range increment with a difference array (GfG) |  | code |

### Day 40 - Maximum subarray (Kadane)

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D40-1 | Maximum contiguous sum (GfG) | maximum-subarray-sum | code |
| HW-D40-2 | Largest sum of exactly k elements | k-largest-elements-5 | code |


## Week 9

### Day 41 - Count / frequency arrays

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D41-1 | Missing number in 1..N | missing-number-finder-1 | code |
| HW-D41-2 | Element appearing once |  | code |

### Day 42 - Count-array problems

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D42-1 | LC169 Majority Element | majority-element-ii | code |
| HW-D42-2 | Check if arrays are permutations of each other |  | code |

### Day 43 - Two pointers - intro

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D43-1 | LC977 Squares of a Sorted Array | squares-of-a-sorted-array-2 | code |
| HW-D43-2 | Remove duplicates from a sorted array (LC26) | squares-of-a-sorted-array-2 | code |

### Day 44 - Two pointers II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D44-1 | Merge two sorted arrays in place (LC88) | merge-two-sorted-arrays-7 | code |
| HW-D44-2 | Container with most water (intro) |  | code |

### Day 45 - Two pointers III

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D45-1 | LC16 3Sum Closest |  | code |
| HW-D45-2 | Two-sum on an unsorted array (hashing preview) | merge-two-unsorted-array-in-sorted-form- | code |


## Week 10

### Day 46 - Sliding window

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D46-1 | LC1343 Number of Subarrays of Size K and Average Greater than or Equal to Threshold |  | code |
| HW-D46-2 | Count occurrences of anagrams (GfG) | count-the-occurrences | code |

### Day 47 - Sliding window (Variable)

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D47-1 | Longest subarray with k distinct characters (GfG) | longest-substring-without-repeating-characters-6-1 | code |
| HW-D47-2 | Smallest window containing all characters of string (GfG) | toggle-all-characters-in-a-string | code |

### Day 48 - Strings - deeper

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D48-1 | Print all substrings | print-all-substrings | code |
| HW-D48-2 | Longest word in a sentence |  | code |

### Day 49 - Strings & frequency

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D49-1 | LC49 Group Anagrams (Intro via sorting strings) | anagrams-25-3 | code |
| HW-D49-2 | LC1047 Remove All Adjacent Duplicates In String | remove-all-adjacent-duplicates-in-string | code |

### Day 50 - 2-D arrays I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D50-1 | Row with the maximum sum | minimal-maximum-sum | code |
| HW-D50-2 | Check the identity matrix |  | code |


## Week 11

### Day 51 - 2-D Arrays II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D51-1 | LC59 Spiral Matrix II | spiral-matrix-44 | code |
| HW-D51-2 | LC73 Set Matrix Zeroes | set-matrix-zeroes-2 | code |

### Day 52 - Bit Manipulation I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D52-1 | Multiply/Divide a number by 2 using bit shifts |  | code |
| HW-D52-2 | XOR of numbers from 1 to N (GfG) | print-the-numbers-to-n- | code |

### Day 53 - Bit Manipulation II

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D53-1 | Set the rightmost unset bit (GfG) | rightmost-set-bit-of-number | code |
| HW-D53-2 | LC338 Counting Bits | counting-jumps | code |

### Day 54 - Bit Manipulation III

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D54-1 | LC268 Missing Number (Using XOR) | missing-number-finder-1 | code |
| HW-D54-2 | Find the two non-repeating elements (GfG) |  | code |

### Day 55 - Subarrays Deep Dive

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D55-1 | Count subarrays with sum exactly K (Brute force) | count-19-1 | code |
| HW-D55-2 | Product of all subarrays (GfG) | print-subsets-1 | code |


## Week 12

### Day 56 - Subarray Optimization

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D56-1 | LC974 Subarray Sums Divisible by K | subarray-sums-divisible-by-k | code |
| HW-D56-2 | Maximum product subarray (LC152) | maximum-product-subarray-2 | code |

### Day 57 - Advanced String Manipulations

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D57-1 | LC43 Multiply Strings | find-strings | code |
| HW-D57-2 | Check if a string is a valid shuffle of two strings (GfG) |  | code |

### Day 58 - 2-D Matrix Searches

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D58-1 | Median in a row-wise sorted Matrix (GfG) | print-the-matrix-row-wise | code |
| HW-D58-2 | LC378 Kth Smallest Element in a Sorted Matrix | kth-smallest-element-in-a-sorted-matrix-1-1 | code |

### Day 59 - Mixed Problem Solving I

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D59-1 | LC75 Sort Colors | sort-0-1-4 | code |
| HW-D59-2 | Trapping Rain Water (LC42 - Brute/Better approach) | trapping-rain-water-10-1 | code |

### Day 60 - Wrap-up & Roadmap to Sem 3

| ID | Problem | Slug | Type |
|----|---------|------|------|
| HW-D60-1 | Complete any pending HWs |  | theory |
| HW-D60-2 | Rest and prepare for DSA 301! |  | theory |

