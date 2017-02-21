##################################################################################
#  ©2017 Synthx                                                                  #
#  You may not redistribute as yours unless you have writen consent from Synthx  #
#  Twitter: @_synthx                                                             #
#  Email: synthx@protonmail.com or synthx01@gmail.com                            #
##################################################################################

# os.system('clear') is in place to keep people from seeing your password after you press enter!
import readline # arrow keys
import os # This imports your OS.
version = 'V2.0.0'
incorrect = 'Wrong password, Please try again!' # You can change this to say whatever you like!
exitsentence = 'Exiting Folder Lock ' + version + '\n'
exit = False
idiot = 'You must be a fucking idiot, you really think I would set that as my password?\n' + exitsentence # You can change this to say whatever you like!
os.system("clear") # This will clear the screen for a nice and clean interface!

os.system('chflags hidden SeceretPasswordFile.txt') # make sure this file is in same directory that you are running this script from.
passwordFile = open('SeceretPasswordFile.txt') # make sure this file is in same directory that you are running this script from.
secretPassword = passwordFile.read()
print('''
  _____     _     _             _               _
 |  ___|__ | | __| | ___ _ __  | |    ___   ___| | _____ _ __
 | |_ / _ \| |/ _` |/ _ \ '__| | |   / _ \ / __| |/ / _ \ '__|
 |  _| (_) | | (_| |  __/ |    | |__| (_) | (__|   <  __/ |
 |_|  \___/|_|\__,_|\___|_|    |_____\___/ \___|_|\_\___|_|

''')
print('                        -=-=-=-=-=-=-=-=-=-=-=-=-\n                          Folder Locker ' + version + '\n                          Created by Synthx\n                        -=-=-=-=-=-=-=-=-=-=-=-=-')
print('Type "help" to begin!\n')
def Main():
	global exit
	maininput = input(">>> ") # You can change this to whatever you like! Dont forget the space after it.
	if maininput == 'help':
		helpme()
	elif maininput == 'unlock':
		unlockst()
	elif maininput == 'lock':
		os.system("clear")
		print('Folder locked! ' + exitsentence)
		os.system('chflags hidden ~/Desktop/Hidden\ Folder') # Change ~/Desktop/HiddenFolder to what ever directory of your choice, and whatever name you want for the folder.
		exit = True
	elif maininput == 'exit':
		os.system('clear')
		print(exitsentence)
		exit = True
	elif maininput == 'Exit':
		os.system('clear')
		print(exitsentence)
		exit = True
	elif maininput == 'clear':
		os.system('clear')
	else:
		print('[ERROR] COMMAND NOT FOUND\nPLEASE USE A PROPER COMMAND!')
def helpme():
	global exit
	print('|------------|-------------------------------|')
	print('| help       |   shows this dialog           |')
	print('| unlock     |   lets you unlock folder      |')
	print('| lock       |   locks the folder            |')
	print('| exit       |   exits the program           |')
	print('| clear      |   clears the screen           |')
	print('|------------|-------------------------------|')
	Main()
def unlockst():
	os.system('clear')
	print('Please enter in password to unlock the folder!')
	unlockmain()
def unlockmain():
	global exit
	typedPassword = input(">>> ") # You can change this to whatecer you like! Dont forget the space after it.
	if typedPassword == secretPassword:
		os.system("clear")
		print('Folder Unlocked! ' + exitsentence)
		os.system("chflags nohidden ~/Desktop/Hidden\ Folder") # Change ~/Desktop/HiddenFolder to what ever directory of your choice, and whatever name you want for the folder.
		exit = True
	elif typedPassword == 'password':
		os.system('clear')
		print(idiot)
		exit = True
	elif typedPassword == '12345':
		os.system('clear')
		print(idiot)
		exit = True
	elif typedPassword == 'synthx':
		os.system('clear')
		print(idiot)
		exit = True
	elif typedPassword == 'Synthx':
		os.system('clear')
		print(idiot)
		exit = True
	elif typedPassword == 'exit':
		os.system('clear')
		print(exitsentence)
		exit = True
	elif typedPassword == 'Exit':
		os.system('clear')
		print(exitsentence)
		exit = True
	elif typedPassword == 'lock':
		os.system('clear')
		print('You cannot use this command as the folder is already locked :/')
	elif typedPassword == 'clear':
		os.system('clear')
	else:
		os.system("clear")
		print(incorrect)
		unlockmain()
while exit == False:
    Main()