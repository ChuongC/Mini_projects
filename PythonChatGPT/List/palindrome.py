
def palindrome(s):
	s_reverse = ""
	for i in range(len(s)):
		chars = len(s) #
		s_reverse = s[chars-i-1]

		if (s[i] != s_reverse[i]):
			return False
		else:
			return True

print(palindrome("abababa"))