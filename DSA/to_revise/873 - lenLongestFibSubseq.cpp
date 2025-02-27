// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

#include <bits/stdc++.h>
using namespace std;

class Solution {
    public:
        int lenLongestFibSubseq(vector<int>& arr) {
            unordered_map<int, int> arr_map;  // Map of elements to their indices
            int res = 0;
            int n = arr.size();
            
            // Create a DP table (2D vector) initialized to 0
            vector<vector<int>> dp(n, vector<int>(n, 0));
    
            // Fill the map with the indices of elements in arr
            for (int i = 0; i < n; ++i) {
                arr_map[arr[i]] = i;
            }
    
            // Iterate in reverse to find Fibonacci subsequences
            for (int i = n - 2; i >= 0; --i) {
                for (int j = n - 1; j > i; --j) {
                    int prev = arr[i], cur = arr[j];
                    int nxt = prev + cur;
                    int length = 2;  // Starting length for Fibonacci sequence (two elements)
    
                    // Check if the next Fibonacci number exists in the array
                    if (arr_map.find(nxt) != arr_map.end()) {
                        int k = arr_map[nxt];  // Get the index of the next number in the sequence
                        length = 1 + dp[j][k];  // Update the length of the subsequence
                        res = max(res, length);  // Track the maximum length
                    }
    
                    dp[i][j] = length;  // Store the length in the DP table
                }
            }
    
            return res;  // Return the result
        }
    };