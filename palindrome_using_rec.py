def is_Palindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return is_Palindrome(s[1:-1])
    else:
        return False


n = input("Enter a string: ").strip()

if is_Palindrome(n):
    print(f"'{n}' is a palindrome!")
else:
    print(f"'{n}' is not a palindrome!")