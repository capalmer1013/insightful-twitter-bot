import random

start = "<START>"
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

            prev = word

        if prev not in self.graph:
            self.graph[prev] = {}

        if end not in self.graph[prev]:
            self.graph[prev][end] = 1

        else:
            self.graph[prev][end] += 1

    def outputText(self, charLen=None):
        outStr = ""
        nextState = start
        while nextState != end:
            selection = self.listOfOccurances(nextState)
            nextState = random.choice(selection)
            if nextState != end:
                outStr += nextState + " "

        return outStr

    def getKnowledgeGraph(self):
        return self.graph

    def loadKnowledgeGraph(self, knowledgeDict):
        self.graph = knowledgeDict

    def listOfOccurances(self, index):
        value = []
        for each in self.graph[index]:
            value.extend([each]*self.graph[index][each])

        return value
