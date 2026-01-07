def uncompress(s):
  nums="0123456789"
  res=''
  i=0
  j=0
  while j<len(s):
    if s[j] in nums:
      j+=1
    else:
      num= int(s[i:j])
      if num ==1:
        res+=s[j]
      else:  
       res+= s[j]*num
      j+=1
      i=j
  return res