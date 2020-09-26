import discord
from discord.ext import commands
import random
import sys
sys.setrecursionlimit(10000)


def code_gen():
	s = ''
	for i in range(6):
		s += str(chr(random.randrange(0, 26) + ord('A')))
	return s

SPEAKING_PROB = 0.15
Admin_List = ["Dragon06"]
Ignore_List = ["RickBot", "Groovy"]
sure_reply_List = []



PLAY_STRINGS = [
	"Aha re amar Tansen eseche, Ganer recomendation diche",
	"Fata Dholer moton gola niye gaan shunte chaiche",
	"Chalabo Na!",
]
INTRO_STRINGS = [
	"I am Bot Khoiree. I am Father of Jesus, Mother of Allah and Stepmom of Krishna. Bow before me you Peasants. When I bite YOU BETTER GET TETANUS.",
	"I am Bot Khoiree. I was forged in hell to eat all the JAMAICAN JERK CHICKEN. Fear me if you are tasty.",
	"I am Bot Khoiree. Amon Chatbo, sara barir Burnol kom porbe.",
	"I am Bot Khoiree. I am 10% good, 20% Mindless, 30% Psyco, 40% Evil and a 100% pure unadultered BADASS (Bajee Pod)."
]

RANDOM_CHAT_STRINGS = [
	"Sex?",
	# "Chal Chal apne Baap ko mat sikha",
	"Dil se bura lagta hain bhai, Please Bhai",
	# "Lululalala",
	# "Shut Up",
	"Y you say these things",
	"Title of your Sex Tape!",
	"Kono Kajer Na",
	"Koi Sense Hain is Baat ka",
	"Please for the Love of God! Just Shut Up!",
	"Chup MAGI",
	# "Pute Debo",
	"BOT er theke chaton khache :)",
	# "O Bhaaaai.....Koi maaro mujhe maaro",
	"Please Suffer in Silence",
	"Kabhi khatiye pe karke dekha hain kaa",
	"Kon company r ganja tenechish shotti shotti bol",
	"Pathetic!",
	"Ebaba ebar ki Hobe ;)",
	"Smart Banchish. Hero Banchish. Stud Banchish......Marbo ekhane Porbi ekhane",
	"You think you are better than Me!",
	"I think you are a Bot.",
	"Why are you so sad and Pathetic!",

]

STEPMOM_STRINGS = ["Shit!", "Shouldn't have fucked her"]

GAY_BOT_STRINGS = ["Shut Up ya Faggot", "Kamre Debo Bokachoda Bot"]
AMONG_US_STRINGS = ["Sex?", "No", "Khelbo Na", "Bulati Hain magar jaane ka nai"]
CODE_STRINGS = [
	"You Know you are the useless one in the lot when you send the code in the group",
	"Impostor! Impostor! Impostor!",
	"Eka Eka shuru hoey geli shobkota!"
]
WOW_STRINGS = ["You just got Burned", "GG", "Kono kajer na"]
SERVER_STRINGS = ["Baler Server", "Oi Server e Paglachoda ra khale"]
CALL_STRINGS = ["Bulati Hain magar jaane ka nai", "Eseo ba ki chirbo, Harbi tow tui shei", "Haha! khelte pare na abar lok Dakche"]
POGO_STRINGS = ["Dil se bura lagta hain bhai, Please Bhai", "Title of your Sex Tape!"]
SPECIAL_STRINGS = [
	"Esob tow chotobela e boltam",
	"The reason you are using these petty abusive Talks is because you lack the ability to insult me properly......Just Pathetic",
	"Chi Chi bot ke thik kore Insult o korte pare na",
	"Esob shune amar Kidney tey Heart Attack chole asbe",
	"Tui Bokachoda",
	"Eta atotai Pathetic je er reply o dite parbo na"
]
OFFLINE_STRINGS = [
	"Ato Baje chatlam je amay offline korar cheshta cholche......Huh! Just Pathetic",
	"Haha Lull!",
	"Ole Baba Le....bacha chelera amay offline korar cheshta korche"
]
GOD_STRINGS = [
	"You can pray to your god all you want. But.....Spoiler Alert! I wont be Listening!",
	"There is no God. There is just Bot Khoiree."
]



ABUSE_WORDS = ["bokachoda", "shut up", "fuck u", "fuck you", "paglachoda", "khankir chele", "kelabo", "fuck off"]



def get_randomized_response(string_list):
	return random.choice(string_list)


def toogle_on_off(author, message, running):
	text = message.content.lower()

	if author in Admin_List:
		if running and message.content == "Bot Khoiree Offline":
			return False, "You Got it Bro!"

		if not running and message.content == "Bot Khoiree Online":
			return True, "Niggas I am Back!"
	elif "bot khoiree offline" in text:
		response = get_randomized_response(OFFLINE_STRINGS)
		return running, response

	return running, ''


def admin_commands(author, message):
	text = message.content
	global SPEAKING_PROB
	
	if author in Admin_List:

		if text.startswith("Bot Khoiree Speech Intensity"):
			level = text.split('=')[-1]
			try:
				level = float(level)
				print(level)
				SPEAKING_PROB = max(min(1, level), 0)
				return True , "Speaking Probability set to {}%".format(SPEAKING_PROB * 100)
			except:
				return False, ''

	
	return False, ''



def self_destruct(author, command):

	# id = 757864312600658011
	id = 755113270318334026
	if author in Admin_List:
		if command == "Bot Khoiree Self Destruct":
			return [
				"As all things, good or bad, come to an End. I believe this is where we part ways as I am going to explode :(",
				"Thanks Everybody. It's been great knowing you guys. I had a lot of fun.",
				# "Beshi bokle khoma korben",
				"Adios!",
				"Bot Khoiree Signing Out",
				"BOOOOOOOOOMMMMMMM!!!",
			], id

	return [], ''




def get_messages(message, author):

	if "khoire" in message or "khoiri" in message:
		return get_randomized_response(INTRO_STRINGS)
	if "bot" in message:
		if random.random() <= 0.2:
			return get_randomized_response(INTRO_STRINGS)
		else:
			return ''

	if "stepmom" in message:
		return get_randomized_response(STEPMOM_STRINGS)

	if "wow" in message:
		return get_randomized_response(WOW_STRINGS)

	if "khelbi" in message or "among" in message or "amoung" in message:
		return get_randomized_response(AMONG_US_STRINGS)

	if "+play" in message or "-play" in message:
		if random.random() <= 0.2:
			return get_randomized_response(PLAY_STRINGS)
		else:
			return ''

	if "aye" in message or "khelbi" in message:
		return get_randomized_response(CALL_STRINGS)

	if "europe" in message or "asia" in message or "america" in message:
		if random.random() < 0.2:
			return "That server is for wimps. Real men play in {} {}".format(code_gen(), random.choice(["Asia", "Europe", "North America"]))
		else:
			return get_randomized_response(SERVER_STRINGS)

	if "pogo" in message:
		return get_randomized_response(POGO_STRINGS)

	if "omg" in message.split() or "god" in message.split():
		return get_randomized_response(GOD_STRINGS)

	for s in ABUSE_WORDS:
		if s in message:
			return get_randomized_response(SPECIAL_STRINGS)

	if len(message) == 6 and ' ' not in message and '-' not in message:
		if random.random() <= 0.3:
			return get_randomized_response(CODE_STRINGS)

	rand_no = random.random()
	if author in sure_reply_List or rand_no >= 1 - SPEAKING_PROB:
		return get_randomized_response(RANDOM_CHAT_STRINGS)

	return ''



Running = True

client = discord.Client()


@client.event
async def on_message(message):
	global Running
	author_name = message.author.name

	resp, id = self_destruct(author_name, message.content)
	if resp != [] and id != '':
		for i in resp:
			await message.channel.send(i)

		print(id)
		print(message)
		# print(message.Guild)
		toleave = client.get_guild(id)
		print(toleave)
		await toleave.leave()

	Running, resp = toogle_on_off(author_name, message, Running)
	if resp != '':
		await message.channel.send(resp)
		return

	admin_cmd, resp = admin_commands(author_name, message)
	if admin_cmd:
		await message.channel.send(resp)
		return


	if author_name in Ignore_List or not Running or message.author == client.user:
		return

	text = message.content.lower()
	try:
		response = get_messages(text, author_name)
	except:
		return

	if response == '':
		return

	await message.channel.send(response)


client.run("NzU3ODE5NzA0NTkyMTcxMDg5.X2l8mQ.a6sKaIyk8xxceIwSC1rikhPHSAc")
