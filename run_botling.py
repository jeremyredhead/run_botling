import sys
import re

# https://stackoverflow.com/questions/10043485/python-import-every-module-from-a-folder
# https://stackoverflow.com/questions/1057431/how-to-load-all-modules-in-a-folder
try:
	from .botbot.botbot.botcollection import BotCollection
except ImportError:
	from .botbot.botcollection import BotCollection
except ImportError:
	from botbot.botcollection import BotCollection

# Defaults -- set these as appropriate
defaults = {
	'room': 'test',
	'name': 'TestBot',
	'creator': 'Ana Ni Muss',
}

def run_file(file):
	botgroup = BotCollection(botbot=None)
	with open(file) as f:
		regex = r'(?:\s*!createbot\s*(?:&(?P<room>\S+)\s+)?@(?P<name>\S+))?(?P<code>.*)'
		m = re.match(regex, f.read(), re.DOTALL)
	room = m.group('room') or defaults.room
	name = (m.group('name') or defaults.name)[:36]
	code = m.group('code')
	creator = defaults.creator
	botgroup.create(nickname=name, room_name=room, password=None, creator=creator, code=code)

def main():
	if re.fullmatch('-\?|-h|--help', sys.argv[1]):
		print('USAGE:')
		print('\t{} <filename>'.format(sys.argv[0]))
	else:
		run_file(sys.argv[1])

if __name__ == "__main__":
	main()