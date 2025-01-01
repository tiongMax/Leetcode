// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution {
    public int maxScore(String s) {
        int totalZeroes = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') totalZeroes++; 
        }

        int curZero = 0, maxScore = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i - 1) == '0') {
                curZero++;
                totalZeroes--;
            }
            maxScore = Math.max(maxScore, curZero + (s.length() - i - totalZeroes));
        }

        return maxScore;
    }
}
