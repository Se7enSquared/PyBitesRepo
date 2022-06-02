def rotate(string, n): 
   if n < 0:
      substring = string[n:]
      return substring + string[:n]
   else:
      substring = string[:n]
      return string[n:] + substring