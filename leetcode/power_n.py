import sys
"""
https://leetcode.com/problems/powx-n/submissions/
Personaly, this does not qualify to be a challenge because it is just staright forward
Also, to improve performance, we can devide the quotient (n) by the prime numbers (2,3,5,7,13 etc.)
"""
def main(x, n):
    if n > 0:
        return x ** n
    else:
        y = 1/x
        return y ** abs(n)

if __name__ == '__main__':
    x = float(sys.argv[1])
    n = int(sys.argv[2])
    print(main(x, n))