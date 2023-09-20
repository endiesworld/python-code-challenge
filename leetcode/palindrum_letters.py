def isPalindrome(s):
    """
        :type s: str
        :rtype: bool
        """
    words = s.split()
    print(f"words after split: {words}")
    words = "".join(words)
    new_word = ""
    for char in words:
        if char.isalnum():
            new_word += char.lower()
    print(f"new_word after split: {new_word}")
    tot_len = len(new_word)
    start = 0
    stop = -1
    counter = tot_len // 2
    print(f"Letters to check: {new_word}")
    while(start < counter):
        if (new_word[start] == new_word[stop]):
            start += 1
            stop -= 1
        else:
            break
    return True if start == counter else False


print(isPalindrome("0P"))
