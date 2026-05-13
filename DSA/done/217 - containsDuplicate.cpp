// https://leetcode.com/problems/contains-duplicate/

#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int n : nums) {
            if (seen.count(n) > 0) {
                return true;
            }
            seen.insert(n);
        }
        return false;
    }
};