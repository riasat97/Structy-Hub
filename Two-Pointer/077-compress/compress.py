def compress(s):
  s= s+'!'
  res=[]
  i=0
  j=0
  while j < len(s):
   if s[j]==s[i]:
     j+=1
   else:
     num= len(s[i:j])
     if num==1:
       res.append(s[i])
     else:
       res.append(str(num)+s[i])
     i=j
  return ''.join(res)

print(compress('ccaaatsss'))