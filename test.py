from executioner import Executioner as ex

class test(object):
    def __init__(self):
        self.out_param = 'int'
        self.double_param = 'int'
    def out(self, dope):
        print(dope)
    def double(self, num):
        print(num*2)

if __name__ == '__main__':
    t = test()
    e = ex(t)

