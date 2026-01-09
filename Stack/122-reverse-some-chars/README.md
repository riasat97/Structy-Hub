## reverse some chars

Write a function, *reverse_some_chars*, that takes in string and an list of target characters. The function
should return the string with the order of the given characters in reverse.

#### test_00:

```python
reverse_some_chars("computer", ["a", "e", "i", "o", "u"]) # -> 'cemputor'

# 'o', 'u', and 'e' are target characters in 'computer'
# so their relative order should be reversed to result in 'cemputor'
```

#### test_01:

```python
reverse_some_chars("skateboard", ["a", "e", "i", "o", "u"]) # -> 'skatobeard'
```

#### test_02:

```python
reverse_some_chars("airplane", ["m", "n", "r"]) # -> 'ainplare'
```

#### test_03:

```python
reverse_some_chars("building", ["g", "d", "i"]) # -> 'buglidni'
```
