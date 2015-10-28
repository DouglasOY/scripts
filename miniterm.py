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
# telnet keywords
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
stateon         = "State        : ON"
stateoff        = "State        : OFF"
TELNETRETRY     = 20
MINICOMCRLF     = '\n'
TELNETCRLF      = '\r'
RESETWAIT       = 10

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# tftp keywords
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
HITKEY          = 'Hit any key to stop autoboot'
BYTESTRANSFER   = 'Bytes transferred = '
TFTPERR1        = 'Retry count exceeded; starting again'
TFTPERR2        = 'Not retrying'
TFTPERR3        = 'Auto-negotiation error is present'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# wait seconds in uboot
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
WAITAUTOBOOT1   = 2
WAITAUTOBOOT2   = 6


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


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# power on or reboot the board
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def do_powercontrol(board):
    HOST = "192.168.0.195"
    USER = "apc"
    PASSWORD  = "apc"
    telneti = 0
    while telneti < TELNETRETRY:
        ret = do_telnet(HOST, USER, PASSWORD, board)
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


class Miniterm:
    def __init__(self, board, runtime):
        self.board = board
        self.runtime = runtime
        self.ser = serial.Serial()
        self.ser.baudrate = 115200
        self.ser.timeout = 1
        # '/dev/ttyU0'  '/dev/ttyU1'  '/dev/ttyU2'
        TTY = '/dev/ttyU' + str(self.board - 1)
        self.ser.port = TTY

    def reader(self):
        now = datetime.datetime.now()
        exittime = now + datetime.timedelta(seconds=self.runtime)
        while True:
            data = self.ser.readline()
            sys.stdout.write(data)
            iternow = datetime.datetime.now()
            if iternow >= exittime:
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


def main(board, ip, casename, runtime):
    # print '===================  start   ====================='
    # print time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    # print '=================================================='
    '''
    print case name
    '''
    print '----------------------------------------'
    print  casename
    print '----------------------------------------'

    '''
    open the console
    '''
    ret = do_powercontrol(board)
    if not ret:
        print "power control failed."
        return 2

    # old uboot
    if (board == 4):
        time.sleep(WAITAUTOBOOT1)
        miniterm = Miniterm(board, runtime)
        miniterm.open()
        miniterm.readhitkey()
    # new uboot
    elif (board == 1) or (board == 2) or (board == 3):
        time.sleep(WAITAUTOBOOT2)
        miniterm = Miniterm(board, runtime)
        miniterm.open()
    else:
        print "Board not exist."
        return 3

    miniterm.writer(MINICOMCRLF)
    miniterm.writer(MINICOMCRLF)

    '''
    set environments
    '''
    SETSERVERIP = 'setenv serverip ' + ip
    miniterm.writer(SETSERVERIP + MINICOMCRLF)

    # 192.168.0.251 / 192.168.0.252 / 192.168.0.253
    SETIPADDR = 'setenv ipaddr 192.168.0.25' + str(board)
    miniterm.writer(SETIPADDR + MINICOMCRLF)

    '''
    tftp
    '''
    TFTPDOWNLOAD = 'tftp 200000 ' + casename
    miniterm.writer(TFTPDOWNLOAD + MINICOMCRLF)
    ret = miniterm.readbytestransfer()
    if not ret:
        print "tftp error"
        return 4

    '''
    run the case
    '''
    GOENTRY = 'go 200000'
    miniterm.writer(GOENTRY + MINICOMCRLF)

    '''
    output of the case
    '''
    miniterm.reader()

    '''
    close the console
    '''
    miniterm.close()

    # print '===================  end   ======================='
    # print time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
    # print '=================================================='
    return 0


def usage():
    helpstring = '''
Usage: <script> [options]

Options:
  -h, --help            show this help message and exit
  -b, --board=number    avnet board number [1 2 3], default is 3
  -i, --ip=IP           ip address of tftp server, default is 192.168.0.190
  -p, --path=imagepath  image path under the tftp root path
  -t, --time=seconds    how much time booting the image will take, default is 15 seconds

Example:
  <script> --board=1 --ip=192.168.0.190 --path=auto/ktos_tests/tests_ktos.bin

'''
    print helpstring
    sys.exit(2)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:i:p:t:", ["help", "board=", "ip=", "path=", "time="])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    board = 3
    ip = "192.168.0.190"
    casename = None
    runtime = 15
    for opt, value in opts:
        if opt in ("-h", "--help"):
            usage()
        elif opt in ("-b", "--board"):
            board = int(value)
            if not ((board == 1) or (board == 2) or (board ==3)):
                print "the board does not exist !! "
                sys.exit(2)
        elif opt in ("-i", "--ip"):
            ip = value
        elif opt in ("-p", "--path"):
            casename = value
        elif opt in ("-t", "--time"):
            runtime = int(value)
        else:
            assert False, "unhandled option"

    ret = main(board, ip, casename, runtime)
    if ret == 0:
        sys.exit(0)
    else:
        sys.exit(1)



