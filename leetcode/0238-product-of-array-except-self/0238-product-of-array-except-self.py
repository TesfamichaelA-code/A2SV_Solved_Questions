class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums return array answer
        answer[i] is equal to nums * nums except nums[i]

        """
        n = len(nums)
        pref = [1] * n 
        suff = [1] * n
        answer = [0] * n
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        for j in range(n - 2, -1, -1):
            suff[j] = nums[j + 1] * suff[j + 1]
        for i in range(n):
            answer[i] = suff[i] * pref[i]
        return answer


