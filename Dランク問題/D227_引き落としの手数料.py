class Solution:
    def __init__(self):
        self.fee = 120

    def balance(self, n: int) -> int:
        return n - self.fee


if __name__ == '__main__':
    input_line = int(input())
    print(Solution().balance(input_line))
