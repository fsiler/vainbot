#!/usr/bin/env python3
#
### suggested cron setup:
#REDDIT_CLIENT=""
#REDDIT_SECRET=""
#REDDIT_USER=""
#REDDIT_PW=""
#10 */3 *   *   *     python3 -m pip install praw pip --upgrade -q; zerovote.py
#
from sys import argv, exit
from os  import environ as e
import praw

c = e.get('REDDIT_CLIENT')
s = e.get('REDDIT_SECRET')
u = e.get('REDDIT_USER')
p = e.get('REDDIT_PW')

if not all([c,s,u,p]):
  print("missing configuration variables")
  exit()

r = praw.Reddit(
    client_id=c,
    client_secret=s,
    username=u,
    password=p,
    user_agent=argv[0]
)

def process(c):
  """Delete comments if the score is less than one"""
  if c.score < 1:
    print("DELETING comment id %s, score %d: %s" % (c.id, c.score, c.body))
    c.delete()

if __name__=="__main__":
  for c in r.redditor(u).comments.new():
    process(c)
