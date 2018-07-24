from __init__ import bot, Buttons
from re import sub, findall
from threading import Thread
import settings

import linker

btn = Buttons()



def noticeSpam(text, maxSymbols=70):
	print(text)
	return len(text) >= maxSymbols







def rban(uid, chid):
	print(bot.method("kickChatMember", {'chat_id':chid, 'user_id':uid}))

def rdelete(mid, chid):
	bot.method("deleteMessage", {'message_id':mid, 'chat_id':chid})

def delete(mid, chid):
	Thread(target=rdelete, args=(mid, chid,)).start()

def ban(mid, chid):
	Thread(target=rban, args=(mid, chid,)).start()


@bot.MainHandler
def main(handle):
	hAngle = """
				Чтобы использовать этого бота у него должны быть права на удаление сообщений и блокировку пользователей.

Этот бот блокирует и удаляет сообщения от подозрительных аккаунтов.
				
				"""
	try:
		ifis = 'text' in handle['message'] and not str(handle['message']['chat']['id']).startswith('-')
	except KeyError:
		print("False")
	if ifis:
		if handle['message']['text'] == '!help':
			bot.sendMessage(hAngle, handle['message']['chat']['id'])
		return False
	if 'new_chat_member' in handle['message']:
		print("member")
		member = handle['message']['new_chat_member']
		name = member['first_name']
		if 'last_name' in member:
			name += " "+member['last_name']
		if noticeSpam(name):
			delete(handle['message']['message_id'], handle['message']['chat']['id'])
			ban(member['id'], handle['message']['chat']['id'])
	else:
		if 'text' in handle['message']:
			text = handle['message']['text'].split(' ')
			if handle['message']['text'] == '!help':
				
				bot.sendMessage(hAngle, handle['message']['chat']['id'])
			elif text[0].lower() == '/config':
				bot.sendMessage("Данная команда временно отключена", handle['message']['chat']['id'])
				return False
				text.remove(text[0])
				title = text[0]
				text.remove(title)
				setting = ' '.join(text)
				settings.conf[title] = setting
				bot.sendMessage("Параметр {0} успешно установлен!".format(title), handle['message']['chat']['id'])
				settings.sets()
			else:
				
				linker.another(bot, handle)

bot.start()