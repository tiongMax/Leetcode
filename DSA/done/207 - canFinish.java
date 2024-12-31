// https://leetcode.com/problems/course-schedule/

import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;

class Solution {
    private Map<Integer, List<Integer>> hm = new HashMap<>();
    private Set<Integer> visited = new HashSet<>();
    private Set<Integer> cycle = new HashSet<>();

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for (int i = 0; i < numCourses; i++) {
            this.hm.put(i, new ArrayList<>());
        }
        for (int[] c : prerequisites) {
            this.hm.get(c[1]).add(c[0]);
        }

        for (int i = 0; i < numCourses; i++) {
            if (!this.dfs(i)) return false;
        }

        return true;
    }

    private boolean dfs(int i) {
        if (this.visited.contains(i)) return true;
        if (this.cycle.contains(i)) return false;

        this.cycle.add(i);
        for (int n : this.hm.get(i)) {
            if (!this.dfs(n)) return false;
        }
        this.cycle.remove(i);

        this.visited.add(i);
        return true;
    }
}