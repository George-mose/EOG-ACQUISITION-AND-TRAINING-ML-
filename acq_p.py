

#!/usr/bin/env python3
# sudo chmod a+rw /dev/ttyACM0

import pyfirmata
import time
import numpy as np
import random
from scipy import stats #import iqr
from sklearn import svm
import pickle
from sklearn.preprocessing import MinMaxScaler, RobustScaler


board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()
analog_pin = board.get_pin('a:0:i')
out_pin = board.get_pin('d:6:p')
#board.analog[0].enable_reporting()
print("Communication Successfully started")

filename = "TrainedModel-svm.pickle"
model = pickle.load(open(filename, "rb"))

duration = 0.6

while True:
    start_time = time.time()
    data = []
    while (time.time() - start_time) < duration:
    
        val = analog_pin.read()
        #val = board.analog[0].read()
        data.append(val)
        #time.sleep(.001)
        print("Data: ",val)
        
    data = np.array(data)
    data = data[data !=np.array(None)]


    print("End of prediction: Time taken", time.time() - start_time)
    time.sleep(.5)






