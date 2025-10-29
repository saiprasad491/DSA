def isPalindrome(s,st,en):
  if st >= en:
    return "Yes"
  return "Yes" if s[st]==s[en] and isPalindrome(s,st+1,en-1) else "No"

s = "malayalam"
print(f"{s} is palindrome {isPalindrome(s,0,len(s)-1)}")
s = "madam"
print(f"{s} is palindrome {isPalindrome(s,0,len(s)-1)}")
s = "sir"
print(f"{s} is palindrome {isPalindrome(s,0,len(s)-1)}")