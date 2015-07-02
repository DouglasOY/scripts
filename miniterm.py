#!/usr/bin/env python

import os
import sys
import serial
import time
import shutil
import telnetlib
import datetime 

# ONLY need change the BOARD and SETSERVERIP  
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BOARD           = 3                                 #   1,            2,            3
TESTUSER        = 'auto'
SETSERVERIP     = 'setenv serverip 192.168.0.190'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TTY             = '/dev/ttyU'                       #   '/dev/ttyU0'  '/dev/ttyU1'  '/dev/ttyU2'  
SETIPADDR       = 'setenv ipaddr 192.168.0.25'      #   251           252           253
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

CASELIST       = ['ktos_package/ktos_package.bin']

stateon         = "State        : ON"
stateoff        = "State        : OFF"
TELNETRETRY     = 20
MINICOMCRLF     = '\n'
TELNETCRLF      = '\r'
ECHOCASE        = 'echo '
GOENTRY         = 'go 200000'
RESETWAIT       = 10

HITKEY          = 'Hit any key to stop autoboot'
BYTESTRANSFER   = 'Bytes transferred = '
TFTPERR1        = 'Retry count exceeded; starting again'
TFTPERR2        = 'Not retrying'
TFTPERR3        = 'Auto-negotiation error is present'

TESTDONE        = "It's built on"
TESTCOUNT       = 2000

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
WAITAUTOBOOT01  = 2
WAITAUTOBOOT2   = 6
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def do_telnet(host, username, password, board):
    tn = telnetlib.Telnet(host)

    # login
    try:
        tn.read_until("ser Name : ")
    except EOFError, e:
        return 200

    tn.write(username + TELNETCRLF)
    if password:
        tn.read_until("assword  : ")
        tn.write(password + TELNETCRLF)

    tn.read_until("\r\n> ")
    # ------- Control Console -------
    # 1- Device Manager
    # 2- Network
    # 3- System
    # 4- Logout


    tn.write("1" + TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Device Manager ----------
    # 1- Phase Management
    # 2- Outlet Management
    # 3- Power Supply Status


    tn.write("2" + TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Outlet Management ----------
    #  1- Outlet Control/Configuration
    #  2- Outlet Restriction

    tn.write("1" + TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Outlet Control/Configuration -----
    #  1- Outlet 1                 OFF
    #  2- Zedboard-1               ON
    #  3- Outlet 3                 OFF
    #  4- Zedboard-2               OFF
    #  5- Outlet 5                 OFF
    #  6- Outlet 6                 OFF
    #  7- Outlet 7                 OFF
    #  8- Outlet 8                 OFF
    #  9- Master Control/Configuration

    if board == 1:
        tn.write("2" + TELNETCRLF)
    elif board == 2:
        tn.write("4" + TELNETCRLF)
    elif board == 3:
        tn.write("6" + TELNETCRLF)
    else:
        print "the board does not exist !! "
        tn.close()
        return 300
        
    tn.read_until("\r\n> ")
    # ------- Zedboard-1 -----------
    #    Name         : Zedboard-1
    #    Outlet       : 2
    #    State        : ON
    #    1- Control Outlet    
    #    2- Configure Outlet  

    tn.write("1" + TELNETCRLF)
    controloutlet  = tn.read_until("\r\n> ")
    # ------- Control Outlet --------
    #     Name         : Zedboard-1
    #     Outlet       : 2
    #     State        : ON
    #  1- Immediate On
    #  2- Immediate Off
    #  3- Immediate Reboot
    #  4- Delayed On
    #  5- Delayed Off
    #  6- Delayed Reboot
    #  7- Cancel 

    poweron  = controloutlet.find(stateon)    
    poweroff = controloutlet.find(stateoff)    
    if (poweron > 20) and (poweroff == -1):
        tn.write("3" + TELNETCRLF)
        print "shutdown and delay for 5 seconds, reboot"
    else:
        tn.write("1" + TELNETCRLF)
        print "immediately turn on"

    tn.read_until("to cancel : ")
    # ----------------------------------
    #    Immediate Reboot
    #    This command will immediately shutdown
    #    outlet 2 named 'Zedboard-1', delay for 5 seconds,
    #    and then restart.
    #    Enter 'YES' to continue or <ENTER> to cancel : yes

    tn.write("YES" + TELNETCRLF)
    tn.read_until("to continue...")
    # Command successfully issued.
    # Press <ENTER> to continue...

    tn.write(TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Control Outlet ------
    # ?- Help, <ESC>- Back, <ENTER>- Refresh, <CTRL-L>- Event Log

    tn.write("\x1b" + TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Zedboard-1 -------
    # ?- Help, <ESC>- Back, <ENTER>- Refresh, <CTRL-L>- Event Log

    tn.write("\x1b" + TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Outlet Control/Configuration -------
    #     <ESC>- Back, <ENTER>- Refresh, <CTRL-L>- Event Log

    tn.write("\x1b" + TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Outlet Management ----------
    # <ESC>- Back, <ENTER>- Refresh, <CTRL-L>- Event Log


    tn.write("\x1b" + TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Device Manager ------
    # <ESC>- Back, <ENTER>- Refresh, <CTRL-L>- Event Log

    tn.write("\x1b" + TELNETCRLF)
    tn.read_until("\r\n> ")
    # ------- Control Console -------
    # 1- Device Manager
    # 2- Network
    # 3- System
    # 4- Logout
    # <ESC>- Main Menu, <ENTER>- Refresh, <CTRL-L>- Event Log

    tn.write("4" + TELNETCRLF)
    # print tn.read_all()
    return 100


def do_powercontrol():
    global BOARD 
    HOST = "192.168.0.195"
    USER = "apc"
    PASSWORD  = "apc"
    telneti = 0
    while telneti < TELNETRETRY: 
        ret = do_telnet(HOST, USER, PASSWORD, BOARD)
        telneti += 1
        if ret == 100:
            print "power control successfully"
            telneti -= 1
            break
        elif ret == 200:
            print "== telnet retry %d ==" % telneti 
            time.sleep(8)
        elif ret == 300:
            print "the board does not exist !! "
            break
    
    if telneti == TELNETRETRY: 
        print "========= telnet failed ============="
        return False
    else:
        time.sleep(RESETWAIT)
        return True
    

class Miniterm(object):
    def __init__(self):
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        global TTY
        self.ser.port = TTY
        self.ser.timeout = 1

    def reader(self):
        now = datetime.datetime.now()
        exittime = now + datetime.timedelta(seconds=200)
        while True:
            data = self.ser.readline()
            sys.stdout.write(data)
            iternow = datetime.datetime.now()
            if iternow >= exittime:
                break

    def readtestdone(self):
        readtimes = 0
        while True:
            data = self.ser.readline()
            if data:
                sys.stdout.write(data)
                if (data.find(TESTDONE) >= 0):
                    break
            else:
                readtimes += 1
                if (readtimes > TESTCOUNT):
                    break

    def readhitkey(self):
        while True:
            data = self.ser.readline()
            sys.stdout.write(data)
            if data.find(HITKEY) == 0:
                break

    def readbytestransfer(self):
        while True:
            data = self.ser.readline()
            if data:
                sys.stdout.write(data)
                if (data.find(TFTPERR1) >= 0):
                    return False
                elif data.find(TFTPERR2) >= 0:
                    return False
                elif data.find(TFTPERR3) >= 0:
                    return False
                elif data.find(BYTESTRANSFER) == 0:
                    return True

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

    def close(self):
        self.ser.close()
        time.sleep(1)


def updateArguments():
    global TTY
    global BOARD
    global TESTUSER

    if len(sys.argv) >= 2:
        BOARD = int(sys.argv[1])

    if len(sys.argv) >= 3:
        TESTUSER = sys.argv[2]

    global SETIPADDR 
    if (BOARD == 1):
        TTY = TTY + '0'
        SETIPADDR = SETIPADDR + '1'
    elif (BOARD == 2):
        TTY = TTY + '1'
        SETIPADDR = SETIPADDR + '2'
    elif (BOARD == 3):
        TTY = TTY + '2'
        SETIPADDR = SETIPADDR + '3'
    else:
        print "the board does not exist !! "
    
    print "TTY == %s " %  TTY
    print "SETIPADDR == %s " %  SETIPADDR  

def main():
    # print '===================  start   ====================='
    # print time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    # print '=================================================='
    global TESTUSER
    caseindex = 1
    for casename in CASELIST:
        casename = TESTUSER + '/' + casename
        '''
        print case name in terminal
        '''
        print '\n'
        print '----------------------------------------'
        print  casename
        print '----------------------------------------'
        caseindex += 1
        
        '''
        open the console
        '''
        ret = do_powercontrol()
        if not ret:
            print "power control failed."
            return 22
        
        global BOARD
        if  (BOARD == 4):
            time.sleep(WAITAUTOBOOT01)
            miniterm = Miniterm()
            miniterm.open() 
            miniterm.readhitkey() 
        elif (BOARD == 2) or (BOARD == 1) or (BOARD == 3):
            time.sleep(WAITAUTOBOOT2)
            miniterm = Miniterm()
            miniterm.open() 
        else:
            print "Board not exist."
            return 33

        miniterm.writer(MINICOMCRLF)
        miniterm.writer(MINICOMCRLF)
        
        '''
        set environments
        '''
        miniterm.writer(SETSERVERIP + MINICOMCRLF)
        global SETIPADDR 
        miniterm.writer(SETIPADDR + MINICOMCRLF)
        
        '''
        tftp
        '''
        TFTPDOWNLOAD = 'tftp 200000 ' + casename
        miniterm.writer(TFTPDOWNLOAD + MINICOMCRLF)
        ret = miniterm.readbytestransfer()
        if not ret:
            print "tftp error"
            return 44
        
        '''
        run the case
        '''
        miniterm.writer(GOENTRY + MINICOMCRLF)
        
        miniterm.reader() 
        # miniterm.readtestdone() 

        '''
        close the console
        '''
        miniterm.close()
    
    return 55

    # print '===================  end   ======================='
    # print time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    # print '=================================================='

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    updateArguments()
    ret = main()
    if ret == 55:
        sys.exit(0)
    else:
        sys.exit(88)

