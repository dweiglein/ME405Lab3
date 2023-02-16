import time
import pyb
import mma845x
from pyb import I2C

if __name__ == "__main__":
    aye = pyb.I2C(1, pyb.I2C.CONTROLLER)
    res = pyb.I2C.scan(aye)
    print(res)
    
    accel1 = mma845x.MMA845x(pyb.I2C(1, pyb.I2C.MASTER, baudrate = 100000), 29)
    accel1.active()
    
    while True:	
        accel = accel1.get_accels()
        print(accel)
        pyb.delay(500)
    
    

    