'''
=========================
MICROSOFT_SLATEBOT_V2.PY
=========================
:Author: Elizabeth
:Date Created: 2018/11/22
:Last Updated: 2018/11/22
:Description: Created to help a medical doctor with social anxiety lose a karaoke competition in a fit of Seinfeld-inspired terror.  Now with Discord-specific emojis!  Even MORE obnoxious!

INSTRUCTIONS FOR USE: 
1. Place the .txt file that you want to Slate-ify into the same directory as this file.  
2. Install Python 3.6 from this link: https://www.python.org/downloads/release/python-367/
3. If on Windows, enter in "Powershell" to the search, & click the link
4. On the command line, type
	"cd [COMPLETE DIRECTORY PATH OF SCRIPT]"
5. Once there, type in:
	"python ./microsoft_slate_v2.py [NAME OF YOUR FILE].py"
The final version of the file should be located in the same directory. 
'''

import io
import os
import sys


def main(argv):
	# Examine all text files and select the one with the same name as the designated filetype.
	filename = argv[1]
	for root, dirs, files in os.walk(os.getcwd()):
		if filename not in files:
			print("Filename not found!")
			print(files)
			sys.exit(1)
		else:
			#try: 
			orig = open(filename, "r")
			if filename + "_BEES_indicator.txt" in files:
				new = open(filename + "_BEES_indicator.txt", "w")
			else:
				new = open(filename + "_BEES_indicator.txt", "a")
			buffer = orig.readline()
			while buffer is not "":
				if buffer is not "\n" and not buffer.isspace():
					newstring = buffer.rstrip("\n")
					newstring_indicators = ""
					# ERROR HANDLING FOR COMMAS, SPACES, NUMBERS, AND SPECIAL CHARACTERS:
					for letter in newstring:
						if letter.isalpha():
							letter = letter.lower()
							letter_indicator = ":regional_indicator_" + letter + ":"
						elif letter.isnumeric():
							# Dictionary object with spelled out reference. 
							dict = {"0":"zero", "1": "one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
							letter_indicator = ":" + dict[letter] + ":"
						elif letter.isspace():
							letter_indicator = " "
						else:
							letter_indicator = ""
						newstring_indicators = newstring_indicators + letter_indicator + " "
					newstring_indicators = newstring_indicators + "\n"
					new.write(newstring_indicators)
				buffer = orig.readline()
				
			# except Exception:
				# print("Read/write file failed.  Check that you have permission to write to this directly.")
				# sys.exit(1)
	print("'Well, thank Heavens it's over... hopefully that never happens again.'")
	sys.exit(0)


if __name__ == "__main__":
	main(sys.argv)