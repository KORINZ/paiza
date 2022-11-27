from typing import List
from collections import deque


class Solution:
    @staticmethod
    def driving_school(n: int, a: List[int]) -> int:
        car_id = [i + 1 for i in range(n)]
        circle_count = 0
        i = 0

        if list(a) == car_id:
            return circle_count
        elif a[0] != N and a[-1] != N:
            circle_count -= 1

        a = deque(a)

        while a:

            if a[0] != car_id[i]:
                a.append(a.popleft())
            elif a[0] == car_id[i]:
                a.popleft()
                i += 1

            if a and N == a[0]:
                circle_count += 1

        return circle_count


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for i in range(N)]
    print(Solution().driving_school(N, A))
