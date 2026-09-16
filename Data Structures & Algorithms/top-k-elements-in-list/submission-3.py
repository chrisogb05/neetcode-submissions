class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # num_set = list(set(nums))
        # result = []
        # for i in range(k):
        #     freq = nums[0]
        #     for j in num_set:
        #         if nums.count(j) > nums.count(freq):
        #             freq = j

        #     result.append(freq)
        #     for l in range(nums.count(freq)):
        #         nums.pop(nums.index(freq))
        # return result
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result