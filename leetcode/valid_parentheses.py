"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    
    Input: s = "()"
    Output: true
    
    Input: s = "()[]{}"
    Output: true
    
    Input: s = "(]"
    Output: false

"""

class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in [')', '}', ']']:
            return False
        if s[0] == s[-1]:
            return False

        string_store = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        close = []
        counter = 0
        for char in s:
            if char in string_store:
                close.append(string_store[char])
                counter += 1
            elif(counter > 0):
                if(close[-1] != char):
                    return False
                else:
                    close.pop()
                    counter -= 1
            else:
                return False
        return True if counter == 0 else False


test_1 = "{[]}"
test_2 = "["
test_3 = "(){}}{"
test_4 = "(["
test_5 = "()"
test_6 = "()[]{}"
test_7 = "(]"

tests = [test_1, test_2, test_3, test_4, test_5, test_6, test_7]

operation = Solution()

for test in tests:
    print(operation.isValid(test))

