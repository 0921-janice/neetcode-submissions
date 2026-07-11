from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashT = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for l in word:
                count[ord(l) - ord('a')] += 1

            hashT[tuple(count)].append(word)

        return list(hashT.values())
            
        