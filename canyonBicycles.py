import os
import requests

def check(soup):
    inStockButton = soup.find(id='js-productDetailBuyButton')
    innerText = inStockButton.getText(strip=True).lower()
    print(innerText)
    if innerText == 'add to cart':
        discordNotification()

'''
    Discord notification
'''
def discordNotification():
    discordBotToken = os.environ.get('DISCORD_BOT_TOKEN')
    channelId = os.environ.get('DISCORD_CHANNEL_ID')
    discordUrl = f'https://discord.com/api/v10/channels/{channelId}/messages'
    itemUrl = os.environ.get('URL')
    content = f'THE BIKE IS IN STOCK\n{itemUrl}\n(If I\'m still spamming and Tony isn\'t available to stop me, right click me on the sidebar and mute me for now.)'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bot {discordBotToken}',
        }
    json = {'content': content}
    request = requests.post(discordUrl, headers=headers, json=json)
    print(request.text)
