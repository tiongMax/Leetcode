// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

class Solution {
    private Set<String> visited = new HashSet<>();
    private Set<String> cycle = new HashSet<>(); 
    private Set<String> supplies;                 
    private Map<String, List<String>> recipeMap;  

    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        this.supplies = new HashSet<>(Arrays.asList(supplies));
        this.recipeMap = new HashMap<>();
        for (int i = 0; i < recipes.length; i++) {
            this.recipeMap.put(recipes[i], ingredients.get(i));
        }

        List<String> res = new ArrayList<>();
        for (String recipe : recipes) {
            if (dfs(recipe)) {
                res.add(recipe);
            }
        }
        return res;
    }

    private boolean dfs(String food) {
        if (this.supplies.contains(food) || this.visited.contains(food)) return true; 
        if (this.cycle.contains(food) || !this.recipeMap.containsKey(food)) return false;   

        this.cycle.add(food); 
        for (String ingredient : this.recipeMap.get(food)) { 
            if (!dfs(ingredient)) {
                return false;
            }
        }

        this.cycle.remove(food);    
        this.visited.add(food);     
        return true;
    }
}
