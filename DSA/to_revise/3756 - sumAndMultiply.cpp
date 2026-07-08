// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        long long MOD = 1e9 + 7;
        int n = s.length();
        
        // 1. Initialize our padded prefix arrays
        // Using long long to prevent integer overflow during multiplication
        vector<long long> prefix_sum(n + 1, 0);
        vector<long long> prefix_val(n + 1, 0);
        vector<int> prefix_nonzero(n + 1, 0);
        
        // Precompute powers of 10 modulo MOD
        vector<long long> pow10(n + 1, 1);
        for (int i{1}; i <= n; i++) {
            pow10[i] = (pow10[i - 1] * 10) % MOD;
        }
        
        // 2. Build the prefix arrays
        for (int i = 0; i < n; i++) {
            long long digit{s[i] - '0'}; // Convert char to integer
            
            // Standard prefix sum is always updated
            prefix_sum[i + 1] = prefix_sum[i] + digit;
            
            // CRITICAL FIX: Only shift and add to the value if the digit is NOT zero
            if (digit != 0) {
                prefix_val[i + 1] = (prefix_val[i] * 10 + digit) % MOD;
                prefix_nonzero[i + 1] = prefix_nonzero[i] + 1;
            } else {
                // If it's zero, carry forward the previous state
                prefix_val[i + 1] = prefix_val[i];
                prefix_nonzero[i + 1] = prefix_nonzero[i];
            }
        }
        
        vector<int> results;
        results.reserve(queries.size()); // Small optimization to avoid reallocations
        
        // 3. Process each query
        for (const auto& q : queries) {
            int L{q[0]}, R{q[1] + 1};
            
            // Sum of the digits in the range
            long long current_sum{prefix_sum[R] - prefix_sum[L]};
            
            // Find exactly how many non-zero digits are in this specific range
            int count{prefix_nonzero[R] - prefix_nonzero[L]};
            
            // Isolate the concatenated value and safely handle modulo for negatives in C++
            long long sub_val{(prefix_val[L] * pow10[count]) % MOD};
            long long current_val{(prefix_val[R] - sub_val + MOD) % MOD};
            
            // Multiply them together as intended
            long long ans{(current_sum * current_val) % MOD};
            results.push_back(static_cast<int>(ans));
        }
        
        return results;
    }
};