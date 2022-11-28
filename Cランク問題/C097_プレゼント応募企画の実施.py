"""
https://paiza.jp/works/challenges/480/retry
"""
from typing import List


class Solution:
    @staticmethod
    def balance(n_x_y: List[int]) -> List[str]:
        n, x, y = n_x_y
        people = []

        for i in range(1, n + 1):
            if i % x == 0 and i % y != 0:
                people.append("A")
            elif i % y == 0 and i % x != 0:
                people.append("B")
            elif i % y == 0 and i % x == 0:
                people.append("AB")
            else:
                people.append("N")

        return people


if __name__ == '__main__':
    input_line = list(map(int, input().split()))
    for j in Solution().balance(input_line):
        print(j)
