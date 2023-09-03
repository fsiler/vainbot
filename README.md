# VainBot
This is a very simple Python script using the `praw` library..
All it does is scan your account for your own comments, and delete them when the fall below a score of 1.


## Configuration (cron job)

```
REDDIT_CLIENT=""
REDDIT_SECRET=""
REDDIT_USER=""
REDDIT_PW=""
10 */3 *   *   *     python3 -m pip install praw pip --upgrade -q; VainBot.py
```
