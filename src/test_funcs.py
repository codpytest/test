import wrap
import numpy as np
#import inv

def test_add():
    assert(wrap.add(3, 4) == 7)

if __name__ == '__main__':
    test_add()
    print(wrap.add(3, 4))
    A = np.random.randn(100,3)
    b = A @ np.random.randn(3,1)
    #x = inv.lstsq(A,b)