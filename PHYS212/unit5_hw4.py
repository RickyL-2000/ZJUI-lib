k = 9e9
a = 0.025
Qin = -3e-9
b = 0.06
c = 0.09
Qout = 2e-9

Vout = k*(Qin+Qout)/c
Vin_minus_Vout = k*Qin*(1/a-1/b)    # 只能算球壳外面的
Vin = Vout + Vin_minus_Vout
print(Vin)