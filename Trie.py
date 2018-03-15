
#An implementation of the Trie and a Node with a children property which holds subsequent letters of
#a word as nodes in the dictionary, till a leaf where the full word is stored in the data of the node

from TrieNode import *

class Trie:
    def __init__(self):
        # first node will be an empty node
        self.head = TrieNode()

    def addName(self, word):
        # starting from the head
        currentNode = self.head

        #print("Adding", word)
        # Moving through the Trie to find the last node with respect to the word
        for i in range(len(word)):
            if word[i] in currentNode.children:
                currentNode = currentNode.children[word[i]]
                #print('Existing Key:', currentNode.key)
                #rint('Existing Data:', currentNode.data)
            else:
                #print("ended at index", i, " at letter", word[i])
                currentNode.addChild(word[i])
                currentNode = currentNode.children[word[i]]
                #print("New Key:", currentNode.key)
                #print("New Data", currentNode.data)

        # the entire word is now stored at the leaf of the Trie
        currentNode.data = word
        #print("DONE!!! data is now", currentNode.data)
        #print()

    def getData(self, word):
        currentNode = self.head

        # Move down the trie to the last letter in the trie
        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]

        return currentNode.data

    #Given a name, or a string of characters, this method traverses the Trie
    #to return the node containing the last character
    def getNodeOfLastLetter(self, name):
        currentNode = self.head

        # Move through the Trie to find the last node representing the last letter of the prefix
        for i in name:
            if i in currentNode.children:
                currentNode = currentNode.children[i]
            else:
                raise ValueError('There is no name with the prefix being', i)
        return currentNode

    #A recursive implementation of finding the full names of the students in the Trie
    #The method recursively visits every node and its children to return the node which
    #has value stored in the data of the node
    def findNames(self, presentNode,name, words):
        values = presentNode.children.values()

        if presentNode.data != None:
            words.append(presentNode.data)

        for i in values:
            self.findNames(i, name, words)

    def hasName(self,word):
         
        #checking whether a word exists in the trie by looping
        currentNode = self.head
        exists = True
        #while the letters are equal to those within the trie, keep moving through the trie, 
        #until there is no match between current character and current key of dictionary
        while exists != False:
            for i in range(len(word)):
                if char in currentNode.children:
                #if current key is a match, exists is true
                    exists = True
                    currentNode = currentNode.children[i]
                #current key isnt a match, exists is False
                else: 
                    exists = False
