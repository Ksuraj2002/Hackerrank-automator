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

## Count Leaf Nodes

**Problem Statement**
Given the level-order traversal of a binary tree with `N` tokens (where `-1` denotes a missing child), count the number of leaf nodes. A leaf node is any node whose left and right children are both null.

Example: for tokens `1 2 3 -1 -1 4 5` the tree is

```
        1
       / \
      2   3
         / \
        4   5
```

Leaves are `2, 4, 5`, so the answer is `3`.

**Input Format**
- Line 1: an integer `N`, the number of tokens in the level-order description.
- Line 2: `N` space-separated integers. `-1` marks an absent child. The first token is the root; subsequent tokens fill the tree in breadth-first order.

**Output Format**
A single integer - the number of leaf nodes in the tree.

**Constraints**
- `1 <= N <= 10^5`
- Each node value fits in a 32-bit signed integer, or is `-1` for null.

**Sample Input 0**
```
7
1 2 3 -1 -1 4 5
```

**Sample Output 0**
```
3
```

**Sample Input 1**
```
1
42
```

**Sample Output 1**
```
1
```

**Sample Input 2**
```
3
5 -1 -1
```

**Sample Output 2**
```
1
```

**Sample Input 3**
```
7
1 2 3 4 5 6 7
```

**Sample Output 3**
```
4
```

**Sample Input 4**
```
5
1 2 -1 3 -1
```

**Sample Output 4**
```
1
```

**Sample Input 5**
```
5
1 -1 2 -1 3
```

**Sample Output 5**
```
1
```

**Sample Input 6**
```
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

**Sample Output 6**
```
8
```

**Sample Input 7**
```
9
10 20 30 -1 -1 40 -1 -1 50
```

**Sample Output 7**
```
3
```

**Sample Input 8**
```
11
-5 -10 -15 0 -1 -1 20 -1 -1 -1 30
```

**Sample Output 8**
```
3
```

**Sample Input 9**
```
1000
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 703 704 705 706 707 708 709 710 711 712 713 714 715 716 717 718 719 720 721 722 723 724 725 726 727 728 729 730 731 732 733 734 735 736 737 738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755 756 757 758 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773 774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791 792 793 794 795 796 797 798 799 800 801 802 803 804 805 806 807 808 809 810 811 812 813 814 815 816 817 818 819 820 821 822 823 824 825 826 827 828 829 830 831 832 833 834 835 836 837 838 839 840 841 842 843 844 845 846 847 848 849 850 851 852 853 854 855 856 857 858 859 860 861 862 863 864 865 866 867 868 869 870 871 872 873 874 875 876 877 878 879 880 881 882 883 884 885 886 887 888 889 890 891 892 893 894 895 896 897 898 899 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 920 921 922 923 924 925 926 927 928 929 930 931 932 933 934 935 936 937 938 939 940 941 942 943 944 945 946 947 948 949 950 951 952 953 954 955 956 957 958 959 960 961 962 963 964 965 966 967 968 969 970 971 972 973 974 975 976 977 978 979 980 981 982 983 984 985 986 987 988 989 990 991 992 993 994 995 996 997 998 999 1000
```

**Sample Output 9**
```
500
```

**Tags**
Trees, Recursion

---

## Check if Binary Tree is Height Balanced

**Problem Statement**
Given the level-order traversal of a binary tree (with `-1` marking null children), decide whether the tree is height balanced. A tree is height balanced when, for every node, the heights of its left and right subtrees differ by at most `1`.

**Input Format**
- Line 1: an integer `N`, the number of tokens.
- Line 2: `N` space-separated integers describing the tree in level-order; `-1` denotes a missing child.

**Output Format**
Print `true` if the tree is height balanced, `false` otherwise.

**Constraints**
- `1 <= N <= 10^5`
- Node values fit in a 32-bit signed integer, or are `-1` for null.

**Sample Input 0**
```
5
1 2 3 4 -1
```

**Sample Output 0**
```
true
```

**Sample Input 1**
```
5
1 2 -1 3 -1
```

**Sample Output 1**
```
false
```

**Sample Input 2**
```
1
7
```

**Sample Output 2**
```
true
```

**Sample Input 3**
```
7
1 2 3 4 5 6 7
```

**Sample Output 3**
```
true
```

**Sample Input 4**
```
3
1 2 -1
```

**Sample Output 4**
```
true
```

**Sample Input 5**
```
7
1 2 3 -1 -1 4 -1
```

**Sample Output 5**
```
true
```

**Sample Input 6**
```
9
1 2 3 4 -1 -1 -1 5 -1
```

**Sample Output 6**
```
false
```

**Sample Input 7**
```
7
1 2 3 -1 4 -1 -1
```

**Sample Output 7**
```
true
```

**Sample Input 8**
```
15
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```

**Sample Output 8**
```
true
```

**Sample Input 9**
```
201
1 2 -1 3 -1 4 -1 5 -1 6 -1 7 -1 8 -1 9 -1 10 -1 11 -1 12 -1 13 -1 14 -1 15 -1 16 -1 17 -1 18 -1 19 -1 20 -1 21 -1 22 -1 23 -1 24 -1 25 -1 26 -1 27 -1 28 -1 29 -1 30 -1 31 -1 32 -1 33 -1 34 -1 35 -1 36 -1 37 -1 38 -1 39 -1 40 -1 41 -1 42 -1 43 -1 44 -1 45 -1 46 -1 47 -1 48 -1 49 -1 50 -1 51 -1 52 -1 53 -1 54 -1 55 -1 56 -1 57 -1 58 -1 59 -1 60 -1 61 -1 62 -1 63 -1 64 -1 65 -1 66 -1 67 -1 68 -1 69 -1 70 -1 71 -1 72 -1 73 -1 74 -1 75 -1 76 -1 77 -1 78 -1 79 -1 80 -1 81 -1 82 -1 83 -1 84 -1 85 -1 86 -1 87 -1 88 -1 89 -1 90 -1 91 -1 92 -1 93 -1 94 -1 95 -1 96 -1 97 -1 98 -1 99 -1 100 -1 -1 -1
```

**Sample Output 9**
```
false
```

**Tags**
Trees, Recursion

---

## Next Greater Element using Set

**Problem Statement**
You are given an array `A` of `N` distinct integers. For every element `A[i]`, find the smallest value in `A` that is strictly greater than `A[i]` among all elements. If no such value exists, print `-1` for that position.

Use `std::set` (or an equivalent ordered set) to look up the next greater value in `O(log N)` per query.

**Input Format**
- Line 1: an integer `N`, the size of the array.
- Line 2: `N` space-separated distinct integers `A[0]..A[N-1]`.

**Output Format**
`N` space-separated integers on one line - the next greater element for each `A[i]` in order, or `-1` if none exists.

**Constraints**
- `1 <= N <= 10^5`
- `-10^9 <= A[i] <= 10^9`
- All `A[i]` are distinct.

**Sample Input 0**
```
5
4 1 7 3 9
```

**Sample Output 0**
```
7 3 9 4 -1
```

**Sample Input 1**
```
1
42
```

**Sample Output 1**
```
-1
```

**Sample Input 2**
```
5
1 2 3 4 5
```

**Sample Output 2**
```
2 3 4 5 -1
```

**Sample Input 3**
```
5
5 4 3 2 1
```

**Sample Output 3**
```
-1 5 4 3 2
```

**Sample Input 4**
```
6
-3 -1 -5 0 -2 -4
```

**Sample Output 4**
```
-2 0 -4 -1 -1 -3
```

**Sample Input 5**
```
2
1000000000 -1000000000
```

**Sample Output 5**
```
-1 1000000000
```

**Sample Input 6**
```
8
10 20 5 15 25 8 12 30
```

**Sample Output 6**
```
12 25 8 20 30 10 15 -1
```

**Sample Input 7**
```
4
100 200 50 150
```

**Sample Output 7**
```
150 -1 100 200
```

**Sample Input 8**
```
3
-1 0 1
```

**Sample Output 8**
```
0 1 -1
```

**Sample Input 9**
```
1000
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 703 704 705 706 707 708 709 710 711 712 713 714 715 716 717 718 719 720 721 722 723 724 725 726 727 728 729 730 731 732 733 734 735 736 737 738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755 756 757 758 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773 774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791 792 793 794 795 796 797 798 799 800 801 802 803 804 805 806 807 808 809 810 811 812 813 814 815 816 817 818 819 820 821 822 823 824 825 826 827 828 829 830 831 832 833 834 835 836 837 838 839 840 841 842 843 844 845 846 847 848 849 850 851 852 853 854 855 856 857 858 859 860 861 862 863 864 865 866 867 868 869 870 871 872 873 874 875 876 877 878 879 880 881 882 883 884 885 886 887 888 889 890 891 892 893 894 895 896 897 898 899 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 920 921 922 923 924 925 926 927 928 929 930 931 932 933 934 935 936 937 938 939 940 941 942 943 944 945 946 947 948 949 950 951 952 953 954 955 956 957 958 959 960 961 962 963 964 965 966 967 968 969 970 971 972 973 974 975 976 977 978 979 980 981 982 983 984 985 986 987 988 989 990 991 992 993 994 995 996 997 998 999 1000
```

**Sample Output 9**
```
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 270 271 272 273 274 275 276 277 278 279 280 281 282 283 284 285 286 287 288 289 290 291 292 293 294 295 296 297 298 299 300 301 302 303 304 305 306 307 308 309 310 311 312 313 314 315 316 317 318 319 320 321 322 323 324 325 326 327 328 329 330 331 332 333 334 335 336 337 338 339 340 341 342 343 344 345 346 347 348 349 350 351 352 353 354 355 356 357 358 359 360 361 362 363 364 365 366 367 368 369 370 371 372 373 374 375 376 377 378 379 380 381 382 383 384 385 386 387 388 389 390 391 392 393 394 395 396 397 398 399 400 401 402 403 404 405 406 407 408 409 410 411 412 413 414 415 416 417 418 419 420 421 422 423 424 425 426 427 428 429 430 431 432 433 434 435 436 437 438 439 440 441 442 443 444 445 446 447 448 449 450 451 452 453 454 455 456 457 458 459 460 461 462 463 464 465 466 467 468 469 470 471 472 473 474 475 476 477 478 479 480 481 482 483 484 485 486 487 488 489 490 491 492 493 494 495 496 497 498 499 500 501 502 503 504 505 506 507 508 509 510 511 512 513 514 515 516 517 518 519 520 521 522 523 524 525 526 527 528 529 530 531 532 533 534 535 536 537 538 539 540 541 542 543 544 545 546 547 548 549 550 551 552 553 554 555 556 557 558 559 560 561 562 563 564 565 566 567 568 569 570 571 572 573 574 575 576 577 578 579 580 581 582 583 584 585 586 587 588 589 590 591 592 593 594 595 596 597 598 599 600 601 602 603 604 605 606 607 608 609 610 611 612 613 614 615 616 617 618 619 620 621 622 623 624 625 626 627 628 629 630 631 632 633 634 635 636 637 638 639 640 641 642 643 644 645 646 647 648 649 650 651 652 653 654 655 656 657 658 659 660 661 662 663 664 665 666 667 668 669 670 671 672 673 674 675 676 677 678 679 680 681 682 683 684 685 686 687 688 689 690 691 692 693 694 695 696 697 698 699 700 701 702 703 704 705 706 707 708 709 710 711 712 713 714 715 716 717 718 719 720 721 722 723 724 725 726 727 728 729 730 731 732 733 734 735 736 737 738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755 756 757 758 759 760 761 762 763 764 765 766 767 768 769 770 771 772 773 774 775 776 777 778 779 780 781 782 783 784 785 786 787 788 789 790 791 792 793 794 795 796 797 798 799 800 801 802 803 804 805 806 807 808 809 810 811 812 813 814 815 816 817 818 819 820 821 822 823 824 825 826 827 828 829 830 831 832 833 834 835 836 837 838 839 840 841 842 843 844 845 846 847 848 849 850 851 852 853 854 855 856 857 858 859 860 861 862 863 864 865 866 867 868 869 870 871 872 873 874 875 876 877 878 879 880 881 882 883 884 885 886 887 888 889 890 891 892 893 894 895 896 897 898 899 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 920 921 922 923 924 925 926 927 928 929 930 931 932 933 934 935 936 937 938 939 940 941 942 943 944 945 946 947 948 949 950 951 952 953 954 955 956 957 958 959 960 961 962 963 964 965 966 967 968 969 970 971 972 973 974 975 976 977 978 979 980 981 982 983 984 985 986 987 988 989 990 991 992 993 994 995 996 997 998 999 1000 -1
```

**Tags**
STL, Set

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
