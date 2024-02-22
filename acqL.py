
#sudo chmod a+rw /dev/ttyACM0



import serial 
import time
import numpy as np
#import random
#from scipy import stats #import iqr
#from sklearn import svm
import pickle


arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)



duration = 8
dur = 1750
start_time = time.time()
data = np.zeros((dur, 2))
ddd = 100
for ii in range(dur):
    
    eog = arduino.readline().rstrip()
    
    t = time.time()
        #val = board.analog[0].read()
    try:
    	data[ii,0] = (t)
    	data[ii,1] = float(eog)
    	    #ddd = data[ii-1,:]
    	print([[t], [data[ii,1]]])
        #ddd =float(eog)
        #cc = float(eog)
        
    except: pass
data = np.array(data)
#data = data[data !=np.array(None)]
#print("Acq data: ", data)
filename = "eog_record8.pickle"
pickle.dump(data,open(filename, "wb"))
print("End of loop: Time taken", time.time() - start_time)



