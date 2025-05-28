// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        unordered_map<int, vector<int>> adj1 { buildAdj(edges1) };
        unordered_map<int, vector<int>> adj2 { buildAdj(edges2) };

        int n = edges1.size() + 1;
        int m = edges2.size() + 1;
        int max2 { 0 } ;

        for (int i { 0 }; i < m; ++i) {
            unordered_set<int> visited {};
            max2 = max(max2, dfs(i, k - 1, adj2, visited));
        }

        vector<int> res {};
        for (int i { 0 }; i < n; ++i) {
            unordered_set<int> visited {};
            int cnt { dfs(i, k, adj1, visited) };
            res.push_back(cnt + max2);
        }

        return res;
    }

private:
    unordered_map<int, vector<int>> buildAdj(const vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> adj {};
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        return adj;
    }

    int dfs(int node, int depth, unordered_map<int, vector<int>>& adj, unordered_set<int>& visited) {
        if (depth < 0) return 0;
        visited.insert(node);
        int count { 1 };
        for (int neighbor : adj[node]) {
            if (!visited.count(neighbor)) {
                count += dfs(neighbor, depth - 1, adj, visited);
            }
        }
        return count;
    }
};
