class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      "crear diccionario"

      numeros = {}
      for i, num in enumerate (nums):
        resultado = target - num
        
        if resultado in numeros:
          return [numeros[resultado], i]

        numeros[num] = i
