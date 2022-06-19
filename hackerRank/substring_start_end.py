"""
start() & end()
These expressions return the indices of the start and end of the substring matched by the group.
Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


# input_str = input()
# search_str = input()
input_str = input()
search_str = input()
# pattern = '^{}'.format(search_str)
match_count = 0
ans = []
index = 0
while index < len(input_str):
    match = re.search(search_str, input_str[index:])
    if match:
        start = match.start() + index
        stop = match.end()-1 + index
        ans.append((start, stop))
        if start == stop:
            index += match.end()
        else:
            index += match.end()-1

    else:
        break


print(ans)
