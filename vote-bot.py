import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_message(message):

    if message.content.startswith('/vote'):
        tmp = 96
        # メッセージの取得・list化
        msg = message.content[6:]
        msg_list = msg.split()
        # リスト数の取得
        count = len(msg.split())
        # 投票をした人のリスト
        vote_list = []
        # 絵文字のリスト
        emoji_list = []
        vote_switch = ':regional_indicator_{}: '
        test = msg_list[0]
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            await message.channel.send(msg_list[0])

            for i in range(1, count):
                tmp += 1
                revmsg = vote_switch.format(chr(tmp))
                emoji_list.append(revmsg)
                await message.channel.send(emoji_list[i - 1] + msg_list[i])


# BOTのTokenを張り付ける
client.run("token")