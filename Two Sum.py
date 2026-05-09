class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      "crear diccionario"
   
      numeros = {}
      for i, num in enumerate (nums):
        resultado = target - num
        
        if resultado in numeros:
          return [numeros[resultado], i]

        numeros[num] = i
          
"""Busca dos números en una lista que sumen el target. 
Usa un diccionario para guardar los números ya vistos y, por cada elemento, 
verifica si su complemento (target - num) ya existe en el diccionario. 
Retorna los índices de los dos números."""
