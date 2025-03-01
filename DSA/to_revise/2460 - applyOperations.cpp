// https://leetcode.com/problems/apply-operations-to-an-array/

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        // First loop: handle the merge operation
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }

        // Second loop: move non-zero elements to the front
        int l = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) {
                swap(nums[i], nums[l]);
                l++;
            }
        }

        return nums;
    }
};
