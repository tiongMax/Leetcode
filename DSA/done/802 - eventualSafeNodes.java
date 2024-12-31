// https://leetcode.com/problems/find-eventual-safe-states/

import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

class Solution {
    private Set<Integer> visited = new HashSet<>();
    private Set<Integer> cycle = new HashSet<>();

    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < graph.length; i++) {
            if (this.dfs(i, graph)) {
                res.add(i);
            }
        }
        
        return res;
    }

    private boolean dfs(int node, int[][] graph) {
        if (this.cycle.contains(node)) return false; // Node is in the current cycle
        if (this.visited.contains(node)) return true; // Node is already determined to be safe

        this.cycle.add(node); // Mark node as being in the current DFS path
        for (int neighbor : graph[node]) { // Loop through neighbors of the node
            if (!this.dfs(neighbor, graph)) {
                return false; // Found a cycle
            }
        }
        this.cycle.remove(node); // Remove node from the current path

        this.visited.add(node); // Mark node as safe
        return true;
    }
}