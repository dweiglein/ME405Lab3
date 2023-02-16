import time
import pyb
from mma845x import MMA845x

if __name__ == "__main__":
    aye = pyb.I2C(1, pyb.I2C.CONTROLLER)
    res = pyb.I2C.scan(aye)
    print(res)
    
    i2c = pyb.I2C (1, pyb.I2C.MASTER, baudrate = 100000)
    accel1 = MMA845x (i2c, 29)
    accel1.active()
    
    while True:
        accel = accel1.get_accels()
        print(accel)
    
    

    