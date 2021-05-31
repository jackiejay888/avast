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