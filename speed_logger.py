### SCRIPT TO READ AND TWEET INTERNET SPEED TO BT

import subprocess as sp
from twitter.api import Twitter

test_speed = sp.Popen('python speedtest_cli.py --simple', shell=True, stdout=sp.PIPE)
# test_speed.wait()

# output = []
# for line in test_speed.stdout:
#     try:
#         output.append(line)
#     except BrokenPipeError:
#         continue

username = 'BTUserScotland'
password = 'ironmaiden54'

twitter = Twitter(username,password)
twitter.statuses.update(status='Here is a test tweet from Python.')

output = [b'Ping: 441.598 ms\n']
for i in range(len(output)):
    output[i] = (output[i].decode("utf-8")).split(' ')[1]
    print(output[i])
