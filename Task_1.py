import math
class TASK:
    def __init__(self, C_a, P_n, C_f, T_f, T_t, T_c, C_t):
        self.C_a = C_a
        self.P_n = P_n
        self.C_f = C_f
        self.T_f = T_f
        self.T_t = T_t
        self.T_c = T_c
        self.C_t = C_t

    def product(self):
        i = self.P_n / self.C_a
        return math.ceil(i)

    def calculate(self):
        X = self.C_f * self.T_f * self.T_t
        Y = self.T_c * self.T_t
        Z = self.C_t
        ans = X + Y + Z
        return ans

def main():
    C_a = eval(input("the capacity of the aircraft:"))
    P_n = eval(input("the number of passengers:"))
    C_f = eval(input("the cost of fuel per kg:"))
    T_f = eval(input("the trip fuel:"))
    T_t = eval(input("the trip time:"))
    T_c = eval(input("the time related cost per minute of flight:"))
    C_t = eval(input("fixed cost independent of time:"))
    a = TASK(C_a, P_n, C_f, T_f, T_t, T_c, C_t)
    i = a.calculate()
    k = a.product()
    print(int(i * k))

main()