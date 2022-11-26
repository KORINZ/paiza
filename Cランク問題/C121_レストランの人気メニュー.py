from typing import List


class Solution:
    @staticmethod
    def top_ten(n_c: List[int], r_cal: List[List[int]]) -> str or int:
        n, c = n_c

        top_list = [i + 1 for i in range(10)]
        current_cal = 0
        top_ten_had = []

        for i in r_cal:
            current_cal += i[1]

            if i[0] in top_list and current_cal <= c:
                top_ten_had.append(i[0])
            if current_cal >= c:
                break

        if sorted(top_ten_had) == top_list:
            return 'Yes'
        else:
            return len(top_ten_had)


if __name__ == '__main__':
    N_C = list(map(int, input().split()))
    R_Cal = [list(map(int, input().split())) for i in range(N_C[0])]
    print(Solution().top_ten(N_C, R_Cal))
