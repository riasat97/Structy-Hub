## has subarray sum

Write a function, _has\_subarray\_sum_, that takes in an list of _numbers_ and a _target\_sum_. The
function should return a boolean indicating whether or not there exists a subarray of _numbers_ that
sums to the given target.

A subarray is a consecutive series of one or more elements of the list.

#### test_00:

```python
has_subarray_sum([1, 3, 1, 4, 3], 8) # -> True
```

#### test_01:

```python
has_subarray_sum([1, 3, 1, 4, 3], 2) # -> False
```

#### test_02:

```python
has_subarray_sum([1, 3, 1, 1, 3], 2) # -> True
```

#### test_03:

```python
has_subarray_sum([5], 5) # -> True
```

#### test_04:

```python
has_subarray_sum([4, 2, 5, 1, 5, -2, 8], 9) # -> True
```

#### test_05:

```python
has_subarray_sum([4, 2, 5, 1, 5, -2, 8], 10) # -> False
```

#### test_06:

```python
has_subarray_sum([1, 1, 1, 1, 1, 1, 1, 1, 1], 9) # -> True
```

#### test_07:

```python
has_subarray_sum([1, 1, 1, 1, 1, 1, 1, 1, 1], 10) # -> False
```

