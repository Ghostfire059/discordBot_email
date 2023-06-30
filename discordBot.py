class discordBot:
    def __init__(self, channelId):
        self.__channelId = channelId
        self.__textLimit = 2000

    async def postMessage(self, bot, message):
        '''Use the bot provided to send the message on the channelId can send several messages due to the Discord's textLimit'''
        print("posting message on Discord")
        channel = bot.get_channel(self.__channelId)
        textStep = 1
        for char in range(0, len(message), self.__textLimit):
            truncatedMessage = message[char:textStep*self.__textLimit]
            await channel.send(truncatedMessage)
            textStep+=1
        print("\tposted!")
