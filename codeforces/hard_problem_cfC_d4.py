# Problem link: https://codeforces.com/contest/2044/problem/C
import sys

def hard_problem():
    m, a, b, c = map(int, input().split())
    # monkey with preference
    first_row_seats = min(a, m)
    second_row_seats = min(b, m)
    # monkey without preference
    remaining_seats = (2 * m) - (first_row_seats + second_row_seats)
    no_pref = min(c, remaining_seats)
    # total monkey can be seated
    can_seat = first_row_seats + second_row_seats + no_pref
    print(can_seat)
    


if __name__ == "__main__":
    T = int(input()) # test case
    for _ in range(T):
        hard_problem()
    



