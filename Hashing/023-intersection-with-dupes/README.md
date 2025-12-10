## intersection with dupes

Write a function, _intersection\_with\_dupes_, that takes in two lists, _a_,_b_, as arguments. The function
should return a new list containing elements that are common to both input lists. The elements in the
result should appear as many times as they occur in both input lists.

You can return the result in any order.

#### test_00:

```python
intersection_with_dupes(
  ["a", "b", "c", "b"], 
  ["x", "y", "b", "b"]
) # -> ["b", "b"]
```

#### test_01:

```python
intersection_with_dupes(
  ["q", "b", "m", "s", "s", "s"], 
  ["s", "m", "s"]
) # -> ["m", "s", "s"]
```

#### test_02:

```python
intersection_with_dupes(
  ["p", "r", "r", "r"], 
  ["r"]
) # -> ["r"]
```

#### test_03:

```python
intersection_with_dupes(
  ["r"], 
  ["p", "r", "r", "r"]
) # -> ["r"]
```

#### test_04:

```python
intersection_with_dupes(
  ["t", "v", "u"], 
  ["g", "e", "d", "f"]
) # -> [ ]
```

#### test_05:

```python
intersection_with_dupes(
  ["a", "a", "a", "a", "a", "a",], 
  ["a", "a", "a", "a"]
) # -> ["a", "a", "a", "a"]
```

#### test_06:

```python
a = []
b = [] 
for i in range(0, 150000):
  a.append(i)
  b.append(i)

intersection_with_dupes(a, b) # -> [0, 1, 2, ..., 149999]
```