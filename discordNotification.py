import os
import requests

discordBotToken = os.environ.get('DISCORD_BOT_TOKEN')
headers = {
    'User-Agent': 'DiscordBot (https://discord.com/, 1.0)',
    'Content-Type': 'application/json',
    'Authorization': f'Bot {discordBotToken}',
    }

'''
    Get DM Channel from User ID
'''
def getDmChannel(userId):
    url = f'https://discord.com/api/v10/users/@me/channels'
    json = {'recipient_id': userId}
    response = requests.post(url, headers=headers, json=json)
    print(f'Discord fetch DM channel status code: {response.status_code}')
    channel = response.json()
    return channel['id']

'''
    Discord DM notification
'''
def dmNotify(message):
    userId = os.environ.get('DISCORD_USER_ID')
    channelId = getDmChannel(userId)
    url = f'https://discord.com/api/v10/channels/{channelId}/messages'
    json = {'content': message}
    response = requests.post(url, headers=headers, json=json)
    print(f'Discord DM notification status code: {response.status_code}')
