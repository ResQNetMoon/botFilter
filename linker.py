from os import listdir
from re import sub
import __init__ as pytg
from os.path import isfild
def loadPlugins():
	arr=listdir("plug")
	
	for i in arr:
		if not isfile("plug/"+i):
			continue
		name = sub("\..*$", "", i)
		yield {'moduleName':name, 'module':__import__("plug."+name)}

def another(bot, handle):
	pass