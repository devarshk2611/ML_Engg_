def reverse_string(s): return s[::-1]
def is_palindrome(s): return s == s[::-1]
def count_vowels(s): return sum(ch in "aeiouAEIOU" for ch in s)

if __name__ == "__main__":
    print(reverse_string("hello"))    # olleh
    print(is_palindrome("madam"))     # True
    print(count_vowels("Illinois"))   # 3
