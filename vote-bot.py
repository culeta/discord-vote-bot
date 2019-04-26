import discord

client = discord.Client()

# リアクションボタン
reaction_list = ['\U0001F1E6', '\U0001F1E7', '\U0001F1E8', '\U0001F1E9', '\U0001F1EA']
lst_emoji = ''
count = 1
# 投票をした人のリスト
vote_list = []


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_message(message):

    if message.content.startswith('/vote'):
        # メッセージの取得・list化
        msg = message.content[6:]
        msg_list = msg.split()
        # リスト数の取得
        global count
        count = len(msg.split())
        count -= 1
        # 絵文字のリスト
        emoji_list = [' ', ':regional_indicator_a:', ':regional_indicator_b:', ':regional_indicator_c:',
                      ':regional_indicator_d:', ':regional_indicator_e:']
        # 質問内容
        skip_msg = msg_list[0]
        # リアクションをつけるメッセージ
        global lst_emoji
        lst_emoji = emoji_list[count]

        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            await message.channel.send(skip_msg)

            for emoji_list, msg_list in zip(emoji_list, msg_list):
                if msg_list == skip_msg:
                    continue
                await message.channel.send(emoji_list + msg_list)

    if message.content.startswith(lst_emoji):
        for i in range(0, count):
            await message.add_reaction(reaction_list[i])


# BotのTokenを張り付ける
client.run("token")