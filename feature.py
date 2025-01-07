def isPalindrome(s):
    return s == s[::-1]

word = 'racecar'
ans = isPalindrome(word)

if ans:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")