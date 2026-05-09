class Solution:

  "complejidad temporal, mejor y peor caso O(n) se recorre solo una vez - complejidad espacial O(1)"
    def maxSubArray(self, nums: List[int]) -> int:
      current_sum = nums[0]
      max_sum = nums[0]

      for i in range (1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

      return max_sum
# Encuentra la suma máxima de un subarreglo contiguo (algoritmo de Kadane). Por cada elemento decide 
#si extender el subarreglo actual o empezar uno nuevo, manteniendo registro del máximo global.
