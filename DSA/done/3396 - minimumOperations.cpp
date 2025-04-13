// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

#include <bits/stdc++.h>
using namespace std;

class Solution {
    public:
        int minimumOperations(vector<int>& nums) {
            vector<bool> seen(101);
            for (int i = nums.size() - 1; i > -1; i--) {
                if (seen[nums[i]]) {
                    return i / 3 + 1;
                }
                seen[nums[i]] = true;
            }
            return 0;
        }
    };