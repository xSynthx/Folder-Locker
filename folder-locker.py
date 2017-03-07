##################################################################################
#  ©2017 Synthx                                                                  #
#  You may not redistribute as yours unless you have written consent from Synthx #
#  Twitter: @_synthx                                                             #
#  Email: synthx@protonmail.com or synthx01@gmail.com                            #
##################################################################################

# os.system('clear') is in place to keep people from seeing your password after you press enter!
import readline # arrow keys
import os # This imports your OS.
color = {
    'RED'             : '\033[1;91m',
    'UNDERLINE_PURPLE' : '\033[4;34m',
    'GREEN'           : '\033[1;92m',
    'YELLOW'          : '\033[1;33m',
    'CYAN'            : '\033[0;36m',
    'PURPLE'            : '\033[0;34m',
    'MAGENTA'         : '\033[0;35m',
    'DEFAULT'         : '\033[0m',
    'TWITTER_BLUE'            : '\033[38;5;33m',
}
incorrect = 'Wrong password! ' # You can change this to say whatever you like!
exitSentence = color['RED'] + '[Now Exiting!] ' + color['DEFAULT'] +'Folder Locker\n'
exit = False
idiot = 'You must be a idiot, you really think I would set that as my password? -_-\n' + exitSentence # You can change this to say whatever you like!
noRun = 'You are not allowed to enter that command here!'
credits = '©2017 Synthx\n' + color['TWITTER_BLUE'] + 'Twitter: @_Synthx' + color['DEFAULT'] + '\n@danbatiste\n@NyteLife26'
os.system("clear") # This will clear the screen for a nice and clean interface!

os.system('chflags hidden SeceretPasswordFile.txt') # make sure this file is in same directory that you are running this script from.
passwordFile = open('SeceretPasswordFile.txt') # make sure this file is in same directory that you are running this script from.
secretPassword = passwordFile.read()
header = color['RED'] + '''
          _____     _     _             _               _
         |  ___|__ | | __| | ___ _ __  | |    ___   ___| | _____ _ __
         | |_ / _ \| |/ _` |/ _ \ '__| | |   / _ \ / __| |/ / _ \ '__|
         |  _| (_) | | (_| |  __/ |    | |__| (_) | (__|   <  __/ |
         |_|  \___/|_|\__,_|\___|_|    |_____\___/ \___|_|\_\___|_|

''' + color['DEFAULT'] + '''                        +-----------------------+\n                        |  Created by ''' + color['TWITTER_BLUE'] + '''@_Synthx''' + color['DEFAULT'] + '''  |\n                        +-----------------------+
''' + color['DEFAULT']
print(header + 'Type "help" to begin!\n')
def Main():
	global exit
	maininput = input(color['TWITTER_BLUE'] + 'Folder Locker> ' + color['DEFAULT']) # You can change this to whatever you like! Dont forget the space after it.
	if maininput == '':
		Main()
	elif maininput.lower() == 'help':
		helpme()
	elif maininput.lower() == 'unlock':
		unlockst()
	elif maininput.lower() == 'lock':
		lockFolder()
	elif maininput.lower() == 'exit':
		os.system('clear')
		print(exitSentence)
		exit = True
	elif maininput.lower() == 'clear':
		os.system('clear')
		print(header)
		Main()
	elif maininput.lower() == 'info':
		os.system('clear')
		print(credits)
		Main()
	elif maininput == 'cancel':
		os.system('clear')
		print(header + '\n' + color['RED'] + noRun + color['DEFAULT'] + '\nThis command is only valid when trying to unlock a folder!')
		Main()
	else:
		print(color['RED'] + '[ERROR] COMMAND "' + maininput + '" NOT FOUND\n' + color['DEFAULT'] + 'PLEASE USE A PROPER COMMAND!\n')
def helpme():
	global exit
	os.system('clear')
	print(color['YELLOW'] + '''
+--------+-------------------------------------+
| help   |  shows this dialog                  |
+--------+-------------------------------------+
| unlock |  lets you unlock a specified folder |
+--------+-------------------------------------+
| lock   |  lets you lock a specified folder   |
+--------+-------------------------------------+
| exit   |  exits folder locker :/             |
+--------+-------------------------------------+
| clear  |  clears the screen                  |
+--------+-------------------------------------+
| info   |  shows credits for folder locker    |
+--------+-------------------------------------+
	''')
	Main()
def unlockst():
	os.system('clear')
	print(header + 'What folder would you like to unlock? Please type a Directory!')
	folderSelect = input(color['TWITTER_BLUE'] + "(e.x. ~/Desktop/FOLDER_NAME)> " + color['DEFAULT'])
	if "help" in folderSelect.lower() or "unlock" in folderSelect.lower() or "lock" in folderSelect.lower() or "exit" in folderSelect.lower() or "clear" in folderSelect.lower() or "info" in folderSelect.lower():
		unlockst()
	else:
		unlockMain(folderSelect)
def unlockMain(folder_select):
	global exit
	os.system('clear')
	print(header + 'Please enter in password to unlock the folder!')
	typedPassword = input(color['TWITTER_BLUE'] + "Folder Locker> " + color['DEFAULT']) # You can change this to whatever you like! Dont forget the space after it.
	if typedPassword == secretPassword:
		os.system('clear;' + 'chflags nohidden ' + folder_select + ';clear')
		print('Folder Unlocked!')
		theExit()
	elif typedPassword.lower() == 'password':
		os.system('clear')
		print(idiot)
		exit = True
	elif typedPassword == '12345':
		os.system('clear')
		print(idiot)
		exit = True
	elif typedPassword.lower() == 'synthx':
		os.system('clear')
		print(idiot)
		exit = True
	elif typedPassword.lower() == 'qwerty':
		os.system('clear')
		print(idiot)
		exit = True
	elif typedPassword.lower() == 'exit':
		os.system('clear')
		print(exitSentence)
		exit = True
	elif typedPassword.lower() == 'lock':
		os.system('clear')
		print(color['RED'] + 'You cannot use this command as the folder is already locked :/' + color['DEFAULT'])
	elif typedPassword.lower() == 'clear':
		os.system('clear')
	elif typedPassword.lower() == 'info':
		os.system('clear')
		print(noRun + '\nIf you would like to see credits, please type "cancel"!\nOtherwise, Please enter in password to unlock the folder!')
		unlockMain()
	elif typedPassword.lower() == 'cancel':
		os.system('clear')
		print(header)
		Main()
	else:
		os.system("clear")
		print(incorrect + exitSentence)
		exit = True
def lockFolder():
	os.system('clear')
	print(header + 'What folder would you like to lock? Please type a Directory!')
	lockInput = input(color['TWITTER_BLUE'] + "(e.x. ~/Desktop/FOLDER_NAME)> " + color['DEFAULT'])
	os.system('clear;' + 'chflags hidden ' + lockInput + ';clear')
	print('Folder Locked!')
	theExit()
def theExit():
	global exit
	print(header + 'Would you like to exit Folder Locker? Yes/no or Y/n')
	exitInput = input(color['TWITTER_BLUE'] + "Folder Locker> " + color['DEFAULT'])
	if "yes" in exitInput.lower() or "y" in exitInput.lower():
		os.system('clear')
		print(exitSentence)
		exit = True
	elif "no" in exitInput.lower() or "n" in exitInput.lower():
		os.system('clear')
		print(header + 'Please type "help" to begin!')
		Main()
	elif exitInput.lower() == 'exit':
		os.system('clear')
		print(exitSentence)
		exit = True
	else:
		os.system('clear')
		print('You may only say yes or no!')
		theExit()
while exit == False:
    Main()