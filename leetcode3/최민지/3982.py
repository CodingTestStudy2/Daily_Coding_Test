class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        dict = {}
        for num in nums:
            num_list = list(map(int, str(num)))
            range = max(num_list) - min(num_list)
            if range not in dict:
                dict[range] = []
            dict[range].append(num)
        max_key = max(dict)

        return sum(dict[max_key])


        