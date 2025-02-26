// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

#include <bits/stdc++.h>
using namespace std;

class Solution {
    public:
        int maxAbsoluteSum(vector<int>& nums) {
            int res(0), maxPref(0), minPref(0), curSum(0);
            for (int n : nums) {
                curSum += n;
                res = max(res, max(abs(curSum - maxPref), abs(curSum - minPref)));
                maxPref = max(maxPref, curSum);
                minPref = min(minPref, curSum);
            }   
            return res;
        }
};