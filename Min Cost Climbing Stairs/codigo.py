class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      prev1 = 0
      prev2 = 0
      for i in range(2, len(cost) + 1):
        curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
        prev2 = prev1
        prev1 = curr
      return prev1

---"complejidad temporal O(n) y espacio O(1)"
# Calcula el costo mínimo para subir una escalera donde puedes avanzar 1 o 2 pasos, 
#usando programación dinámica con solo dos variables en lugar de un arreglo completo.
