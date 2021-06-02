# -*- coding: utf-8 -*-
'''
Created on 2021/06/01

@author: ZL Chen
@Task: Develop a tool for log filtering

Create an application with the ability to parse logs to look for certain patterns in test results:

1.	Download the Logcat log: https://drive.google.com/file/d/1xWOP76X8qxQDL9kxa-URNGhChY_rET1o/view?usp=sharing
2.	Develop a tool in Java or Python with the following switches:
-h prints out info about all the available switches
-s prints out the time difference between lines containing “TEST STARTED” and “TEST FINISHED”
-i <args,…> prints out lines containing all the provided arguments
-e <args,…> prints out all lines which don't contain any of the provided arguments

Usage (Python): python logcat_parser.py logcat_file.txt -i word1,word2,word3
Usage (Java): java -jar logcat_parser.jar logcat_file.txt -i word1,word2,word3

3. Send us a link to your Git repository with sources (and, in case of Java, also a jar file) on a publicly accessible service (GitHub, GitLab, Bitbucket).

'''

import sys
from time import sleep

class logcat_parser(object):
	def open_logcat_file(self, filename):
		self = open(filename, 'r')
		return self

	def h(self):
		print('-h prints out info about all the available switches')
		print('-s prints out the time difference between lines containing \"TEST STARTED\" and \"TEST FINISHED\"')
		print('-i <args,…> prints out lines containing all the provided arguments')
		print('-e <args,…> prints out all lines which don\'t contain any of the provided arguments')

	def s(self, filename):
		s_info = self.open_logcat_file(filename)
		for i in s_info:
			# print(i.strip())
			if 'TEST STARTED' in i:
				start = i.strip('1. TEST STARTED: ').strip(' sec')[:4]
				# print(start)
			if 'TEST FINISHED' in i:
				finish = i.strip('2. TEST FINISHED: ').strip(' sec')[:4]
				# print(finish)
		difference = str(float(finish) - float(start))
		print('Time difference is:', difference)

	def i(self, filename, args):
		i_info = self.open_logcat_file(filename)
		i_split = list()
		i_split = args.split(',')
		i_length = len(i_split)
		for i in i_info:
			for string_check in range(i_length):
				if i_split[string_check] in i.strip():
					print(i.strip())
					break

	def e(self, filename, args):
		e_info = self.open_logcat_file(filename)
		e_split = list()
		e_split = args.split(',')
		e_length = len(e_split)
		for e in e_info:
			for string_check in range(e_length):
				if e_split[string_check] not in e.strip():
					print(e.strip())
					break

if __name__ == '__main__':
	logcat_parser = logcat_parser()
	argument = sys.argv[1]
	if argument == None:
		raise 'syntax error.'
	elif argument == '-h':
		logcat_parser.h()
	elif argument == 'logcat_file.txt' and sys.argv[2] == '-s':
		logcat_parser.s(argument)
	elif argument == 'logcat_file.txt' and sys.argv[2] == '-i':
		logcat_parser.i(argument, sys.argv[3])
	elif argument == 'logcat_file.txt' and sys.argv[2] == '-e':
		logcat_parser.e(argument, sys.argv[3])
	else:
		raise 'syntax error.'
