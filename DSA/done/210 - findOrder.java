// https://leetcode.com/problems/course-schedule-ii/

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;


class Solution {
    private Map<Integer, List<Integer>> hm = new HashMap<>();
    private Set<Integer> visited = new HashSet<>();
    private Set<Integer> cycle = new HashSet<>();

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        for (int i = 0; i < numCourses; i++) {
            this.hm.put(i, new ArrayList<>());
        }    
        for (int[] c : prerequisites) {
            this.hm.get(c[0]).add(c[1]);
        }

        int[] res = new int[numCourses];
        List<Integer> topo = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            if (!this.dfs(i, topo)) {
                return new int[0]; 
            }
        }
        for (int i = 0; i < numCourses; i++) {
            res[i] = topo.get(i);
        }
        return res;
    }

    private boolean dfs(int i, List<Integer> topo) {
        if (this.visited.contains(i)) return true;
        if (this.cycle.contains(i)) return false;

        this.cycle.add(i);
        for (int n : this.hm.get(i)) {
            if (!this.dfs(n, topo)) {
                return false;
            }
        }
        this.cycle.remove(i);

        this.visited.add(i);
        topo.add(i);
        return true;
    }
}