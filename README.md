# run_botling.py
>(*i don't have a better name yet*)

Easily run a BotBot botling standalone, i.e. without BotBot itself.

Once the dependencies are installed, just plop `run_botling.py` down in any folder,  
and pass it the name of a file containing your bot's code. (e.g. `py run_botling.py spambot.txt`)  

The `!createbot &room @BotName` prefix is technically optional, but highly encouraged,  
as currently the only other way to change the name or room is editing the python file.  
(you will **have** to edit the file if you want the creator variable to refer to you :S)  

## Dependencies (*and how to install them*)  

### Python (naturally)

As this program & botbot itself are written in Python,  
you will need Python installed to run this, specifically Python 3  

To see if it's installed already, just open up Terminal (mac/unix), or Command Prompt (win)  
then type `python --version`, or `py --version` on Ms Windows.  
If it says Python 3.x.x, then YAY! It's already installed!  
Otherwise head over to https://python.org/downloads/ and install a recent 3.x version  

### BotBot library

Now that Python is installed, we'll want to install the BotBot library.  
But first, run `python -m pip show setuptools` for me, will you? (On Windows:tm:, use `py`)  
If the version listed is 58 or above, you'll need to use [my fork of BotBot](https://github.com/jeremyredhead/BotBot)  
(Actually, let's just use my fork either way)  

*But wait, how to download & install botbot? :thinking:*

#### Download BotBot

If you have git installed, then just run `git clone https://github.com/jeremyredhead/BotBot`  
(But actually, first, make sure to `cd` into your Documents folder or something)  
If you don't have git, then just click the big ol' Code button and...  
Actually, let's [download & install git](https://git-scm.com/downloads) anyway (for now),  
because I'm not actually sure if BotBot's dependencies can be installed without it.  

#### Install BotBot

First, `cd` into the BotBot folder, where ever you put it.  
Then, run `python setup.py install` (or `py` on windows).  
A bunch of text will scroll onto your screen for a lil while until its finishes.  
If the end of the text says something like:  
`Finished processing dependencies for botbot==x.y.z`  
Then congrats! BotBot is now installed!  
If not... uhhh... tell me and I'll see if I can figure it out.  
