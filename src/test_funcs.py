import wrap

def test_add():
    assert(wrap.add(3, 4) == 7)

if __name__ == '__main__':
    test_add()
    print(wrap.add(3, 4))