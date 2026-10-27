# -*- coding: utf-8 -*-
"""Authored problem specs, keyed by the canonical key from parse_curriculum.py.

One entry per unique question. `solve` is a reference solution used to COMPUTE
every sample output at build time, so no sample can drift from its statement.

spec keys:
  title        challenge name on HackerRank (prefixed with Classwork:/Homework: at build)
  tags         HackerRank tags
  lc           LeetCode number, or None; the link is rendered into the statement
  statement    problem statement body (markdown)
  input_fmt / output_fmt / constraints
  samples      list of raw stdin strings
  solve        fn(stdin_str) -> stdout_str
"""

LC_SLUGS = {
    53: "maximum-subarray",
}


def lc_url(num):
    slug = LC_SLUGS.get(num)
    return "https://leetcode.com/problems/%s/" % slug if slug else None


# ----------------------------------------------------------------- solutions
def _solve_reverse_number(stdin):
    n = int(stdin.split()[0])
    sign = -1 if n < 0 else 1
    rev = int(str(abs(n))[::-1])
    return str(sign * rev)


def _solve_factors(stdin):
    n = int(stdin.split()[0])
    return " ".join(str(d) for d in range(1, n + 1) if n % d == 0)


def _solve_pyramid(stdin):
    n = int(stdin.split()[0])
    return "\n".join(" " * (n - i) + "*" * (2 * i - 1) for i in range(1, n + 1))


def _solve_max_subarray(stdin):
    nums = [int(x) for x in stdin.strip().split("\n")[1].split()]
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return str(best)


def _solve_last_digit(stdin):
    return str(int(stdin.split()[0]) % 10)


def _solve_drop_last_digit(stdin):
    return str(int(stdin.split()[0]) // 10)


def _solve_simple_interest(stdin):
    p, r, t = [float(x) for x in stdin.split()]
    return "%.2f" % (p * r * t / 100.0)


def _solve_grading(stdin):
    m = int(stdin.split()[0])
    if m > 90:
        return "excellent"
    if m > 80:
        return "good"
    if m > 70:
        return "fair"
    if m > 60:
        return "meets expectations"
    if m > 40:
        return "below par"
    return "failed"


def _solve_age_category(stdin):
    age = int(stdin.split()[0])
    if age > 70:
        return "Super Senior Citizen"
    if age >= 59:
        return "Senior Citizen"
    if age >= 18:
        return "Adult"
    if age > 1:
        return "Underage"
    return "New Born"


def _make_chocolate(stdin):
    small, big, goal = [int(x) for x in stdin.split()]
    big_used = min(big, goal // 5)
    rest = goal - big_used * 5
    return str(rest) if rest <= small else "-1"


def _make_bricks(stdin):
    small, big, goal = [int(x) for x in stdin.split()]
    big_used = min(big, goal // 5)
    return "true" if goal - big_used * 5 <= small else "false"


# ----------------------------------------------------------------------- bank
BANK = {
    "reverse-a-number": {
        "title": "Reverse the Digits of an Integer",
        "tags": ["Loops", "Number Theory"],
        "lc": None,
        "statement": (
            "Riya is building a digital odometer display. When the vehicle reverses, the "
            "display must show the odometer reading with its digits written back to front.\n\n"
            "Given an integer `N`, print the integer formed by reversing the order of its "
            "digits. Leading zeros produced by the reversal disappear because the answer is "
            "printed as an integer - reversing `4500` gives `54`.\n\n"
            "If `N` is negative the minus sign stays in front: reversing `-3020` gives `-203`.\n\n"
            "Work through the number one digit at a time: take the last digit with `N % 10`, "
            "append it to a running answer with `ans = ans * 10 + digit`, then drop the "
            "consumed digit with `N / 10`. Do not convert the number to a string."
        ),
        "input_fmt": "A single line containing one integer `N`.",
        "output_fmt": "A single line containing `N` with the order of its digits reversed.",
        "constraints": (
            "- `-2 * 10^9 <= N <= 2 * 10^9`\n"
            "- Time Complexity: `O(number of digits)`\n"
            "- Space Complexity: `O(1)`"
        ),
        "samples": ["45983", "4500", "-3020", "7", "1000000"],
        "solve": _solve_reverse_number,
    },
    "print-all-factors-of-n": {
        "title": "List Every Factor of N",
        "tags": ["Loops", "Number Theory"],
        "lc": None,
        "statement": (
            "A factor (divisor) of `N` is a positive integer that divides `N` leaving no "
            "remainder. For `N = 12` the factors are `1 2 3 4 6 12`.\n\n"
            "Given a positive integer `N`, print all of its factors in increasing order on a "
            "single line, separated by single spaces.\n\n"
            "The direct solution tests every candidate from `1` to `N` with `N % i == 0`, "
            "which costs `O(N)`. Once that works, try the `O(sqrt(N))` improvement: whenever "
            "`i` divides `N`, both `i` and `N / i` are factors - collect both and sort before "
            "printing. Careful with perfect squares, where `i` and `N / i` coincide."
        ),
        "input_fmt": "A single line containing one integer `N`.",
        "output_fmt": (
            "A single line with all factors of `N` in increasing order, separated by a single "
            "space."
        ),
        "constraints": (
            "- `1 <= N <= 10^6`\n"
            "- Time Complexity: `O(sqrt(N))` expected, `O(N)` accepted\n"
            "- Space Complexity: `O(number of factors)`"
        ),
        "samples": ["12", "1", "37", "36", "100"],
        "solve": _solve_factors,
    },
    "pyramid-of-stars": {
        "title": "Centred Star Pyramid",
        "tags": ["Patterns", "Nested Loops"],
        "lc": None,
        "statement": (
            "Given an integer `N`, print a centred pyramid of `N` rows built from the `*` "
            "character.\n\n"
            "Row `i` (1-indexed) contains exactly `N - i` leading spaces followed by "
            "`2*i - 1` stars, so the first row holds one star and the last row holds "
            "`2*N - 1` stars. A row has **no trailing spaces** after its last star.\n\n"
            "For `N = 4` the output is:\n\n"
            "```\n   *\n  ***\n *****\n*******\n```\n\n"
            "Use one outer loop over the rows and two inner loops inside it - one printing the "
            "spaces, one printing the stars."
        ),
        "input_fmt": "A single line containing one integer `N`, the number of rows.",
        "output_fmt": (
            "`N` lines forming the pyramid. Row `i` has `N - i` spaces followed by `2*i - 1` "
            "stars and no trailing spaces."
        ),
        "constraints": (
            "- `1 <= N <= 100`\n"
            "- Time Complexity: `O(N^2)`\n"
            "- Space Complexity: `O(1)` extra"
        ),
        "samples": ["4", "1", "2", "7", "10"],
        "solve": _solve_pyramid,
    },
    "lc53": {
        "title": "Maximum Subarray Sum (Kadane)",
        "tags": ["Arrays", "Kadane", "Dynamic Programming"],
        "lc": 53,
        "statement": (
            "Given an integer array `A` of size `N`, find the contiguous subarray containing "
            "at least one element that has the largest sum, and print that sum.\n\n"
            "A *subarray* is a run of consecutive elements: `[2, 3, 4]` is a subarray of "
            "`[1, 2, 3, 4, 5]`, but `[1, 3, 5]` is not.\n\n"
            "The array may contain negative numbers, and it may be **entirely** negative. "
            "Because the chosen subarray must be non-empty, the answer for an all-negative "
            "array is its largest (least negative) element - not `0`. That edge case is the "
            "one most submissions get wrong.\n\n"
            "Kadane's algorithm solves this in a single pass. Walk left to right holding "
            "`cur`, the best sum of a subarray ending at the current index. At each element "
            "either extend the previous run or start a new one - `cur = max(A[i], cur + A[i])` "
            "- and keep the largest `cur` ever seen."
        ),
        "input_fmt": (
            "- The first line contains an integer `N`, the size of the array.\n"
            "- The second line contains `N` space-separated integers, the elements of `A`."
        ),
        "output_fmt": "A single line containing the maximum subarray sum.",
        "constraints": (
            "- `1 <= N <= 10^5`\n"
            "- `-10^4 <= A[i] <= 10^4`\n"
            "- Time Complexity: `O(N)`\n"
            "- Space Complexity: `O(1)`"
        ),
        "samples": [
            "9\n-2 1 -3 4 -1 2 1 -5 4",
            "1\n1",
            "5\n5 4 -1 7 8",
            "4\n-5 -2 -9 -3",
            "6\n-1 -2 -3 4 -1 -2",
        ],
        "solve": _solve_max_subarray,
    },

    # ------------------------------------------------------------------
    # Questions the standardised sheet adds that are absent on HackerRank.
    # See tools/verdicts.json for why each one is treated as missing.
    # ------------------------------------------------------------------
    "find-the-last-digit-of-a-given-number-say-45983": {
        "title": "Last Digit of a Number",
        "tags": ["Operators", "Basics"],
        "lc": None,
        "statement": (
            "A billing system needs the final digit of an invoice number to pick a "
            "verification counter.\n\n"
            "Given a non-negative integer `N`, print only its last digit. For `N = 45983` the "
            "last digit is `3`.\n\n"
            "You do not need a loop for this. Dividing by `10` in integer arithmetic throws "
            "away the last digit, and the remainder operator keeps exactly that digit: "
            "`N % 10` is the answer. Watch what happens when the last digit is `0` - "
            "`100 % 10` is `0`, and `0` is the correct output, not an empty line."
        ),
        "input_fmt": "A single line containing one non-negative integer `N`.",
        "output_fmt": "A single line containing the last digit of `N`.",
        "constraints": (
            "- `0 <= N <= 10^9`\n"
            "- Time Complexity: `O(1)`\n"
            "- Space Complexity: `O(1)`"
        ),
        "samples": ["45983", "7", "100", "999999999", "0"],
        "solve": _solve_last_digit,
    },
    "remove-the-last-digit-of-a-given-number-say-45983": {
        "title": "Drop the Last Digit",
        "tags": ["Operators", "Basics"],
        "lc": None,
        "statement": (
            "Given a non-negative integer `N`, print the number that remains after its last "
            "digit is removed. For `N = 45983` the answer is `4598`.\n\n"
            "This is the companion of finding the last digit. Where `N % 10` keeps the last "
            "digit, integer division `N / 10` discards it - as long as both operands are "
            "integers, C++ throws the fractional part away rather than rounding.\n\n"
            "A single-digit input has nothing left once its only digit is removed, so the "
            "answer for `N = 7` is `0`."
        ),
        "input_fmt": "A single line containing one non-negative integer `N`.",
        "output_fmt": "A single line containing `N` with its last digit removed.",
        "constraints": (
            "- `0 <= N <= 10^9`\n"
            "- Time Complexity: `O(1)`\n"
            "- Space Complexity: `O(1)`"
        ),
        "samples": ["45983", "7", "100", "40", "1000000"],
        "solve": _solve_drop_last_digit,
    },
    "take-input-of-p-r-t-and-calculate-si": {
        "title": "Simple Interest",
        "tags": ["Operators", "Basics"],
        "lc": None,
        "statement": (
            "A bank quotes interest on a deposit using the simple-interest formula\n\n"
            "```\nSI = (P * R * T) / 100\n```\n\n"
            "where `P` is the principal amount, `R` is the annual rate of interest in per "
            "cent, and `T` is the time in years.\n\n"
            "Read `P`, `R` and `T` and print the simple interest, rounded to exactly two "
            "decimal places.\n\n"
            "Two things to be careful about. First, read the values into `double` variables - "
            "the rate can be fractional, like `7.5`. Second, dividing by `100` must not be "
            "integer division: if all three inputs are stored as `int`, `P * R * T / 100` "
            "truncates and the answer comes out wrong. Print with a fixed two decimals, for "
            "example `cout << fixed << setprecision(2) << si;`."
        ),
        "input_fmt": (
            "A single line containing three space-separated values: `P` (principal), "
            "`R` (annual rate per cent) and `T` (time in years). Any of them may be decimal."
        ),
        "output_fmt": "A single line containing the simple interest, printed with exactly two decimal places.",
        "constraints": (
            "- `0 <= P <= 10^7`\n"
            "- `0 <= R <= 100`\n"
            "- `0 <= T <= 100`\n"
            "- Answer must match to two decimal places\n"
            "- Time Complexity: `O(1)`"
        ),
        "samples": ["1000 5 2", "2500 7.5 3", "500 2.25 4", "10000 12 1", "1 1 1"],
        "solve": _solve_simple_interest,
    },
    "grading-system-1-you-are-given-as-input-marks-of-a-student-2-display-an-appropri": {
        "title": "Grading System: Marks to Message",
        "tags": ["Conditionals", "else-if ladder"],
        "lc": None,
        "statement": (
            "A school reports a student's performance as a message rather than a letter "
            "grade. Given the marks scored by a student, print the matching message using "
            "these bands:\n\n"
            "```\nmarks > 90                 -> excellent\n"
            "80 < marks <= 90           -> good\n"
            "70 < marks <= 80           -> fair\n"
            "60 < marks <= 70           -> meets expectations\n"
            "40 < marks <= 60           -> below par\n"
            "marks <= 40                -> failed\n```\n\n"
            "Print the message exactly as written above, in lower case, with no extra "
            "punctuation.\n\n"
            "Note that every boundary value belongs to the *lower* band: `90` is `good`, not "
            "`excellent`, and `40` is `failed`, not `below par`. An else-if ladder handles "
            "this naturally - test `marks > 90` first, then `marks > 80`, and so on, so each "
              "test only sees values the earlier tests rejected. Writing the bands as "
            "independent `if` statements is where this problem usually goes wrong."
        ),
        "input_fmt": "A single line containing one integer, the marks scored by the student.",
        "output_fmt": (
            "A single line containing one of `excellent`, `good`, `fair`, "
            "`meets expectations`, `below par` or `failed`."
        ),
        "constraints": (
            "- `0 <= marks <= 100`\n"
            "- Time Complexity: `O(1)`\n"
            "- Space Complexity: `O(1)`"
        ),
        "samples": ["95", "90", "71", "65", "41", "40"],
        "solve": _solve_grading,
    },
    "take-age-as-input-from-the-user-a-print-super-senior-citizen-if-age-is-above-70-": {
        "title": "Age Category Ladder",
        "tags": ["Conditionals", "else-if ladder"],
        "lc": None,
        "statement": (
            "A transport service prices tickets by age category. Given a person's age in "
            "years, print their category using these bands:\n\n"
            "```\nage > 70                   -> Super Senior Citizen\n"
            "59 <= age <= 70            -> Senior Citizen\n"
            "18 <= age <= 58            -> Adult\n"
            "1 < age <= 17              -> Underage\n"
            "age <= 1                   -> New Born\n```\n\n"
            "Print the category exactly as written, including capitalisation.\n\n"
            "An else-if ladder is the clean way to do this: order the tests from the oldest "
            "band downwards, and each later test can assume the earlier ones failed. If you "
            "write five separate `if` statements instead, an age of `75` will match several "
            "bands and print more than one line."
        ),
        "input_fmt": "A single line containing one integer, the age in years.",
        "output_fmt": (
            "A single line containing one of `Super Senior Citizen`, `Senior Citizen`, "
            "`Adult`, `Underage` or `New Born`."
        ),
        "constraints": (
            "- `0 <= age <= 120`\n"
            "- Time Complexity: `O(1)`\n"
            "- Space Complexity: `O(1)`"
        ),
        "samples": ["75", "70", "59", "30", "10", "1"],
        "solve": _solve_age_category,
    },
    "coding-bat-make-chocolates-and-bricks-problem": [
        {
            "title": "Make Chocolate (CodingBat)",
            "tags": ["Conditionals", "Greedy", "CodingBat"],
            "lc": None,
            "statement": (
                "The CodingBat classic *makeChocolate*. Reference: "
                "https://codingbat.com/prob/p191363\n\n"
                "You need to make a goal weight of chocolate using small bars of `1` kilo "
                "each and big bars of `5` kilos each. Print the **number of small bars** to "
                "use, assuming you always use big bars before small ones. Print `-1` if the "
                "goal weight cannot be made exactly.\n\n"
                "The greedy rule is forced: use as many big bars as fit without overshooting, "
                "which is `min(big, goal / 5)` bars. Whatever weight is left must be covered "
                "one kilo at a time by small bars - if the remainder exceeds the number of "
                "small bars available, the goal is impossible and the answer is `-1`.\n\n"
                "With `small = 4`, `big = 1`, `goal = 9`: one big bar covers `5`, leaving `4`, "
                "and you have exactly `4` small bars, so the answer is `4`. With "
                "`small = 4`, `big = 1`, `goal = 10` the remainder is `5` but only `4` small "
                "bars exist, so the answer is `-1`."
            ),
            "input_fmt": (
                "A single line containing three space-separated integers: `small` (count of "
                "1-kilo bars), `big` (count of 5-kilo bars) and `goal` (the weight to make)."
            ),
            "output_fmt": (
                "A single line containing the number of small bars to use, or `-1` if the "
                "goal cannot be made exactly."
            ),
            "constraints": (
                "- `0 <= small <= 1000`\n"
                "- `0 <= big <= 1000`\n"
                "- `0 <= goal <= 10^5`\n"
                "- Time Complexity: `O(1)`"
            ),
            "samples": ["4 1 9", "4 1 10", "4 1 7", "6 2 7", "1 2 7", "60 100 550"],
            "solve": _make_chocolate,
        },
        {
            "title": "Make Bricks (CodingBat)",
            "tags": ["Conditionals", "Greedy", "CodingBat"],
            "lc": None,
            "statement": (
                "The CodingBat classic *makeBricks*. Reference: "
                "https://codingbat.com/prob/p118406\n\n"
                "You are building a row of bricks of a given goal length. You have small "
                "bricks that are `1` inch long and big bricks that are `5` inches long. Print "
                "`true` if it is possible to make a row of **exactly** the goal length using "
                "the bricks available, and `false` otherwise.\n\n"
                "You do not have to use every brick, and the big bricks cannot be broken up. "
                "So take as many big bricks as fit without overshooting - `min(big, goal / 5)` "
                "- and check whether the leftover length can be filled by the small bricks "
                "you have.\n\n"
                "With `small = 3`, `big = 1`, `goal = 8`: use the big brick for `5`, and the "
                "remaining `3` inches need `3` small bricks, which you have, so print `true`. "
                "With `small = 3`, `big = 1`, `goal = 9` the leftover is `4` but only `3` "
                "small bricks exist, so print `false`."
            ),
            "input_fmt": (
                "A single line containing three space-separated integers: `small` (count of "
                "1-inch bricks), `big` (count of 5-inch bricks) and `goal` (the length to "
                "build)."
            ),
            "output_fmt": "A single line containing `true` or `false`, in lower case.",
            "constraints": (
                "- `0 <= small <= 1000`\n"
                "- `0 <= big <= 1000`\n"
                "- `0 <= goal <= 10^5`\n"
                "- Time Complexity: `O(1)`"
            ),
            "samples": ["3 1 8", "3 1 9", "3 2 10", "3 1 7", "6 1 11", "1 4 12"],
            "solve": _make_bricks,
        },
    ],
}
