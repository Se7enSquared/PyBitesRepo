def rotate(string, n): 
   if n < 0:
      substring = string[n:]
      final_string = substring + string[:n]
   else:
      substring = string[:n]
      final_string =  string[n:] + substring
   return final_string