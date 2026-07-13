// https://leetcode.com/problems/sequential-digits/

#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    std::vector<int> sequentialDigits(int low, int high) {
        int min_len = std::to_string(low).length();
        // Clamp max_len to 9 because "123456789" only has 9 characters
        int max_len = std::min(9, (int)std::to_string(high).length());
        
        std::string mas_str = "123456789";
        std::vector<int> res;
        
        // Outer loop for the window sizes
        for (int i = min_len; i <= max_len; ++i) {
            int n = mas_str.length();
            
            // Cast to int to prevent unsigned underflow bugs
            for (int l = 0; l <= n - i; ++l) {
                std::string sub = mas_str.substr(l, i);
                int seq_dig = std::stoi(sub);
                
                if (seq_dig >= low && seq_dig <= high) {
                    res.push_back(seq_dig);
                }
                
                if (seq_dig > high) {
                    break;
                }
            }
        }
        
        return res;
    }
};