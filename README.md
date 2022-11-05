# Python script for wigle.net api calls

## Installation
```
git clone https://github.com/GMtranscendence/neopygle.git
cd neopygle
pip install -r require.txt
```

## Usage

### As a script
```
python pygle.py -u YOUR_USERNAME -p YOUR_PASSWORD -s SSID,BSSID
```

### As a library
```
from utils import Wigle
agent = Wigle('YOUR_USERNAME', 'YOUR_PASSWORD')
search_json = agent.search('SSID', 'BSSID')
```
