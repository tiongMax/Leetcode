// https://leetcode.com/problems/two-sum/

#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hm;
        for (int i{0}; i < nums.size(); i++) {
            int complement{target - nums[i]};
            if (hm.find(complement) != hm.end()) {
                return {hm[complement], i};
            }
            hm[nums[i]] = i;
        }
        return {};
    }
};