## anagrams

Write a function, _anagrams_, that takes in two strings as arguments. The function should return
a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same
characters, but in any order.

#### test_00:

```python
anagrams('restful', 'fluster') # -> True
```

#### test_01:

```python
anagrams('cats', 'tocs') # -> False
```

#### test_02:

```python
anagrams('monkeyswrite', 'newyorktimes') # -> True
```

#### test_03:

```python
anagrams('paper', 'reapa') # -> False
```

#### test_04:

```python
anagrams('elbow', 'below') # -> True
```

#### test_05:

```python
anagrams('tax', 'taxi') # -> False
```

#### test_06:

```python
anagrams('taxi', 'tax') # -> False
```

#### test_07:

```python
anagrams('night', 'thing') # -> True
```

#### test_08:

```python
anagrams('abbc', 'aabc') # -> False
```

#### test_09:

```python
anagrams('po', 'popp') # -> false
```

#### test_10:

```python
anagrams('pp', 'oo') # -> false
```