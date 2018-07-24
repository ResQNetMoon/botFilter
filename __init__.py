from requests import get, post
from re import sub

class telegram:
	def __init__(self, token):
		self.uri = "https://api.telegram.org/bot"+token
		self.token = token
		self.run = True
		self.timeout = 10
	def method(self, method, params):
		return get(self.uri+"/"+method, params).json()
	
	def sendMessage(self, s, chat_id, markup=""):
		return self.method("sendMessage", {'text':s, 'chat_id':chat_id, 'reply_markup':markup})
	
	def MainHandler(self, handler):
		self.handler = handler
	
	def start(self):
		new_offset = None
		while self.run:
		#	new_offset = None
			resp = get(self.uri+"/getUpdates", {'offset':new_offset, 'timeout':self.timeout}).json()
			if len(resp['result']) <= 0:
				continue
			new_offset= str(int(resp['result'][-1]['update_id'])+1)
			#print(new_offset)
			if len(resp['result']) <= 0:
				continue
			for handle in resp['result']:
				self.handler(handle)
			
			
	

class Buttons:
	def __init__(self):
		self.buttons = '{"keyboard_markup":['
	
	def add(self, text, callback_data, size=False ):
		self.buttons += '[{"text":"'+text+'", "callback_data":"'+callback_data+'"}],'
	
	def get(self):
		sdigit = sub(r"\,$", '', self.buttons)+"]"
		self.buttons = '{"keyboard_markup":['
		return sdigit
		
		
token = "token"

bot = telegram(token)