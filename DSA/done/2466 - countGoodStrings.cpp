// https://leetcode.com/problems/count-ways-to-build-good-strings/

#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Memo
class Solution {
public:
    const int MOD = 1'000'000'007;
    unordered_map<int, int> memo;

    int dfs(int i, int low, int high, int zero, int one) {
        if (i > high) return 0;
        if (memo.find(i) != memo.end()) return memo[i];

        int res = (i >= low) ? 1 : 0;
        res += dfs(i + zero, low, high, zero, one);
        res %= MOD;
        res += dfs(i + one, low, high, zero, one);
        res %= MOD;

        memo[i] = res;
        return res;
    }

    int countGoodStrings(int low, int high, int zero, int one) {
        return dfs(0, low, high, zero, one);
    }
};

// Dp
class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        const int MOD = 1'000'000'007;
        int maxSize = high + max(zero, one) + 1;
        vector<int> dp(maxSize, 0);

        for (int i = high; i >= 0; i--) {
            dp[i] = (i < low) ? 0 : 1;
            if (i + zero < maxSize) {
                dp[i] += dp[i + zero];
                dp[i] %= MOD;
            }
            if (i + one < maxSize) {
                dp[i] += dp[i + one];
                dp[i] %= MOD;
            }
        }

        return dp[0];
    }
};