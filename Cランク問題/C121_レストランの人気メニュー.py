from typing import List


class Solution:
    @staticmethod
    def top_ten(n_c: List[int], r_cal: List[List[int]]) -> str or int:
        print(r_cal)


if __name__ == '__main__':
    N_C = list(map(int, input().split()))
    R_Cal = [list(map(int, input().split())) for i in range(N_C[0])]
    print(Solution().top_ten(N_C, R_Cal))
