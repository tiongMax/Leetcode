// # https://leetcode.com/problems/sort-colors/

#include <vector>

class Solution {
public:
    void sortColors(std::vector<int>& nums) {
        int zero { 0 }, i { 0 };
        int two = nums.size() - 1;

        while (i <= two) {
            if (nums[i] == 0) {
                int temp = nums[i];
                nums[i] = nums[zero];
                nums[zero] = temp;
                zero++;
                i++;
            } else if (nums[i] == 2) {
                int temp = nums[i];
                nums[i] = nums[two];
                nums[two] = temp;
                two--;
            } else {
                i++;
            }
        }
    }
};