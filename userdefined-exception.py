import math

class AbstractError(RuntimeError):
    def __init__(self, s):
        self.s = s

class DuaDimensi(object):
    def __init__(self):
        raise AbstractError("ERROR: '" + "DuaDimensi" + "' adalah kelas abstrack")
    def luas(self):
        raise NotImplementedError
    def keliling(self):
        raise NotImplementedError

class lingkaran(DuaDimensi):
    def __init__(self, r):
        self.r = r
    def luas(self):
        return math.pi * self.r * self.r

def main():

    obj1 = lingkaran(3)


    print("LINGKARAN")
    print("Luas\t\t:", obj1.luas())
    print("Keliling\t:", obj1.keliling())

    try:
        print("\nMembuat objek " + "dari kelas DuaDimensi...")
        obj2 = DuaDimensi()
    except AbstractError as error:
        print (error.s)
    else :
            print("DUADIMENSI")
            print("Luas\t\t:", obj2.luas())
            print("Keliling\t:", obj2.keliling())

if __name__ == "__main__":
    main()
    
                            
