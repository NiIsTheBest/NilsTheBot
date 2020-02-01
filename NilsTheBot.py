import discord
import asyncio
import time
from random import randint
# Above this line is importing stuff

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as: " + client.user.name)
    print("ID: " + client.user.id)
    print('------')

# Below this, you can customize the bot.

moderation = 0
mode = 1
whyping = ["0Ihai6i","OrOHLxo", "fqeCLxl", "alrElmt"]
imgur = "https://imgur.com/"

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    letters = 0
    caps = 0
    captest = 0
    for i in range(len(message.content)):
        if message.content[captest].isalpha():
            letters = letters + 1
            if message.content[captest].isupper():
                caps = caps + 1
        captest = captest + 1
    if letters == caps and letters > 10 and moderation == 1:
        if mode == 1:
            await client.send_message(message.channel, "Y U USIN' ALL CAPS??")
        elif mode == 2:
            await client.send_message(message.author, "Hey there, please don't use full caps in your messages.")
    if "@everyone" in message.content and moderation == 1:
        await client.send_message(message.channel, imgur + whyping[randint(1,(len(whyping) - 1))])
# The above tests if the message sent above is all in caps. If it is, it'll send a warning to the user.
    elif message.content == "ntb!help":
        await client.send_message(message.channel,"\
Here's a list of commands:\
\n ntb!help - provides you a list of commands.\
\n ntb!info - tells you more about me and how to communicate with me.\
\n ntb!mod\
\n     [on/off] - enables or disables moderation (mode 1 by default)\
\n     [1/2] - sets mode\
\n ----------\
\n !C-to-F and !F-to-C - converts Celsius to Fahrenheit, and vice-versa.\
\n !huge - displays huge text.\
\n !hype - provides you something in DMs to copy/paste into whatever channel you like :smirk:\
")
    elif message.content == "ntb!info":
        await client.send_message(message.channel, "Hi! :wave: I'm a bot created by @NilsTheBest. Please put an exclamation mark to make me execute something (like '!info'). Type !help for a list of commands I can execute for now. Also keep in mind that **I'm still being programmed** and am far from being done! :smirk:")
    elif message.content[0:7] == "ntb!mod":
        if len(message.content) > 7:
            if message.content[8:] == "on":
                if moderation == 0:
                    mode = 1
                    await client.send_message(message.channel, ":white_check_mark: Moderation mode enabled! (mode 1)")
                    moderation = 1
                elif moderation == 1:
                    await client.send_message(message.channel, ":star: Moderation mode is already on. (mode " + str(mode) + ")")
            elif message.content[8:] == "off":
                if moderation == 0:
                    await client.send_message(message.channel, ":star: Moderation mode is already off.")
                elif moderation == 1:
                    moderation = 0
                    mode = 0
                    await client.send_message(message.channel, ":x: Moderation mode disabled!")
            elif message.content[8] == "1" or message.content[8] == "2":
                mode = int(message.content[8])
                if moderation == 0:
                    await client.send_message(message.channel, ":white_check_mark: Moderation mode enabled! \n Moderation mode successfully set to" + str(mode) + ".")
                    moderation = 1
                elif moderation == 1:
                    await client.send_message(message.channel, ":white_check_mark: moderation mode is currently enabled. (mode " + str(mode) + ")")
    elif message.content[0:5] == "!huge": # The "!huge" command displays huge text by using the "regional indicator" emoji.
        if len(message.content) == 5:
            await client.send_message(message.channel, "Please type something after '!huge '.")
        elif len(message.content) <= 8 or len(message.content) >= 23:
            await client.send_message(message.channel, "You can only type strings between 3 and 17 characters.")
        elif len(message.content) > 9 and len(message.content) < 23:
            hugechar = 0
            huge = ""
            hugeletters = 0
            hugechar = 0
            huge = ""
            hugeletters = 0
            for i in range(len(message.content) - 6):
                if message.content[6 + hugechar].isalpha():
                    huge = huge + ":regional_indicator_" + message.content[6 + hugechar].lower() + ":"
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] == "-":
                    huge = huge + ":heavy_minus_sign:"
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] == " ":
                    huge = huge + " " * 12
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] in digits:
                    nb = int(message.content[6 + hugechar])
                    huge = huge + ":" + str(numbers[nb]) + ":"
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] == "!":
                    huge = huge + ":grey_exclamation:"
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] == "?":
                    huge = huge + ":grey_question:"
                    hugeletters = hugeletters + 1
                hugechar = hugechar + 1
            if hugeletters > 0:
                await client.send_message(message.channel, huge)
            elif hugeletters < hugechar:
                await client.send_message(message.channel, "*This command only supports letter A-Z, all numbers, ! ? and -.*")
    elif message.content[0:5] == "!hype":
        if len(message.content) == 5:
            await client.send_message(message.author, "Please type something after '!hype '.")
        elif len(message.content) >= 75:
            await client.send_message(message.channel, "Sorry, but your message is way too long! O_O")
        elif len(message.content) > 6 and len(message.content) < 75:
            hugechar = 0
            hype = ""
            hugeletters = 0
            for i in range(len(message.content) - 6):
                if message.content[6 + hugechar].isalpha():
                    hype = hype + ":regional_indicator_" + message.content[6 + hugechar].lower() + ":"
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] == "-":
                    hype = hype + ":heavy_minus_sign:"
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] == " ":
                    hype = hype + " " * 6 + ":clap:" + 6 * " "
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] in digits:
                    nb = int(message.content[6 + hugechar])
                    hype = hype + ":" + str(numbers[nb]) + ":"
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] == "!":
                    hype = hype + ":grey_exclamation:"
                    hugeletters = hugeletters + 1
                elif message.content[6 + hugechar] == "?":
                    hype = hype + ":grey_question:"
                    hugeletters = hugeletters + 1
                hype = hype + " "
                hugechar = hugechar + 1
            if hugeletters > 0:
                await client.send_message(message.author, "```" + hype + "```")
            elif hugeletters < hugechar:
                await client.send_message(message.channel, "*This command only supports letter A-Z, all numbers, ! ? and -.*")
    elif message.content[0:7] == "!C-to-F": # Celsius to Fahrenheit
        if len(message.content) == 7:
            await client.send_message(message.channel, "You must enter a temperature in Celsius.")
        elif len(message.content) >= 9:
            Celsius = float(message.content[8:])
            Fahrenheit = float(Celsius * 1.8 + 32)
            if Fahrenheit.is_integer():
                await client.send_message(message.channel, message.content[8:] + "°C is " + str(round(Fahrenheit)) + "°F.")
            else:
                await client.send_message(message.channel, message.content[8:] + "°C is about " + str(round(Fahrenheit)) + "°F.")
    elif message.content[0:7] == "!F-to-C": # Fahrenheit to Celsius
        if len(message.content) == 7:
            await client.send_message(message.channel, "You must enter a temperature in Farenheit.")
        elif len(message.content) >= 9:
            Fahrenheit = float(message.content[8:])
            Celsius = float((Fahrenheit - 32) * 5 / 9)
            if Celsius.is_integer():
                await client.send_message(message.channel, message.content[8:] + "°F is " + str(round(Celsius)) + "°C.")
            else:
                await client.send_message(message.channel, message.content[8:] + "°F is about " + str(round(Celsius)) + "°C.")

client.run("Token") # Note to self: this isn't actually the token, it's a reminder to replace this with the actual bot's token.
