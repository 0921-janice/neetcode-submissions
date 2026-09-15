class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        

        nei = collections.defaultdict(list)

        if beginWord not in wordList:
            wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                nei[pattern].append(word)

        res = 1
        visited = set([beginWord])
        queue = collections.deque([beginWord])

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            queue.append(neiWord)
                            visited.add(neiWord)
            res += 1

        return 0


