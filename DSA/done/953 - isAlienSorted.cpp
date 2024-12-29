// https://leetcode.com/problems/verifying-an-alien-dictionary/

#include <string>
#include <vector>

using namespace std;
 
class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        int orderIndex[26] = {0};
        for (int i = 0; i < order.size(); ++i)
            orderIndex[order[i] - 'a'] = i;
        
        for (int i = 1; i < words.size(); i++) {
            string w1 = words[i - 1], w2 = words[i];
            for (int j = 0; j < w1.size(); j++) {
                if (j == w2.size()) 
                    return false;
                if (w1[j] != w2[j]) {
                    if (orderIndex[w1[j] - 'a'] > orderIndex[w2[j] - 'a'])
                        return false;
                    break;
                }
            }
        }

        return true;
    }
};