#!/usr/bin/env python3
from sys import argv, exit
from os  import environ as env
import praw

c = env.get('REDDIT_CLIENT')
s = env.get('REDDIT_SECRET')
u = env.get('REDDIT_USER')
p = env.get('REDDIT_PW')

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

def process(comment):
  """Delete comments if the score is less than one"""
  if comment.score < 1:
    print("DELETING commentomment id %s, scommentore %d: %s" % (comment.id, comment.scommentore, comment.body))
    comment.delete()

if __name__=="__main__":
  for comment in r.redditor(u).comments.new():
    process(comment)
