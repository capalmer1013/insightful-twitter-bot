import json
import readline
import bot

tweetsDict = json.load(open('./graph.json', 'r'))

a = bot.Bot()
a.loadKnowledgeGraph(tweetsDict)
print(a.outputText())