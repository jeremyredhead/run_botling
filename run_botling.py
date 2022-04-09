import sys
import re

from botbot.botcollection import BotCollection

# Defaults -- set these as appropriate
_room = 'test'
_name = 'TestBot'
creator = 'Ana Ni Muss'

def run_file(file):
	botgroup = BotCollection(botbot=None)
	with open(file) as f:
		regex = r'(?:\s*!createbot\s*(?:&(?P<room>\S+)\s+)?@(?P<name>\S+))?(?P<code>.*)'
		m = re.match(regex, f.read(), re.DOTALL)
	room = m.group('room') or _room
	name = m.group('name')[:36] or _name
	code = m.group('code')
	botgroup.create(nickname=name, room_name=room, password=None, creator=creator, code=code)

def main():
	if re.fullmatch('-\?|-h|--help', sys.argv[1]):
		print('USAGE:')
		print('\t{} <filename>'.format(sys.argv[0]))
	else:
		run_file(sys.argv[1])

if __name__ == "__main__":
	main()