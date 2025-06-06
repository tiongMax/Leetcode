// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

import java.util.Arrays;

class Solution {
    public void dfs(int node, int[] edges, int[] dist, boolean[] visit) {
        visit[node] = true;
        int neighbor = edges[node];
        if (neighbor != -1 && !visit[neighbor]) {
            dist[neighbor] = 1 + dist[node];
            dfs(neighbor, edges, dist, visit);
        }
    }

    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int n = edges.length;
        int[] dist1 = new int[n], dist2 = new int[n];
        Arrays.fill(dist1, Integer.MAX_VALUE);
        Arrays.fill(dist2, Integer.MAX_VALUE);
        dist1[node1] = 0;
        dist2[node2] = 0;

        boolean[] visit1 = new boolean[n], visit2 = new boolean[n];
        Arrays.fill(visit1, false);
        Arrays.fill(visit2, false);

        dfs(node1, edges, dist1, visit1);
        dfs(node2, edges, dist2, visit2);

        int minDistNode = -1, minDistTillNow = Integer.MAX_VALUE;
        for (int currNode = 0; currNode < n; currNode++) {
            if (minDistTillNow > Math.max(dist1[currNode], dist2[currNode])) {
                minDistNode = currNode;
                minDistTillNow = Math.max(dist1[currNode], dist2[currNode]);
            }
        }
        return minDistNode;
    }
}