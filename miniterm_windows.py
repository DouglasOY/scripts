#!/usr/bin/env python

import os
import sys
import serial
import time
import datetime

MINICOMCRLF  = '\n'
PROMPT       = '# '
EXITCMD      = 'exitcom'

class Miniterm:
    def __init__(self):
        self.ser = serial.Serial(port = 'com2', baudrate = 115200, timeout = 1)

    def readseconds(self, runtime):
        exittime = datetime.datetime.now() + datetime.timedelta(seconds=runtime)
        while True:
            data = self.ser.readline()
            sys.stdout.write(data)
            now = datetime.datetime.now()
            if now >= exittime:
                break

    def readkeyword(self, keyword):
        while True:
            data = self.ser.readline()
            sys.stdout.write(data)
            if data.find(keyword) == 0:
                break

    def writer(self, data):
        self.ser.write(data)
        # self.ser.flush()
        time.sleep(0.5)

    def open(self):
        try:
            self.ser.open()
        except Exception, e:
            print e

        isopen = self.ser.isOpen()
        if isopen:
            print '!!!! open console True  !!!!'
            return True
        else:
            print '!!!! open console False !!!!'
            return False

    def waitopen(self):
        while True:
            openflag = self.ser.isOpen()
            if openflag:
                print '#### open console ####'
                return True
            else:
                print '#### wait 2 seconds ####'
                time.sleep(2)

    def interactive(self):
        while True:
            command = raw_input()
            if command == EXITCMD:
                break
            else:
                self.writer(command + MINICOMCRLF)

            while True:
                data = self.ser.readline()
                sys.stdout.write(data)
                if data == PROMPT:
                    break

    def close(self):
        self.ser.close()
        time.sleep(1)


def main():
    miniterm = Miniterm()
    # miniterm.open()
    miniterm.waitopen()
    miniterm.readkeyword('OS is running')
    miniterm.writer(MINICOMCRLF)
    miniterm.writer(MINICOMCRLF)

    '''
    set ip
    '''
    ETH0IP = 'ifconfig eth0 inet 192.168.0.100 up'
    miniterm.writer(ETH0IP + MINICOMCRLF)

    '''
    output of the case
    '''
    miniterm.readseconds(1)
    miniterm.interactive()

    '''
    close the console
    '''
    miniterm.close()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    main()

