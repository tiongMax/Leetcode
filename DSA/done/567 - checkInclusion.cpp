#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;

        vector<int> target(26, 0);
        for (char c : s1) target[c - 'a']++;

        vector<int> window(26, 0);
        int l = 0, r = 0, required = 0, formed = 0;;
        
        int uniqueChars = 0;
        for (int count : target) if(count > 0) uniqueChars++; 

        while (r < s2.length()) {
            char curr = s2[r];
            int idx = curr - 'a';
            window[idx]++;
            if (target[idx] > 0 && window[idx] == target[idx]) formed++;
            
            if (r - l + 1 > s1.length()) {
                char leftChar = s2[l];
                int leftIdx = leftChar - 'a';
                if (target[leftIdx] > 0 && window[leftIdx] == target[leftIdx]) formed--;
                
                window[leftIdx]--;
                l++;
            }

            if (formed == uniqueChars) return true;
            r++;
        }
        return false;
    }
};