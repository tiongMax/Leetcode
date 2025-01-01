# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        sup = set(supplies)  
        hm = {recipes[i]: ingredients[i] for i in range(len(recipes))}  

        visited, cycle = set(), set()  
        def dfs(food):
            if food in sup or food in visited:  
                return True
            if food not in hm or food in cycle: 
                return False
            
            cycle.add(food)
            for ingredient in hm[food]:  
                if not dfs(ingredient):
                    return False
            cycle.remove(food)

            visited.add(food) 
            return True

        res = []
        for r in recipes:
            if dfs(r):  
                res.append(r)

        return res
