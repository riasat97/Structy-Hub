## longest word

Write a function, _longest\_word_, that takes in a sentence string as an argument. The function should return
the longest word in the sentence. If there is a tie, return the word that occurs later in the sentence.

You can assume that the sentence is non-empty.


#### test_00:

```python
longest_word("what a wonderful world") # -> "wonderful"
```

#### test_01:

```python
longest_word("have a nice day") # -> "nice"
```

#### test_02:

```python
longest_word("the quick brown fox jumped over the lazy dog") # -> "jumped"
```

#### test_03:

```python
longest_word("who did eat the ham") # -> "ham"
```

#### test_04:

```python
longest_word("potato") # -> "potato"
```