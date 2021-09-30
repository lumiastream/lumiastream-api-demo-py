from time import sleep
import requests

# Paste token from Lumia Stream (Settings > Advanced > Developers API > Show Token)
token = 'paste-token-here'

# Get settings
response = requests.get('http://localhost:39231/api/retrieve?token=' + token)
print('response: ', response.json())

# Send Chat Command
requests.post('http://localhost:39231/api/send?token=' + token,
              data={'type': 'chat-command', 'params': {'value': 'blue'}})
sleep(1)

# Send Alert
requests.post('http://localhost:39231/api/send?token=' + token,
              data={'type': 'alert', 'params': {'value': 'twitch-follower'}})
sleep(1)

# Send RGB Colors with Brightness
requests.post('http://localhost:39231/api/send?token=' + token, data={type: 'rgb-color', 'params': {
              'value': {'r': 20, 'g': 100, 'b': 10}, 'brightness': 100, 'transition': 0, 'duration': 5000}})
sleep(1)

# Send Text To Speech
requests.post('http://localhost:39231/api/send?token=' + token,
              data={type: 'tts', 'params': {'value': 'Wow, this tutorial is so cool'}})
sleep(1)

# Send Chatbot message
requests.post('http://localhost:39231/api/send?token=' + token,
              data={type: 'chatbot-message', 'params': {'value': 'Wow, this tutorial is so cool', 'platform': 'twitch'}})
sleep(1)
