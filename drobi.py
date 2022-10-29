from math import gcd

class Drobi:
    def __init__(self, a, b):
        self.verx = a
        self.niz = b

    def __str__(self):
        return f"{self.verx} / {self.niz}"

    def __add__(self, v):

        if isinstance(v, Drobi):
            v = str(v).split()
            dea = int(gcd((int(self.verx) * int(v[2])), (int(v[0]) * int(self.niz))))
            return str(f"{(int((self.verx) * int(v[2])) + (int(v[0]) * int(self.niz)) / dea)} / {int((self.niz) * int(v[2]) / dea)}")


        if int(v):
            dea = int(gcd(self.verx + (v * self.niz), self.niz))
            return str(f"{int((self.verx + (v * self.niz)) / dea)} / {int((self.niz) / dea)}")

        elif float(v):
            dea = int(gcd(self.verx + (v * self.niz), self.niz))
            return str(f"{int(((self.verx + (v * self.niz)) / dea))} / {int((self.niz) / dea)}")

    def __sub__(self, f):
        if isinstance(f, Drobi):
            f = str(f).split()
            dea = (gcd(int(((self.verx) * int(f[2])) - (int(f[0]) * int(self.niz)))), int((self.niz) * int(f[2])))
            print(dea)
            return str(f"{(int(((self.verx) * int(f[2]) - (int(f[0]) * int(self.niz))) / dea))} / {int((self.niz) * int(f[2]) / dea)}")

        if int(f):
            dea = int(gcd(self.verx - (f * self.niz), self.niz))
            return str(f"{int((self.verx - (f * self.niz)) / dea)} / {int((self.niz) / dea)}")

        elif float(f):
            dea = int(gcd(self.verx - (f * self.niz), self.niz))
            return str(f"{int((self.verx - (f * self.niz)) / dea)} / {int((self.niz) / dea)}")


    def __mul__(self, negr):
        if isinstance(negr, Drobi):
            negr = str(negr).split()
            dea = int(gcd(int(self.verx) * int(negr[0]), int(self.verx) * int(negr[2])))
            return str( f"{int(((self.verx) * int(negr[0])) / dea)} / {int((self.verx) * int(negr[2]) / dea)}" )

        if int(negr):
            dea = int(gcd(self.verx * (negr * self.niz), self.niz))
            return str(f"{int((self.verx * (negr * self.niz) / dea))} / {int((self.niz) / dea)}")

        elif float(negr):
            dea = int(gcd(self.verx * (negr * self.niz), self.niz))
            return str(f"{(self.verx * (negr * self.niz) / dea)} / {(self.niz) / dea}")

    def __truediv__(self, a):
        if isinstance(a, Drobi):
            a = str(a).split()
            dea = int(gcd(int(self.verx) * int(a[2]), int(self.niz) * int(a[0])))
            return str( f"{int((self.verx) * int(a[2])) / dea} / {int((self.niz) * int(a[0]) / dea)}" )





a = Drobi(1, 3)



b = Drobi(1, 4)


print(a + b)
print(a - b)
print(a * b)
print(a / b)
