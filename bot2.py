import discord
import requests
import random
TOKEN = 'XXXXXXXXXXXXXX'

client = discord.Client()

PLAY_STRINGS = [
        "Aha re amar Tansen eseche, Ganer recomendation diche",
        "Fata Dholer moton gola niye gaan shunte chaiche",
        "Chalabo Na!",
]
INTRO_STRINGS = [
        "I am Chodari. I am Father of Jesus, Mother of Allah and Stepmom of Krishna. Bow before me you Peasants. When I bite YOU BETTER GET TETANUS.",
        "I am Chodari. I was forged in hell to eat all the JAMAICAN JERK CHICKEN. Fear me if you are tasty.",
        "I am Chodari. Amon Chatbo, sara barir Burnol kom porbe.",
        "I am Chodari. I am 10% good, 20% Mindless, 30% Psyco, 40% Evil and a 100% pure unadultered BADASS (Bajee Pod)."
        ""
]

RANDOM_CHAT_STRINGS = [
        "Sex?",
        "Chal Chal apne Baap ko mat sikha",
        "Dil se bura lagta hain bhai, Please Bhai",
        "Lululalala",
        "Shut Up",
        "Y you say these things",
        "Title of your Sex Tape!",
        "Kono Kajer Na",
        "Koi Sense Hain is Baat ka",
        "Please for the Love of God! Just Shut Up!",
        "Chup MAGI",
        "Pute Debo",
        "BOT er theke chaton khache :)",
        "O Bhaaaai.....Koi maaro mujhe maaro",
        "Besi boke"
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
ABUSE_REPLIES = [
        "Esob tow chotobela e boltam",
        "The reason you are using these petty abusive Talks is because you lack the ability to insult me properly......Just Pathetic",
        "Chi Chi bot ke thik kore Insult o korte pare na",
        "Esob shune amar Kidney tey Heart Attack chole asbe",
        "Tui Bokachoda",
        "Eta atotai Pathetic je er reply o dite parbo na",
	"Tui holi bandorer bogoler chul",
	"suorer nati",
	"sala chud khankir dim",
	"kothai na boro hoye, kaaje boro hou",
	"aah, sona go amar! kosto hocche bolo?",
	"nijer mukh ta ainai dekhechis?",
	"Tui jei school e egulo sikhechis, ami sekhankar headmaster chilam"
]
'''
OFFLINE_STRINGS = [
        "Ato Baje chatlam je amay offline korar cheshta cholche......Huh! Just Pathetic",
        "Haha Lull!",
        "Ole Baba Le....bacha chelera amay offline korar cheshta korche"
]
'''
GOD_STRINGS = [
        "You can pray to your god all you want. But.....Spoiler Alert! I wont be Listening!",
        "There is no God. There is just Bot Khoiree."
]



ABUSE_WORDS = ["er chele","marani","haramzada","choda", "boka choda", "shut up", "fuck u", "fuck you", "paglachoda", "khankir chele", "kelabo", "fuck off"]
ONLINE_STRINGS = ["Ese gechi pola pan", "Kon khankir chhele dakli be?", "Sala shanti de ghumateo dei na baal gulo! keno dakli?", "Ei to maa mego, Chole esechi", "uff!! Chude chatni bekar khetni!!", "Mone poreche amai tahole?"]
OFFLINE_STRINGS = ["Ato Baje chatlam je amay offline korar cheshta cholche......Huh! Just Pathetic","Ole Baba Le....bacha chelera amay offline korar cheshta korche","Besh chole jacchi.. pore dakle asbo aar na", ":''') ok", "Accha chalta hu duao me yad rakhna", "OPOMAAN!!", "Chele chaton nite parlo na aar.. XD"]

def get_randomized_response(string_list):
        return random.choice(string_list)

def isin(msg,strings):
	flag = 0
	for s in strings:
		if s in msg:
			flag = 1
			break
	return flag
def isslang(msg,strings):
	flag = 0
	for s in strings:
		if s in msg:
			flag = s
			break
	return flag

def toogle_on_off(author, message, running):
        text = message.content.lower()

        if author in Admin_List:
                if running and message.content == "chup chodari":

                        return False, get_randomized_response(OFFLINE_STRINGS)

                if not running and message.content == "aai chodari":
                        return True, get_randomized_response(ONLINE_STRINGS)
        elif "chup chodari" in text:
                response = get_randomized_response(OFFLINE_STRINGS)
                return running, response

        return running, ''
@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return
	msg = message.content.lower()
	f = isslang(msg,['haramjada', 'bokachoda', 'khankir chhele', 'paglachoda', 'kelachoda', 'dhyamnachoda'])
	if f != 0:
		resp = '{0.author.mention}\n'.format(message)+' tui '+f
		await message.channel.send(resp)
	elif isin(msg,ABUSE_WORDS):
		resp = get_randomized_response(ABUSE_REPLIES)
		await message.channel.send(resp)
		


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
