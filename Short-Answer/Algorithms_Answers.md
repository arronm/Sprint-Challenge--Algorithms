#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n log n)


c) O(n)

## Exercise II

Start at the middle floor (f // 2)
If the egg breaks move to a floor below current and last tested // 2
If the egg does not break move to a floor above current and last tested // 2
When on the last floor, if the egg breaks your optimal floor is one below
If the egg does not break, this is your optimal floor

Proposed solution would be O(log n)