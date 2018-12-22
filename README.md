# reddit-meme-economy-investor-helper

With the recent arrival of [MemeInvestor_bot](https://www.reddit.com/user/MemeInvestor_bot) on [r/MemeEconomy](https://www.reddit.com/r/MemeEconomy/),
 serious measures must be taken in order to invest wisely. 

Thus, `reddit-meme-economy-investor-helper` has seen the light.

Every 5 seconds, the total score of the given post will be fetched and added to a dictionary.
This dictionary will then be converted into json, and used to generate a line chart with Chart.js.

![reddit-meme-economy-investor-helper](https://twinnation.org/api/v1/screenshots/2018-05-28_170123.png)

![reddit-meme-economy-investor-helper](https://twinnation.org/api/v1/screenshots/2018-05-28_182455.png)

This project is just for fun, feel free to PR if you want to implement any new features.


## Requirements 

- Python 3.x


## Instruction

Create an application [here](https://www.reddit.com/prefs/apps/) on reddit (for auth)

Once you have a `client_id` and a `client_secret`, just replace `os.getenv('CLIENT_ID')` and `os.getenv('CLIENT_SECRET')` 
in `app.py` by your client id and your client secret respectively.


## Dependencies

- flask
- praw
- apscheduler
