import os
import requests
from .notificationMethod import notificationMethod

class discord(notificationMethod):

    def __init__(self):
        super().__init__()
        self.discordBotToken = os.environ.get('DISCORD_BOT_TOKEN')
        self.userId = os.environ.get('DISCORD_USER_ID')
        self.headers = {
            'User-Agent': 'DiscordBot (https://discord.com/, 1.0)',
            'Content-Type': 'application/json',
            'Authorization': f'Bot {self.discordBotToken}',
        }

    def _getDmChannel(self):
        url = f'https://discord.com/api/v10/users/@me/channels'
        json = {'recipient_id': self.userId}
        timeout = 10
        try:
            response = requests.post(url, headers=self.headers, json=json, timeout=timeout)
        except requests.exceptions.RequestException as e:
            print(f'Discord fetch DM channel failed:\n{e}')
        channel = response.json()
        return channel['id']

    def notify(self, message):
        channelId = self._getDmChannel()
        url = f'https://discord.com/api/v10/channels/{channelId}/messages'
        json = {'content': message}
        timeout = 10
        try:
            response = requests.post(url, headers=self.headers, json=json, timeout=timeout)
        except requests.exceptions.RequestException as e:
            print(f'Discord DM notification failed:\n{e}')
