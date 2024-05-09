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
    timeout = 5
    try:
        response = requests.post(url, headers=headers, json=json, timeout=timeout)
        print(f'Discord fetch DM channel status code: {response.status_code}')
    except:
        print(f'Discord fetch DM channel hung after {timeout} seconds')
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
    timeout = 5
    try:
        response = requests.post(url, headers=headers, json=json, timeout=timeout)
        print(f'Discord DM notification status code: {response.status_code}')
    except:
        print(f'Discord DM notification hung after {timeout} seconds')
