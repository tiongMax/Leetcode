// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

#include <vector>
using namespace std;

class Solution {
    public:
        int numOfSubarrays(vector<int>& arr) {
            int curSum(0), odd(0), even(0), res(0);
            const int MOD = 1e9 + 7;
    
            for (auto n : arr) {
                curSum += n;
                if (curSum % 2) {
                    res = (res + 1 + even) % MOD;
                    odd++;
                } else {
                    res = (res + odd) % MOD;
                    even++;
                }
            }
    
            return res;
        }
    };