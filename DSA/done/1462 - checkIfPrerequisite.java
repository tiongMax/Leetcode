// https://leetcode.com/problems/course-schedule-iv/submissions/1297670987/

import java.util.Set;
import java.util.Map;
import java.util.List;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;

class Solution {
    private Map<Integer, Set<Integer>> visited = new HashMap<>();
    private Map<Integer, List<Integer>> graph = new HashMap<>();

    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] prerequisite : prerequisites) {
            int a = prerequisite[0];
            int b = prerequisite[1];
            graph.get(b).add(a); 
        }

        for (int c = 0; c < numCourses; c++) {
            if (!visited.containsKey(c)) {
                dfs(c);
            }
        }

        List<Boolean> result = new ArrayList<>();
        for (int[] query : queries) {
            int s = query[0];
            int d = query[1];
            result.add(visited.get(d).contains(s));
        }

        return result;
    }

    private Set<Integer> dfs(int node) {
        if (visited.containsKey(node)) {
            return visited.get(node);
        }

        Set<Integer> prereq = new HashSet<>();
        for (int neighbor : graph.get(node)) {
            prereq.add(neighbor);
            prereq.addAll(dfs(neighbor));
        }

        visited.put(node, prereq);
        return prereq;
    }
}
