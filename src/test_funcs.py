import numpy as np
import inv
from matplotlib import pyplot as plt

if __name__ == '__main__':
    A = np.random.randn(100,3)
    b = A @ np.random.randn(3,1)

    #print(inv.inv(A))            
    x = inv.lstsq(A,b)
    plt.plot(A @ x)
    plt.plot(b)
    plt.show()