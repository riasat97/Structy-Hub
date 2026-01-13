def detect_dictionary(dictionary, alphabet):
  for i in range(len(dictionary)-1):
    current= dictionary[i]
    next= dictionary[i+1]
    if not in lexical_order(current,next,alphabet):
      return False
  return True



def lexical_order(word_1, word_2, alphabet):
  max_length= max(len(word_1),len(word_2))
  #print(max_length)
  for i in range(0,max_length):
    value_1= alphabet.index(word_1[i]) if i<len(word_1) else float("-inf")
    value_2= alphabet.index(word_2[i]) if i<len(word_2) else float("-inf")
    if value_1<value_2:
      return True
    elif value_2<value_1:
      return False
  return True
