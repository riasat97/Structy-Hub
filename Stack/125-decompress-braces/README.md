## decompress braces

Write a function, *decompress_braces*, that takes in a compressed string as an argument. The function should
return the string decompressed. 

The compression format of the input string is 'n{sub_string}', where the *sub_string* within braces should be repeated _n_ times.

You may assume that every number _n_ is guaranteed to be an integer between 1 through 9.

You may assume that the input is valid and the decompressed string will only contain alphabetic characters.

#### test_00:

```python
decompress_braces("2{q}3{tu}v")
# -> qqtututuv 
```

#### test_01:

```python
decompress_braces("ch3{ao}")
# -> chaoaoao
```


#### test_02:

```python
decompress_braces("2{y3{o}}s")
# -> yoooyooos
```


#### test_03:

```python
decompress_braces("z3{a2{xy}b}")
# -> zaxyxybaxyxybaxyxyb 
```

#### test_04:

```python
decompress_braces("2{3{r4{e}r}io}")
# -> reeeerreeeerreeeerioreeeerreeeerreeeerio 
```

#### test_05:

```python
decompress_braces("go3{spinn2{ing}s}")
# -> gospinningingsspinningingsspinningings 
```

#### test_06:

```python
decompress_braces("2{l2{if}azu}l")
# -> lififazulififazul 
```

#### test_07:

```python
decompress_braces("3{al4{ec}2{icia}}")
# -> alececececiciaiciaalececececiciaiciaalececececiciaicia 
```