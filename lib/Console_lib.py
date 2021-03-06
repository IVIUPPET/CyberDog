# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:01:08 2016

CONSOLE LIB: A library of useful shit for the console

Last Updated: 8/16/2016

@author: Mike
"""
import datetime

def timeStamp(text, bad=0):
    ''' 'print' is boring. This has optional bad feedback if the message is 
    bad! Easier to see amidst a sea of printed lines. '''
    
#    print('[+] [{:%b-%d-%Y %H:%M:%S}] CSCAN V1.0 BETA\
#    Init!'.format(datetime.datetime.now()))
# 
    if bad == 0:
        print('[+] [{:%b-%d-%Y %H:%M:%S}] '.format(datetime.datetime.now()) +
        text)
        outstring = '[+] [{:%b-%d-%Y %H:%M:%S}]'.format(datetime.datetime.now()) + text
    else:
        print('[-] [{:%b-%d-%Y %H:%M:%S}] '.format(datetime.datetime.now()) +
        text)
        outstring = '[-] [{:%b-%d-%Y %H:%M:%S}] '.format(datetime.datetime.now()) + text
    return outstring # Return the string for optional use elsewhere

def log(text, file_name):
    #https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file
    with open(file_name, 'a') as f:
        f.write(text + '\n')
    f.closed # is this even necessary?


