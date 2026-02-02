// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

#include <vector>

using namespace std;

class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int small{51}, small2{51};
        for (int i{1}; i < nums.size(); i++) {
            if (nums[i] < small) {
                small2 = small;
                small = nums[i];
            } else if (nums[i] < small2) {
                small2 = nums[i];
            }
        }
        return nums[0] + small + small2;
    }
};