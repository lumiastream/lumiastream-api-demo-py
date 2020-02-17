import requests

token = 'paste-token-here'

response = requests.get('http://localhost:39231/api/retrieve?token=' + token)
print('response: ', response.json())

requests.post('http://localhost:39231/api/send?token=' + token, data={ 'type': 'chat-color', 'value': 'blue' })
