class Trie:

    def __init__(self):
        self.T = {}

    def insert(self, word: str) -> None:
        curr = self.T
        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr["\0"] = None

    def search(self, word: str) -> bool:
        curr = self.T
        for i in word:
            if i not in curr:
                return False
            curr = curr[i]
        if "\0" in curr:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.T
        curr = self.T
        for i in prefix:
            if i not in curr:
                return False
            curr = curr[i]
        return True  
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)