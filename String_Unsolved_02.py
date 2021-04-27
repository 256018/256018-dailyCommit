def remove_char(str, n):
      before_n = str[:n] 
      after_n = str[n+1:]
      return before_n + after_n

print(remove_char('Rohan', 0))
print(remove_char('Rohan', 2))
