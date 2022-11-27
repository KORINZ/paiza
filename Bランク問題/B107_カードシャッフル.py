from typing import List
import itertools


class Solution:
    @staticmethod
    def divide_card(card_set: List[int]) -> List[List[int]]:
        return [card_set[i:i + m] for i in range(0, n, m)]

    @staticmethod
    def shuffle_card(n_m_k: List[int]) -> List[int]:
        global n, m, back_to_undivided
        n, m, k = n_m_k
        card_set = [i + 1 for i in range(n)]
        divided_set = Solution().divide_card(card_set)

        for j in range(k):
            divided_set.reverse()
            back_to_undivided = list(itertools.chain.from_iterable(divided_set))
            divided_set = Solution().divide_card(back_to_undivided)
        return back_to_undivided


if __name__ == '__main__':
    N_M_K = list(map(int, input().split()))
    for card in Solution().shuffle_card(N_M_K):
        print(card)
