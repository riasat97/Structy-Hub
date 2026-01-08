## is subsequence

Write a function, _is\_subsequence_, that takes in string_1 and string_2. The function should return a boolean indicating whether or
not string_1 is a subsequence of string_2.

A subsequence is a string that can be formed by deleting 0 or more characters from another string.

#### test_00:

```python
is_subsequence("bde", "abcdef") # -> True
```

#### test_01:

```python
is_subsequence("bda", "abcdef") # -> False
```

#### test_02:

```python
is_subsequence("ser", "super") # -> True
```

#### test_03:

```python
is_subsequence("serr", "super") # -> False
```

#### test_04:

```python
is_subsequence("ama", "camera") # -> True
```

#### test_05:

```python
is_subsequence("unfun", "unfortunate") # -> True
```

#### test_06:

```python
is_subsequence("riverbed", "river") # -> False
```

#### test_07:

```python
is_subsequence("river", "riverbed") # -> True
```
