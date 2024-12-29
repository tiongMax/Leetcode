// https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        int[] hm = new int[26];
        for (int i = 0; i < order.length(); i++) {
            hm[order.charAt(i) - 'a'] = i;
        }

        for (int i = 1; i < words.length; i++) {
            String w1 = words[i - 1], w2 = words[i];
            for (int j = 0; j < w1.length(); j++) {
                if (j == w2.length()) {
                    return false;
                }
                if (w1.charAt(j) != w2.charAt(j)) {
                    if (hm[w1.charAt(j) - 'a'] > hm[w2.charAt(j) - 'a']) {
                        return false;
                    }
                    break;
                }
            }
        }

        return true;
    }
}