import time
import numpy as np
y=[]
def simadder(x):
    B=0
    S=[0,0,0]
    for i in x:
        A=i
        B=S[2]
        S=[A+B,S[0],S[1]]
        y.append(B)
    return y
print(simadder([9,7,4,1,3,6,8,9,6,7,5,2,3,7,9,4,6,5,4,3]))
