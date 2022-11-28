"""
https://paiza.jp/career/challenges/533/retry
"""
from typing import List


class Solution:
    @staticmethod
    def cinmena(n_h_w_p_q: List[int], p_q: List) -> List:
        n, h, w, p, q = n_h_w_p_q
        reserved = {i for i in p_q}
        available = {(x, y) for x in range(h) for y in range(w) if (x, y) not in reserved}

        min_manhattan_distance = min([abs(p - x) + abs(q - y) for (x, y) in available])
        best_seats = [(x, y) for (x, y) in available if abs(p - x) + abs(q - y) == min_manhattan_distance]

        return best_seats


if __name__ == '__main__':
    N_H_W_P_Q = list(map(int, input().split()))
    P_Q = [tuple(map(int, input().split())) for i in range(N_H_W_P_Q[0])]
    for i in Solution().cinmena(N_H_W_P_Q, P_Q):
        print(*i)
