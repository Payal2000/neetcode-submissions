class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        # Create an empty hashmap
        occur = {}

        # Count frequency of each number 
        for num in nums:
            occur[num] = occur.get(num, 0) + 1

        # Create frequency buckets
        freq_bucket = [[] for i in range (n+1)]

        #Put each number into its frequency bucket
        for num in occur:
            frequency = occur[num]
            freq_bucket[frequency].append(num)

        # Create results
        res = []

        # Go from highest freq to lowest freq
        for frequency in range(n, 0 , -1):

            #Get every number in this frequency bucket:
            for num in freq_bucket[frequency]:
                res.append(num)

                #Once we have k numbers, return
                if len(res) ==k:
                    return res









