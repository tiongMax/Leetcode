// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

class Solution {
public:
    int minScore(int n, std::vector<std::vector<int>>& roads) {
        // 1. Build the graph adjacency list
        // graph[u] stores pairs of {neighbor, distance}
        std::vector<std::vector<std::pair<int, int>>> graph(n + 1);
        for (const auto& road : roads) {
            int u{road[0]};
            int v{road[1]};
            int distance{road[2]};
            graph[u].push_back({v, distance});
            graph[v].push_back({u, distance});
        }
        
        // 2. Initialize BFS tools
        std::queue<int> q;
        std::vector<bool> visited(n + 1, false);
        int min_score{INT_MAX};
        
        // Start BFS from city 1
        q.push(1);
        visited[1] = true;
        
        // 3. Traverse the component
        while (!q.empty()) {
            int curr{q.front()};
            q.pop();
            
            for (const auto& edge : graph[curr]) {
                int neighbor{edge.first};
                int distance{edge.second};
                
                // Update the minimum score seen so far
                min_score = std::min(min_score, distance);
                
                // If we haven't been to this city, explore it
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        
        return min_score;
    }
};