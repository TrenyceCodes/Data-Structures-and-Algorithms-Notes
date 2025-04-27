# Big O Notation Introduction
 - Big O notation - a mathematical simplified analysis that tells us how much slower a piece of algorithm is
   - Input size is represented by the N variable
   - Time/Space Complexity

 - Types of Measurements
   - Worse-Case
   - Best-Case
   - Average Case

- Note
   - Ignore Constants -> 5n translates to O(n)
   - certain terms "dominate" others (good -> horrible)
      - O(1) -> O(log n) -> O(n) -> O(n log n) -> O(n^2) -> O(2^n) -> O(!)
   - Describes the performance of an algorithm as the amount of data increases
   - Machine independent(# of steps to completion)