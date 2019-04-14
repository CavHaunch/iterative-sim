import numpy as np 
import json

def execute(motor_tc=70,turbo_tc=100):
    dT = 1
    T = 15*60
    n = T// dT
    t = 1
    motor = np.zeros(n)
    turbo = np.zeros(n)
    vacuum = np.zeros(n)
    motor[0] = 3
    turbo[0] = motor[0]
    vacuum[0] = motor[0]

    while t < T:
        a1 = 1-1/motor_tc
        c = -1
        a2 = c*(1-a1)
        motor[t] = a1 *(motor[t-1]+a2)
        motor[t] = motor[t] + 0.05*(2*(np.random.rand()-0.5))
        turbo[t] = 0
        if t>5:
            slic = motor[t-5:t]
            mean = np.mean(slic) 
            if mean < 0:
                a1 = 1-1/turbo_tc
                c = -7
                a2 = c*(1-a1)
                turbo[t] = a1 *(turbo[t-1]+a2)
        vacuum[t] = motor[t] + turbo[t]
        t = t+1
    
    return vacuum