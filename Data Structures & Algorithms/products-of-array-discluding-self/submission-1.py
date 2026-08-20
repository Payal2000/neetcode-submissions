class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Left hand side (Prefix)
        n = len(nums)
        prefix = 1
        res = [1] * n

        for i in range(n):
            res[i] = prefix
            prefix = prefix * nums[i]

        # Right hand side (Postfix)
        postfix = 1

        for i in range(n-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res


        




    


        