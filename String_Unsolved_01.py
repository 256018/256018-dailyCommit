def change_second(s1):
  char = s1[0]
  s1 = s1.replace(char, '$')
  s1 = char + s1[1:]
  return s1

print(change_second('restart'))
