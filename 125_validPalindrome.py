def isPalindrome(self, s):
	filtered = ''.join(symbol.lower() for symbol in s if symbol.isalnum())
	return filtered == filtered[::-1]