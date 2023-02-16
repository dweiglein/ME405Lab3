
while True:
    aye = pyb.I2C(1, pyb.I2C.CONTROLLER)
    pyb.I2C.scan(aye)