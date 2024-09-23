# Fetch Installer
# Also updates dependencies

import os

dependencies = ["discord", "requests"] # Can be updated and it will automatically update on this running

for dependency in dependencies:
	print("{}: updating dependency".format(dependency))
	os.system("pip install {}".format(dependency))
	print("{}: updated dependency".format(dependency))

print("Running fetch_bot.py..") 
os.system("python fetch_bot.py") # run the bot