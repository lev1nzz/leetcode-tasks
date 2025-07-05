def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    return x == int(str(x)[::-1])   

        
print(isPalindrome(10))