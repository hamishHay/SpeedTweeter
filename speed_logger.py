### SCRIPT TO READ AND TWEET INTERNET SPEED TO BT

import subprocess as sp
import tweepy
import numpy as np

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

keys = np.genfromtxt('keys.txt',dtype='str')

cfg = {
"consumer_key"        : keys[0],
"consumer_secret"     : keys[1],
"access_token"        : keys[2],
"access_token_secret" : keys[3]
}

test_speed = sp.Popen('python speedtest_cli.py --simple', shell=True, stdout=sp.PIPE)

output = []
for line in test_speed.stdout:
    try:
        output.append(line)
    except BrokenPipeError:
        continue

for i in range(len(output)):
    output[i] = float((output[i].decode("utf-8")).split(' ')[1])
    print(output[i])


down_speed = output[1]
min_speed = 0.1

if down_speed < min_speed:
    api = get_api(cfg)
    tweet = "My current download speed is {:.1f} Mbit/s!".format(down_speed)
    status = api.update_status(status=tweet)
