// https://leetcode.com/problems/valid-anagram/

#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        
        vector<int> hm(26, 0);
        for (int i{ 0 }; i < s.size(); i++) {
            hm[s[i] - 'a']++;
            hm[t[i] - 'a']--;
        }

        for (int count : hm) {
            if (count != 0) return false;
        }
        return true;
    }
};