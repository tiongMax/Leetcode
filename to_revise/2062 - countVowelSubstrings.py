# https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        hm = {v: 0 for v in vowels}
        l = count = matching = 0
        last_consonant = -1

        for r in range(len(word)):
            if word[r] in vowels:
                if hm[word[r]] == 1:
                    matching += 1
                hm[word[r]] += 1
                while matching == 5:
                    hm[word[l]] -= 1
                    if hm[word[l]] == 0:
                        matching -= 1
                    l += 1
                # After the while loop, l to r (inclusive) will not be a valid substring
                # but l - 1 will be the last valid substring, so the count will be 
                # (l + 1 - 1) - (last + 1) = 
                count += l - last_consonant - 1
            else:
                hm = {v: 0 for v in vowels}
                matching = 0
                last_consonant = r
                l = r + 1

        return count