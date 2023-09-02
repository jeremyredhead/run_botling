- config files which specify which bot files to run & their names/creators/rooms/etc
  - but which format(s)?? JSON, TOML, YAML, INI??
  - what option letter? -k maybe?
  - maybe try to load from some location like `~/run_botling.*` or `~/.config/run_botling.*`
  - maybe try to auto-detect if first/any argument is config file?

- multiple bot file arguments

- support -n BOTNAME -r ROOM like BotBot
  - incl. both as defaults and multiple times in a command per file,
    e.g. `run_botling.py -r xkcd -: -n CoolBot coolbot.txt -: -r test testing.txt`
    - `-:` is borrowed from cURL, which also uses --next. i'm inclined to also support `/`
  - maybe also -c CREATOR

- support snapshots e.g. -s SNAPSHOT_FOLDER
  - should i try to support per-bot snapshot configuration? 
    this would be difficult to impossible to support on mainline BotBot
