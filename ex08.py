def given_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(given_list([1,1,4,5,6,4,4,6,9])) 
