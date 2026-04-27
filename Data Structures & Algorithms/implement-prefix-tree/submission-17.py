class PrefixTree:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


    def insert(self, word):
        cur = self 
        for c in word:
            if c not in cur.children:
                cur.children[c] = PrefixTree()
            cur = cur.children[c]
        cur.isEndOfWord = True

    def search(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEndOfWord
    

    def startsWith(self, prefix):
        cur = self 
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
