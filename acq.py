

#!/usr/bin/env python3
# sudo chmod a+rw /dev/ttyACM0
import pickle
import pyfirmata
import time
import numpy as np
import random
import matplotlib.pyplot as plt



board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()
analog_pin = board.get_pin('a:0:i')
out_pin = board.get_pin('d:6:p')
#board.analog[0].enable_reporting()
print("Communication Successfully started")


duration =60
start_time = time.time()
data = []
while (time.time() - start_time) < duration:
    
    val = analog_pin.read()
        #val = board.analog[0].read()
    data.append(val)
        #time.sleep(.001)
        
data = np.array(data)
data = data[data !=np.array(None)]
print("Acq data: ", data)
filename = "data.pickle"
pickle.dump(data,open(filename, "wb"))
print("End of loop: Time taken", time.time() - start_time)
#tme.sleep(.5)







