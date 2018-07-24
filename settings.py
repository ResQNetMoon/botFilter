








f = open("settings/main.conf")
data=f.read().split("\n")
f.close()
textGraph = data
conf = {}
def red():
	global conf
	for event in data:
		if event.strip() == '':
			continue
		inner = event.split(": ")
		conf[inner[0]] = inner[1]
red()
def sets():
	global conf, textGraph
	newText = ""
	first = True
	for event in conf:
	#	print(event)
		if first:
			newText += event+": "+conf[event]
			first = False
		else:
			newText += "\n"+event+": "+conf[event]
	f = open("settings/main.conf", 'w+')
	f.write(newText)
	f.close()
	red()