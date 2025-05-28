// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int[] maxTargetNodes(int[][] edges1, int[][] edges2, int k) {
        Map<Integer, List<Integer>> adj1 = buildAdj(edges1);
        Map<Integer, List<Integer>> adj2 = buildAdj(edges2);

        int m = edges2.length + 1;
        int n = edges1.length + 1;
        int max2 = 0;

        for (int i = 0; i < m; i++) {
            Set<Integer> visited = new HashSet<>();
            max2 = Math.max(max2, dfs(i, k - 1, adj2, visited));
        }

        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            Set<Integer> visited = new HashSet<>();
            res[i] = dfs(i, k, adj1, visited) + max2;
        }

        return res;
    }

    private Map<Integer, List<Integer>> buildAdj(int[][] edges) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int[] edge : edges) {
            adj.computeIfAbsent(edge[0], x -> new ArrayList<>()).add(edge[1]);
            adj.computeIfAbsent(edge[1], x -> new ArrayList<>()).add(edge[0]);
        }
        return adj;
    }

    private int dfs(int node, int depth, Map<Integer, List<Integer>> adj, Set<Integer> visited) {
        if (depth < 0) return 0;
        visited.add(node);
        int count = 1;
        for (int neighbor : adj.get(node)) {
            if (!visited.contains(neighbor)) {
                count += dfs(neighbor, depth - 1, adj, visited);
            }
        }
        return count;
    }
}
