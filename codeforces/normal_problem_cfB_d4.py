# https://codeforces.com/contest/2044/problem/B
import sys

def normal_problem():
    text = input()
    rev_text = text[::-1]
    output = ''.join('q' if ch == 'p' else 'p' if ch == 'q' else ch for ch in rev_text)
    print(output)
  
if __name__ == "__main__":
    T = int(input()) # test case
    for _ in range(T):
        normal_problem()
      
