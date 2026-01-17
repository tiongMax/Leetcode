#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <climits>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) return "";

        unordered_map<char, int> hm;
        for (char c : t) hm[c]++;

        int required = hm.size();
        int l = 0, r = 0, formed = 0;
        unordered_map<char, int> window_counts;
        int min_len = INT_MAX;
        int start_idx = 0;

        while (r < s.length()) {
            char character = s[r];
            window_counts[character]++;
            if (hm.count(character) && window_counts[character] == hm[character]) formed++;

            while (l <= r && formed == required) {
                character = s[l];
                if (r - l + 1 < min_len) {
                    min_len = r - l + 1;
                    start_idx = l;
                }

                window_counts[character]--;
                if (hm.count(character) && window_counts[character] < hm[character]) formed--;
                l++;
            }
            r++;
        }

        return min_len == INT_MAX ? "" : s.substr(start_idx, min_len);
    }
};