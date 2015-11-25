#!/usr/bin/env python

import os
import sys
import serial
import time
import shutil
import telnetlib
import datetime 
import getopt

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CRLF style
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
MINICOMCRLF     = '\n'
TELNETCRLF      = '\r'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# telnet to the board manager
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
    elif board == 4:
        tn.write("8" + TELNETCRLF)
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

    stateon  = "State        : ON"
    stateoff = "State        : OFF"
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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# power on or reboot the board
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def do_powercontrol(board):
    HOST = "192.168.0.15"
    USER = "test"
    PASSWORD  = "test"
    count = 0
    TELNETRETRY = 50
    RESETWAIT = 10
    while count < TELNETRETRY:
        ret = do_telnet(HOST, USER, PASSWORD, board)
        count += 1
        if ret == 100:
            print "==== reboot/turn_on the board successfully ===="
            count -= 1
            break
        elif ret == 200:
            print "==== telnet retry %d ====" % count
            time.sleep(8)
        elif ret == 300:
            print "the board does not exist !! "
            break
    
    if count == TELNETRETRY:
        print "======== telnet failed ========"
        return False
    else:
        # boarda need to wait for a while
        if (board == 1) or (board == 2) or (board == 3):
            time.sleep(RESETWAIT)
        return True
    

class Miniterm:
    def __init__(self, board):
        if board == 1:
            TTY = '/dev/ttyU0'
        elif board == 2:
            TTY = '/dev/ttyU1'
        elif board == 3:
            TTY = '/dev/ttyU2'
        elif board == 4:
            TTY = '/dev/ttyUSB0'
        else:
            TTY = None

        self.ser = serial.Serial(port = TTY, baudrate = 115200, timeout = 1)

    def readseconds(self, runtime):
        exittime = datetime.datetime.now() + datetime.timedelta(seconds=runtime)
        while True:
            data = self.ser.readline()
            sys.stdout.write(data)
            now = datetime.datetime.now()
            if now >= exittime:
                break

    def readkeywordtimeout(self, keyword, timeout):
        exittime = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
        while True:
            data = self.ser.readline()
            sys.stdout.write(data)
            if data.find(keyword) >= 0:
                return True
            elif datetime.datetime.now() >= exittime:
                return False

    def readtimeout(self, keyword, timeoutcount):
        readtimes = 0
        while True:
            data = self.ser.readline()
            if data:
                readtimes = 0
                sys.stdout.write(data)
                if data.find(keyword) >= 0:
                    return True
            else:
                readtimes += 1
                if readtimes > timeoutcount:
                    return False

    def readbytestransfer(self):
        BYTESTRANSFER = 'Bytes transferred = '
        TFTPERR1      = 'Retry count exceeded; starting again'
        TFTPERR2      = 'Not retrying'
        TFTPERR3      = 'Auto-negotiation error is present'
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
            print '#### open console True ####'
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
        EXITCMD = 'exitcom'
        PROMPT = '# '
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


def boarda_default(board, ip, casename, runtime):
    print '----------------------------------------'
    print ' boarda default job: %s' % casename
    print '----------------------------------------'
    
    miniterm = Miniterm(board)
    miniterm.open() 

    miniterm.writer(MINICOMCRLF)
    miniterm.writer(MINICOMCRLF)
    
    '''
    set environments
    '''
    SETSERVERIP = 'setenv serverip ' + ip
    miniterm.writer(SETSERVERIP + MINICOMCRLF)

    # 192.168.0.51 / 192.168.0.52 / 192.168.0.53
    SETIPADDR = 'setenv ipaddr 192.168.0.5' + str(board)
    miniterm.writer(SETIPADDR + MINICOMCRLF)
    
    '''
    tftp
    '''
    TFTPDOWNLOAD = 'tftp 200000 ' + casename
    miniterm.writer(TFTPDOWNLOAD + MINICOMCRLF)
    ret = miniterm.readbytestransfer()
    if not ret:
        print "tftp error"
        return False
    
    '''
    run the case
    '''
    GOENTRY = 'go 200000'
    miniterm.writer(GOENTRY + MINICOMCRLF)
    
    '''
    output of the case 
    '''
    miniterm.readseconds(runtime)

    '''
    close the console
    '''
    miniterm.close()
    
    return True


def boarda_typea(board, ip, casename):
    print '----------------------------------------'
    print ' boarda typea job: %s' % casename
    print '----------------------------------------'
    
    miniterm = Miniterm(board)
    miniterm.open() 

    miniterm.writer(MINICOMCRLF)
    miniterm.writer(MINICOMCRLF)
    
    '''
    set environments
    '''
    SETSERVERIP = 'setenv serverip ' + ip
    miniterm.writer(SETSERVERIP + MINICOMCRLF)

    # 192.168.0.51 / 192.168.0.52 / 192.168.0.53
    SETIPADDR = 'setenv ipaddr 192.168.0.5' + str(board)
    miniterm.writer(SETIPADDR + MINICOMCRLF)
    
    '''
    tftp
    '''
    TFTPDOWNLOAD = 'tftp 100000 boarda_typea/image.bin'
    miniterm.writer(TFTPDOWNLOAD + MINICOMCRLF)
    ret = miniterm.readbytestransfer()
    if not ret:
        print "tftp error"
        return False
    
    '''
    run the case
    '''
    GOENTRY = 'go 100000'
    miniterm.writer(GOENTRY + MINICOMCRLF)
    
    '''
    output of the case 
    '''
    TESTDONE = 'Test Done'
    ret = miniterm.readtimeout(TESTDONE, 80)
    if ret:
        miniterm.readseconds(1)
    else:
        if casename.find('run_error') >= 0:
            print '\n\n[[[[[[[[[[[[[[[[[[[ run error case ]]]]]]]]]]]]]]]]]]]'
            print casename + '\n\n'
        else:
            # - - - - - - - - - - - - - - - - - - - - - - - -
            # for real timeout case, try a longer time again
            # - - - - - - - - - - - - - - - - - - - - - - - -
            ret = miniterm.readtimeout(TESTDONE, 200)
            if ret:
                miniterm.readseconds(1)
            else:
                print '\n\n[[[[[[[[[[[[[[[[[[[ time out case ]]]]]]]]]]]]]]]]]]]'
                print casename + '\n\n'

    '''
    close the console
    '''
    miniterm.close()
    
    return True


def boarda_jobs(board, ip, casename, runtime, job):
    ret = False
    # - - - - - - - - - - -
    # wait seconds in uboot
    # - - - - - - - - - - -
    WAITAUTOBOOT = 6
    time.sleep(WAITAUTOBOOT)
    if job == 'default':
        ret = boarda_default(board, ip, casename, runtime)
    elif job == 'typea':
        ret = boarda_typea(board, ip, casename)
    else:
        print "Job not found."
        
    return ret


def boardb_default(board):
    print '----------------------------------------'
    print 'boardb default job'
    print '----------------------------------------'
    
    miniterm = Miniterm(board)
    miniterm.open() 

    ret = miniterm.readbytestransfer()
    if not ret:
        print "tftp error"
        return False

    '''
    output of the case 
    '''
    ret = miniterm.readkeywordtimeout('Copyright: Beijing China', 20)
    if not ret:
        print "time out error"
        return False

    miniterm.readseconds(1)
    miniterm.writer(MINICOMCRLF)
    miniterm.writer(MINICOMCRLF)
    miniterm.readseconds(1)

    '''
    close the console
    '''
    miniterm.close()
    
    return True

def boardb_testb(board, runtime):
    print '----------------------------------------'
    print 'boardb testb job'
    print '----------------------------------------'
    
    miniterm = Miniterm(board)
    miniterm.open() 

    ret = miniterm.readbytestransfer()
    if not ret:
        print "tftp error"
        return False

    '''
    output of the case 
    '''
    ret = miniterm.readkeywordtimeout('Copyright: Beijing China', 20)
    if not ret:
        print "time out error"
        return False

    TESTDONE = "Built by GNU GCC"
    ret = miniterm.readkeywordtimeout(TESTDONE, runtime)
    if not ret:
        print "time out error"
        return False

    miniterm.readseconds(1)

    '''
    close the console
    '''
    miniterm.close()
    
    return True


def boardb_jobs(board, runtime, job):
    ret = False
    if job == 'default':
        ret = boardb_default(board)
    elif job == 'testb':
        ret = boardb_testb(board, runtime)
    else:
        print "Job not found."
        
    return ret


def main(board, ip, casename, runtime, job):
    '''
    open the console
    '''
    ret = do_powercontrol(board)
    if not ret:
        print "power control failed."
        return 2

    if (board == 1) or (board == 2) or (board == 3):
        ret = boarda_jobs(board, ip, casename, runtime, job)
        if not ret:
            print "run image error"
            return 4
    elif (board == 4):
        ret = boardb_jobs(board, runtime, job)
        if not ret:
            print "run image error"
            return 4
    else:
        print "Board not exist."
        return 3

    return 0


def usage():
    helpstring = '''
Usage: <script> --board=<NUMBER> --ip=<IPADDRESS> --path=<IMAGEPATH> --job=<JOB> --time=<TIME>

Options:
  -b, --board=number    board number [1 2 3 4]. 1/2/3 is boarda, 4 is boardb.
  -i, --ip=ipaddress    ip address of tftp server, default is 192.168.0.10
  -j, --job=JOB         test job name
  -p, --path=imagepath  image path under the tftp root path
  -t, --time=seconds    how long booting the image will take, default is 15 seconds
  -h, --help            show this help message and exit

Example:
  <script> --board=1 --ip=192.168.0.10 --path=auto/testb/image.bin
  <script> --board=4 --time=10

'''
    print helpstring
    sys.exit(2)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:i:j:p:t:", ["help", "board=", "ip=", "job=", "path=", "time="])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    board = 3
    ip = '192.168.0.10'
    casename = None
    runtime = 15
    job = 'default'
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-b", "--board"):
            board = int(arg)
            if not ((board == 1) or (board == 2) or (board == 3) or (board == 4)):
                print "the board does not exist !! "
                sys.exit(2)
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-j", "--job"):
            job = arg
        elif opt in ("-p", "--path"):
            casename = arg
        elif opt in ("-t", "--time"):
            runtime = int(arg)
        else:
            assert False, "unhandled option"

    ret = main(board, ip, casename, runtime, job)
    if ret == 0:
        sys.exit(0)
    else:
        sys.exit(1)

