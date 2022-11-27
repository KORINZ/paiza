from typing import List
from collections import deque


class Solution:
    @staticmethod
    def gondora(n_m: List[int], limit: List[int], group: List[int]) -> List[int]:

        n, m = n_m
        limit, group = deque(limit), deque(group)

        gondora_id_dict = {i: 0 for i in range(1, n + 1)}
        gondora_id = deque([i + 1 for i in range(n)])

        while group:

            if limit[0] >= group[0]:  # lower or equal to the limit of 1 gondora

                limit.append(limit.popleft())
                gondora_id_dict[gondora_id[0]] += group[0]
                gondora_id.append(gondora_id.popleft())
                group.popleft()

            else:  # too many people for 1 gondora
                gondora_id_dict[gondora_id[0]] += limit[0]
                group[0] = group[0] - limit[0]
                limit.append(limit.popleft())
                gondora_id.append(gondora_id.popleft())

        return list(gondora_id_dict.values())


if __name__ == '__main__':
    N_M = list(map(int, input().split()))
    A = [int(input()) for i in range(N_M[0])]
    B = [int(input()) for i in range(N_M[1])]
    for i in Solution().gondora(N_M, A, B):
        print(i)
