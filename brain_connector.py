__author__ = 'Yusaira Khan'

import OpenBCI_Python.open_bci_v3 as bci


import sys
import time
import atexit
import threading
import timeit
import sender

start_time = None
board = None
main_thread = None
lock = threading.RLock()

CSV_FILE_NAME = 'OpenBCI-RAW-PHIL.txt'
CSV_DELIM = ", "
pause = None
def clean_up():
    board.stop()
    board.disconnect()
    print "Disconnecting"

def csv_writer(sample):

        t = timeit.default_timer() - start_time

        row = ''
        row += str(t)
        row += CSV_DELIM
        row += str(sample.id)
        row += CSV_DELIM
        for i in sample.channel_data:
            row += str(i)
            row += CSV_DELIM
        for i in sample.aux_data:
            row += str(i)
            row += CSV_DELIM
            # remove last comma
        row += '\n'
        with open(CSV_FILE_NAME, 'a') as f:
            f.write(row)
        pause.wait()

def main(port):
    global board
    board = bci.OpenBCIBoard(port=port,scaled_output=True)
    atexit.register(clean_up)
    #atexit.register(sender.clean_up())
    startup()
    sender.start_up()
    command = ''
    while command != 'exit':
        command = raw_input('Program is running. Send "exit" to stop.\n-->')



def startup():
    global start_time, main_thread, pause
    with open(CSV_FILE_NAME, 'w+') as f:
        f.write('')

    main_thread = threading.Thread(target=board.start_streaming, args=(csv_writer,-1))
    for c in 'svcd':
        board.ser.write(c)
        time.sleep(0.100)
    pause = threading.Event()
   # print pause

    pause.set()
    start_time = timeit.default_timer()
    main_thread.daemon =True
    main_thread.start()


if __name__ == '__main__':
    port = sys.argv[1]
    main(port)









