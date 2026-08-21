class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Put nums in a hash set

        numSet = set(nums)

        longest = 0

        # Check for the beginning of the sequence (Check left)

        for num in nums:

            if num - 1 not in numSet:
                length = 1 

            # Check right for the sequence
                while num + length in numSet:
                    length += 1

                longest = max(longest, length)


        return longest

            


    











        