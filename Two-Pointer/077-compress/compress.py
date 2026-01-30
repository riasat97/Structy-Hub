# def compress(s):
#   s+='!'
#   res=[]
#   i=0
#   j=0
#   while j < len(s):
#    if s[j]==s[i]:
#      j+=1
#    else:
#      num= len(s[i:j])
#      #num= j-i
#      if num==1:
#        res.append(s[i])
#      else:
#        res.append(str(num)+s[i])
#      i=j
#   return ''.join(res)

#print(compress('ccaaatsss'))


def compress(s):
  s=s+'!'
  i=0
  j=0
  res=[]
  while i < len(s):
    if s[i]==s[j]:
      i+=1
    else:
      num_ch=len(s[j:i])
      if num_ch==1:
        res.append(s[j])
      else:
        res.append(str(num_ch)+s[j])
      j=i
  return ''.join(res)













