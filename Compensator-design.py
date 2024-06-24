# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:25:59 2023

@author: Alonso
"""

# Off-line Flyback LED driver

# Compensator design

from math import pi, log10

kd=4.93
kpwm=1
fp=8.81; fz=2.62e3
CTR=0.5; R1=5e3
C2=1e-6; Cop= 10e-9


Rserie= 1/(2*pi*fp*C2)
R2= Rserie - R1
Rc= 1/(2*pi*fz*Cop)
Rop= (R1+R2)*Rc*CTR/(R1*kd*kpwm)

# ganancia dc del opto
Gdc_opto = 20*log10(Rc*CTR/Rop)
# ganancia del opamp a frec. medias
Gdc_opamp= 20*log10((R1+R2)/R1)
# ganacia dc total a frec. medias
Gdc= Gdc_opto + Gdc_opamp


print("R2 (kOhm)= ", R2/1000)
print("Rc(kOhm)= ", Rc/1000)
print("Rop(kOhm)= ", Rop/1000)
print("Gdc_opto (dB)= ", Gdc_opto)
print("Gdc_opamp (dB)= ", Gdc_opamp)
print("Gdc (dB)= ", Gdc)

