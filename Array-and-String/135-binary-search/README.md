# binary search

Write a function, *binary\_search*, that takes in a sorted list of numbers and a target. The function
should return the index where the target can be found within the list. If the target is not found
in the list, then return -1.

You may assume that the input array contains unique numbers sorted in increasing order.

Your function must implement the
[binary search algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm).

#### test_00

```python
binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) # -> 6
```

#### test_01

```python
binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) # -> -1
```

#### test_02

```python
binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8) # -> 2
```

#### test_03

```python
binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 28) # -> 8
```

#### test_04

```python
binary_search([7, 9], 7) # -> 0
```

#### test_05

```python
binary_search([7, 9], 9) # -> 1
```

#### test_06

```python
binary_search([7, 9], 12) # -> -1
```

#### test_07

```python
binary_search([7], 7) # -> 0
```

#### test_08

```python
binary_search([], 7) # -> -1
```
