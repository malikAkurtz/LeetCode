'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

def isAnagram(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}
    for letter in s:
        s_dict[letter] = 0

    for letter in s:
        s_dict[letter] += 1
    
    for letter in t:
        t_dict[letter] = 0

    for letter in t:
        t_dict[letter] += 1

    return s_dict == t_dict

print(isAnagram("anagram","nagara"))


     