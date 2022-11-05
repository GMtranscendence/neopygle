import requests
import json

class Wigle():

  def __init__(self, username, password, token=None):
    self.username = username
    self.password = password
    self.token = token
    self.session = requests.Session()
    self.auth()

  def search(self, ssid, netid):
    try:
      req = self.session.get('https://api.wigle.net/api/v2/network/search', params={'ssid':ssid, 'netid': netid})
      print(json.dumps(req.json(), indent=2))
    except (json.decoder.JSONDecodeError):
      print('Something went wrong')

  def auth(self):
    header = {'Host':'api.wigle.net', 'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
    post = self.session.post('https://wigle.net/api/v2/login',
                   data={'credential_0': self.username,
                         'credential_1': self.password,
                         'destination': '/'},
                          headers=header)

    if post.json()['success']:
      print('[*] Connected to wigle.net')
    else:
      print('Incorrect username and/or password')
