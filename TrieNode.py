#A node class implemented to be used in the Trie Data Structure
#The node has instance of key which will hold the alphabets of words
#The Trie node also has an instance variable Data which is always None
#unless the node is the leaf of the Trie

class TrieNode:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.children = {}

    def addChild(self, key, data=None):
        if key in self.children:
            subDic = self.children[key].children
            subDic[key] = TrieNode(key, data)
        else:
            self.children[key] = TrieNode(key, data)

    def childrenSize(self):
        return len(self.children)

    def childrenPresent(self):
        return self.children

    def dataPresent(self):
        return self.data

    def keyPresent(self):
        return self.key

