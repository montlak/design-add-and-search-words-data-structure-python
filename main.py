class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.structure = []
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.structure.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        result = False
        if word in self.structure or word == ".":
            result = True
        else:
            for item in self.structure:
                if len(word) == len(item):
                    for i in range(len(word)):
                        if word[i] != ".":
                            if word[i] == item[i]:
                                result = True
                            else:
                                result = False
                                break
                if result:
                    break
        return result
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
