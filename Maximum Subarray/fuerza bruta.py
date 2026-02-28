class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = nums[0]
        for i in range(len(nums)):
          suma = 0
          for j in range(i, len(nums)):
            suma += nums[j]
            if suma > max :
              max = suma
        return max
"complejidad temporal O(n²) y espacial O(n)"
