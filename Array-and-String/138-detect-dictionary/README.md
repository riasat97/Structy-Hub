## detect dictionary

Write a function, _detectDictionary_, that takes in a dictionary of words and an alphabet string.
The function should return a boolean indicating whether or not all words of the dictionary are
[lexically-ordered](https://en.wikipedia.org/wiki/Lexicographic_order) according to the alphabet.

You can assume that all characters are lowercase a-z.

You can assume that the alphabet contains all 26 letters.

#### test_00:

```python
dictionary = ["zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> True
```

#### test_01:

```python
dictionary = ["zoo", "tack", "tick", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> False
```

#### test_02:

```python
dictionary = ["zoos", "zoo", "tick", "tack", "door"]
alphabet = "ghzstijbacdopnfklmeqrxyuvw"
detect_dictionary(dictionary, alphabet) # -> False
```

#### test_03:

```python
dictionary = ["miles", "milestone", "proper", "process", "goal"]
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> True
```

#### test_04:

```python
dictionary = ["miles", "milestone", "pint", "proper", "process", "goal"];
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> True
```

#### test_05:

```python
dictionary = ["miles", "milestone", "pint", "proper", "process","goal", "apple"];
alphabet = "mnoijpqrshkltabcdefguvwzxy"
detect_dictionary(dictionary, alphabet) # -> False
```
