
def reverseVowels(s: str):
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    vowel_indices = [i for i, ch in enumerate(s_list) if ch in vowels]
    
    for i in range(len(vowel_indices)//2):
        left = vowel_indices[i]
        right = vowel_indices[-i-1]
        s_list[left], s_list[right] = s_list[right], s_list[left]
    
    print(''.join(s_list))
    
    
    
reverseVowels(s= "IceCreAm" )