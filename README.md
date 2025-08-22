# Is it in stock yet?

Is there a high demand item that you want to buy online, but it is not in stock yet?

Are you tired of constantly refreshing the store web page to see if it is available?

This program can automatically check for you and alert you when it is in stock!

## Currently Supported Stores
- [Best Buy (Canada)](https://www.bestbuy.ca/)
- [Canyon Bicycles](https://www.canyon.com/)

## Currently Supported Notification Methods
- Discord DM notification (requires a personal Discord bot)
- Tkinter popup (**default**, generic window popup)

## Installation and Guide
1. `pip install -r requirements.txt`
2. Create a `.env` file matching the structure of `.env.template`
### For Devs
3. Setting up a new store:
    1. In the `/stores` folder, create a new `<storeName>.py` 
    2. Inherit the `store` abstract class from `store.py`
    3. Code!
4. Setting up a new notification method:
    1. In the `/notificationMethods` folder, create a new `<notificationMethodName>.py` 
    2. Inherit the `notificationMethod` abstract class from `notificationMethod.py`
    3. Code!
