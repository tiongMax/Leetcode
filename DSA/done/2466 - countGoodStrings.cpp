// https://leetcode.com/problems/count-ways-to-build-good-strings/

#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Memo
class Solution {
public:
    const int MOD = 1'000'000'007;

    int dfs(int i, int low, int high, int zero, int one, unordered_map<int, int>& memo) {
        // Base case: if i exceeds `high`, no valid strings
        if (i > high) return 0;

        // If already calculated, return the memoized result
        if (memo.find(i) != memo.end()) {
            return memo[i];
        }

        // Initialize the result
        int res = 0;

        // If `i` is within the valid range, count it
        if (i >= low) {
            res += 1;
        }

        // Add results for adding `zero` and `one`
        res += dfs(i + zero, low, high, zero, one, memo);
        res %= MOD;
        res += dfs(i + one, low, high, zero, one, memo);
        res %= MOD;

        // Store result in memo
        memo[i] = res;
        return res;
    }

    int countGoodStrings(int low, int high, int zero, int one) {
        unordered_map<int, int> memo;
        return dfs(0, low, high, zero, one, memo);
    }
};

// Dp
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        const int MOD = 1'000'000'007;

        // Initialize dp array with size high + max(zero, one) + 1
        int maxSize = high + max(zero, one) + 1;
        vector<int> dp(maxSize, 0);

        // Reverse iteration from high to 0
        for (int i = high; i >= 0; i--) {
            // If i >= low, initialize to 1, otherwise 0
            dp[i] = (i < low) ? 0 : 1;

            // Add values from dp[i + zero] and dp[i + one], if within bounds
            if (i + zero < maxSize) {
                dp[i] += dp[i + zero];
                dp[i] %= MOD;
            }
            if (i + one < maxSize) {
                dp[i] += dp[i + one];
                dp[i] %= MOD;
            }
        }

        // Return result at dp[0]
        return dp[0];
    }
};