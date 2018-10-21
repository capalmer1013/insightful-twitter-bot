import bot
a = bot.Bot()
with open("../outfile.txt", 'r') as infile:
	for line in infile:
		a.learnText(line)
a.graph
import json
json.dump(a.graph, open("graph.json", "w"))
a.outputText()
import readline; readline.write_history_file('my_history.py')
