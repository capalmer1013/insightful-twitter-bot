import random

start= "<START>"
end = "<END>"


class Bot(object):
    def __init__(self):
        self.graph = {start: {}, end: None}

    def learnText(self, inputText):
        listOfWords = inputText.split()
        prev = start
        for word in listOfWords:
            if prev in self.graph:
                if word in self.graph[prev]:
                    self.graph[prev][word] += 1

                else:
                    self.graph[prev][word] = 1

            else:
                self.graph[prev] = {}
                self.graph[prev][word] = 1


    def outputText(self, charLen=None):
        outStr = ""
        nextState = start
        while nextState != end:
            selection = []
        pass

    def getKnowledgeGraph(self):
        return self.graph

    def loadKnowledgeGraph(self, knowledgeDict):
        pass
