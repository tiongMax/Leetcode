// https://leetcode.com/problems/trionic-array-i/

#include <vector>

using namespace std;

class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();
        int i{0};

        while (i < n && nums[i - 1] < nums[i]) i++;
        int p{i - 1};

        while (i < n && nums[i - 1] > nums[i]) i++;
        int q{i - 1};

        while (i < n && nums[i - 1] < nums[i]) i++;
        int flag{i - 1};

        return (p != 0) && (p != q) && (flag == n - 1 && flag != q);        
    }
};