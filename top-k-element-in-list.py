class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dict = collections.defaultdict(int)
        for i in range(0, len(nums)):
            dict[nums[i]] += 1

        nums = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(nums[i][0])

        return res
