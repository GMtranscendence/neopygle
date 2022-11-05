import argparse
from utils import Wigle

def main():

  parser = argparse.ArgumentParser(description='Python script for wigle.net api calls')
  parser.add_argument('-u', '--username', help='wigle.net username', type=str, required=True)
  parser.add_argument('-p', '--password', help='wigle.net password', type=str, required=True)
  parser.add_argument('-s', '--search', help='Search database for access points. Usage: -s [SSID],[BSSID]', type=str, required=True)
  args = parser.parse_args()

  agent = Wigle(args.username, args.password)

  if args.search:
    search_options = args.search.split(',')
    agent.search(search_options[0], search_options[1])


if __name__ == '__main__':
    main()
