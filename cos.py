import numpy as np
import matplotlib.pyplot as plt
A=input("Enter Amplitude:")
f1=input("Enter Frequency:")
fs=10000
n=np.arange(0,fs,0.1)
fnc=A*(np.cos(2*np.pi*f1*n/fs))
plt.plot(n,fnc)
plt.title('Cosine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.show()

print(fnc)