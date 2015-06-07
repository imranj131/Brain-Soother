__author__ = 'Yusaira Khan'

import socket
import json
#import csvMat
import brain_connector
import time
import soundGenerator
import os
import multiprocessing
import  threading
import csvMat
import freq_FFT

UDP_PORT=8888
HOST="127.0.0.1"
target_freq  = 15
brain_freq = 10
current_duration = 1


server=None
pool = None
sending_thread = None
def clean_up():
    global  server
    server.close()


def start_up():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    pool = multiprocessing.Pool(processes=2)
    sending_thread = threading.Thread(target=process_and_send)
    sending_thread.daemon = True
    #subprocess.Popen('node d3_socket_server.js', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sending_thread.start()

def process_and_send():


    global target_freq,brain_freq, current_duration
    matrix = csvMat.cleanData(brain_connector.CSV_FILE_NAME)
    brain_freq = freq_FFT.meanFFT(matrix)

    diff = abs(target_freq - brain_freq)
    if  diff < 0.1:
        target_freq += diff**0.25
    data =[target_freq,current_duration]
    udp_sender(data)
    sound_sender(data)
    with open(brain_connector.CSV_FILE_NAME, 'w') as f:
        f.write('')




def udp_sender(data):
    server.sendto(json.dumps(data), (HOST, UDP_PORT))

def sound_sender(data):
    soundGenerator.soundGenerator(freq=data[0],stimDur=data[1])
