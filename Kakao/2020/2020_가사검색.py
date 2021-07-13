class Trie:
    def __init__(self):
        self.child = dict()
        self.count = 0

    def insert(self, str):
        curr = self
        for ch in str:
            curr.count += 1
            if ch not in curr.child:
                curr.child[ch] = Trie()
            
            curr = curr.child[ch]
        curr.count += 1

    def search(self, str):
        curr = self
        for ch in str:
            if ch == '?':
                return curr.count
            if ch not in curr.child:
                return 0
            curr = curr.child[ch]
        return curr.count

def solution(words, queries):
    TrieRoot = [Trie() for _ in range(10000)]
    ReTrieRoot = [Trie() for _ in range(10000)]
    answer = []

    for str in words:
        TrieRoot[len(str) - 1].insert(str)
        ReTrieRoot[len(str) - 1].insert(str[::-1])
    
    for str in queries:
        if str[0] != '?':
            answer.append(TrieRoot[len(str) - 1].search(str))
        else:
            answer.append(ReTrieRoot[len(str) - 1].search(str[::-1]))
        
    return answer
