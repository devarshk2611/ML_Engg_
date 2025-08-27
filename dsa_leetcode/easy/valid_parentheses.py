"""
Problem: Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Approach:
- Use a stack to match opening and closing brackets.
- Push opening brackets.
- On closing, check if top of stack matches expected.
- Valid iff stack is empty at end.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def isValid(s):
    stack = []
    mp = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in mp:
            top = stack.pop() if stack else '#'
            if top != mp[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    print(isValid("()[]{}"))     # True
    print(isValid("(]"))         # False
    print(isValid("([{}])"))     # True
    print(isValid("((("))        # False
