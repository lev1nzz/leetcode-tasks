from typing import List

def reverseString(s: List[str]):
   s[:] = s[::-1]
   print(s)
    

reverseString(['H','e','l','l','o'])