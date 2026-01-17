// https://leetcode.com/problems/sliding-window-maximum/

#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> d; 
        vector<int> res;

        for (int r = 0; r < nums.size(); r++) {
            if (r >= k && d.front() == nums[r - k]) d.pop_front();

            while (!d.empty() && d.back() < nums[r]) d.pop_back();

            d.push_back(nums[r]);

            if (r >= k - 1) res.push_back(d.front());
        }
        return res;
    }
};