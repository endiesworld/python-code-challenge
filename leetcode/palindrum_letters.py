def isPalindrome(s):
    """
        :type s: str
        :rtype: bool
        """
    # split words to enable removal of non-alphanumeric characters
    words = s.split()
    print(f"words after split: {words}")
    words = "".join(words)
    new_word = ""
    for char in words:
        if char.isalnum():
            new_word += char.lower()
    
    # confirm that the new word does not include alphabetic characters
    print(f"new_word after split: {new_word}")
    tot_len = len(new_word)
    
    # Palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.
    # Define a start index, stop index, and midpoint counter
    # The start index is to enable you pick words from the left
    # The stop index is to enable you pick words from the right
    # The counter which serves as the midpoint is to enable you stop and midpoints
    
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
