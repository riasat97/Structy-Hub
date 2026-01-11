## running sum

Write a function, _running\_sum_, that takes in a list of *numbers*. The function should return a new
list of the same length where each element contains the running sum up to that index of the original list.

```plaintext
For example, the i-th result should be the sum of all elements 0 to i:

result[i] = numbers[0] + numbers[1] + numbers[2] + ... + numbers[i]
```

#### test_00:

```python
running_sum([4, 2, 1, 6, 3, 6]) # -> [ 4, 6, 7, 13, 16, 22 ] 
```

#### test_01:

```python
running_sum([10, 5, -2, 1, 1]) # -> [ 10, 15, 13, 14, 15 ] 
```

#### test_02:

```python
running_sum([12, 88, 0, -50, 30, 2]) # -> [ 12, 100, 100, 50, 80, 82 ] 
```

#### test_03:

```python
running_sum([2]) # -> [ 2 ] 
```

#### test_04:

```python
running_sum([]) # -> [ ] 
```
