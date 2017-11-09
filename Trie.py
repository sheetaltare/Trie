class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pointerDict = [None] * 26
        self.isWord = False 
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        currentNode = self
        for c in word:
            if currentNode.pointerDict[ord(c) - ord('a')] == None:
                newNode = Trie()
                currentNode.pointerDict[ord(c) - ord('a')] = newNode
            currentNode = currentNode.pointerDict[ord(c) - ord('a')]
        currentNode.isWord = True 
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        currentNode = self
        for c in word:
            if currentNode.pointerDict[ord(c) - ord('a')] == None:
                return False
            currentNode = currentNode.pointerDict[ord(c) - ord('a')]
        return currentNode.isWord   
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        currentNode = self
        for c in prefix:
            if currentNode.pointerDict[ord(c) - ord('a')] == None:
                return False
            currentNode = currentNode.pointerDict[ord(c) - ord('a')]
        return True    
