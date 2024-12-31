// https://leetcode.com/problems/count-ways-to-build-good-strings/

import java.util.Map;
import java.util.HashMap;

// Memo
class Solution {
    private Map<Integer, Integer> dp = new HashMap<>();
    private static final int MOD = 1_000_000_007;

    public int countGoodStrings(int low, int high, int zero, int one) {
        return dfs(0, low, high, zero, one);
    }

    private int dfs(int i, int low, int high, int zero, int one) {
        if (i > high) return 0;
        if (dp.containsKey(i)) return dp.get(i);
    
        int res = i >= low ? 1 : 0;
        res += dfs(i + zero, low, high, zero, one);
        res %= MOD;
        res += dfs(i + one, low, high, zero, one);
        res %= MOD;

        dp.put(i, res);
        return res;
    }
}

// Dp
class Solution2 {
    public int countGoodStrings(int low, int high, int zero, int one) {
        int MOD = 1_000_000_007;
        int[] dp = new int[high + 1];

        for (int i = high; i >= 0; i--) {
            dp[i] = (i < low) ? 0 : 1;
            if (i + zero < dp.length) {
                dp[i] += dp[i + zero];
                dp[i] %= MOD;
            }
            if (i + one < dp.length) {
                dp[i] += dp[i + one];
                dp[i] %= MOD;
            }
        }

        return dp[0];
    }
}