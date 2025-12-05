## exclusive items

Write a function, _exclusive\_items_, that takes in two lists, _a_,_b_, as arguments. The function
should return a new list containing elements that are in either list but not both lists.

You may assume that each input list does not contain duplicate elements.

#### test_00:

```python
exclusive_items([4,2,1,6], [3,6,9,2,10]) # -> [4,1,3,9,10]
```

#### test_01:

```python
exclusive_items([2,4,6], [4,2]) # -> [6]
```

#### test_02:

```python
exclusive_items([4,2,1], [1,2,4,6]) # -> [6]
```

#### test_03:

```python
exclusive_items([0,1,2], [10,11]) # -> [0,1,2,10,11]
```

#### test_04:

```python
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
exclusive_items(a, b) # -> [ ]
```