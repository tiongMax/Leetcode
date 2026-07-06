// https://leetcode.com/problems/remove-covered-intervals

#include <vector>
#include <algorithm>

class Solution {
public:
    int removeCoveredIntervals(std::vector<std::vector<int>>& intervals) {
        // Sort: start ascending. If starts are equal, end descending.
        std::sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
            if (a[0] == b[0]) {
                return a[1] > b[1]; // Descending by end time
            }
            return a[0] < b[0];     // Ascending by start time
        });

        int max_end{0}, cnt{0};
        
        for (const auto& interval : intervals) {
            int e{interval[1]};
            if (e > max_end) {
                max_end = e;
                cnt++;
            }
        }
        
        return cnt;
    }
};